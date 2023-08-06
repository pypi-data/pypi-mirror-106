#!/usr/bin/env python3
# Copyright 2021 Tolteck

import argparse
import asyncio
from datetime import datetime
import fileinput
import os
import random
import re
import shlex
import shutil
import socket
import string
import sys
from tempfile import TemporaryDirectory

import aiocouch


__version__ = '0.1.0'
# Tweak this parameter to your needs: From 17 minutes with 16 workers to 28
# minutes with 8 workers for 10^5 databases on my machine.
N_WORKERS = 16


async def subprocess(*args, **kwargs):
    # For debugging purposes:
    # print('> ' + args[0])
    p = await asyncio.create_subprocess_shell(*args, **kwargs,
                                              stdout=asyncio.subprocess.PIPE,
                                              stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await p.communicate()
    stdout, stderr = stdout.decode(), stderr.decode()
    if p.returncode == 0:
        return stdout
    raise Exception(f'Command {args[0]} returned code {p.returncode}, stdout: '
                    f'{stdout}, stderr: {stderr}')


async def backup(hostname, path, output, reuse_folder):
    # Keep this line otherwise TemporaryDirectory doesn't auto-cleanup
    tmp_dir = TemporaryDirectory(prefix='couchcopy-')
    tmp_path = reuse_folder or tmp_dir.name
    if not os.path.exists(tmp_path + '/data'):
        os.mkdir(tmp_path + '/data')

    with open(tmp_path + '/metadata.yaml', 'w') as f:
        f.write(f'backup:\n'
                f'  date: {datetime.now().isoformat()}\n'
                f'  source: {hostname},{path}\n'
                f'couchcopy:\n'
                f'  version: {__version__}\n')

    # rsync is used to copy from distant machine, but also to save files
    # in a specific order, and to avoid using `tar` on files that are used in
    # parallel by a running CouchDB.
    print('[rsync...]')
    hostname = hostname + ':' if hostname != 'localhost' else ''
    await subprocess(f'rsync --del --ignore-missing-args '
                     f'-av {hostname}{path}/.shards {tmp_path}/data')
    await subprocess(f'rsync --del '
                     f' -av {hostname}{path}/_dbs.couch {tmp_path}/data')
    await subprocess(f'rsync --del --ignore-missing-args '
                     f'-av {hostname}{path}/shards {tmp_path}/data')

    print('[tar...]')
    await subprocess(f'tar -I pigz -cf {output} -C {tmp_path} .')
    # For debugging purposes:
    # import shutil
    # if tmp_dir:
    #     shutil.rmtree('/tmp/couchcopy', True)
    #     shutil.copytree(tmp_dir.name, '/tmp/couchcopy')


async def couch_conn(url, user, password):
    conn = aiocouch.CouchDB(url, user=user, password=password)
    for i in range(25):
        try:
            await conn.info()
            return conn
        except Exception as e:
            error = e
            await asyncio.sleep(0.2)
    await conn.close()
    raise Exception('Cannot connect to CouchDB server: ' + repr(error))


async def do_in_parallel(func, generator, url, user, password):
    async def work_producer(generator, queue):
        block = []
        # Give the consumers block of 100 databases:
        async for item in generator:
            block.append(item)
            if len(block) >= 100:
                await queue.put(block)
                block = []
        if len(block):
            await queue.put(block)

    async def work_consumer(func, queue):
        async with await couch_conn(url, user, password) as couch:
            while True:
                try:
                    block = await queue.get()
                except asyncio.exceptions.CancelledError:
                    break
                for item in block:
                    await func(couch, item)
                queue.task_done()
    queue = asyncio.Queue(maxsize=N_WORKERS)
    # Launch a work "producer" and N parallel "consumer" workers:
    producer = asyncio.create_task(work_producer(generator, queue))
    consumers = [asyncio.create_task(work_consumer(func, queue))
                 for i in range(N_WORKERS)]
    # Wait for either:
    # 1. The producer to have output all databases.
    # 2. Any consumer to return (can happen before 1 in case of an exception).
    await asyncio.wait([producer, *consumers],
                       return_when=asyncio.FIRST_COMPLETED)
    if producer.done():
        # Wait for either:
        # 1. The queue to be fully consumed (consumers to have finished
        #    processing the last items).
        # 2. Any consumer to return (can happen before 1 in case of an
        #    exception).
        await asyncio.wait([asyncio.create_task(queue.join()), *consumers],
                           return_when=asyncio.FIRST_COMPLETED)
    for consumer in consumers:
        consumer.cancel()
    # Exceptions would be raised now:
    await asyncio.gather(*consumers)


async def load(archive):
    tmp_dir = TemporaryDirectory(prefix='couchcopy-')
    os.mkdir(tmp_dir.name + '/etc')
    os.mkdir(tmp_dir.name + '/etc/local.d')
    os.mkdir(tmp_dir.name + '/data')
    creds = 'admin', ''.join(
            random.choice(string.ascii_letters + string.digits)
            for _ in range(10))
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s1.bind(('localhost', 0))
    _, port1 = s1.getsockname()
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2.bind(('localhost', 0))
    _, port2 = s2.getsockname()
    s1.close()
    s2.close()

    for file in ('vm.args', 'default.ini', 'local.ini'):
        shutil.copy('/etc/couchdb/' + file, tmp_dir.name + '/etc/' + file)
    node_name = 'coucharchive-%s@localhost' % ''.join(
        random.choice(string.ascii_letters + string.digits) for _ in range(10))

    for line in fileinput.input(tmp_dir.name + '/etc/vm.args', inplace=True):
        if re.match(r'^-name \S+$', line):
            print('-name ' + node_name)
        else:
            print(line, end='')

    with open(tmp_dir.name + '/etc/local.d/coucharchive.ini', 'w') as f:
        f.write(f'[chttpd]\n'
                f'port = {port1}\n'
                f'\n'
                f'[httpd]\n'
                f'port = {port2}\n'
                f'\n'
                f'[couchdb]\n'
                f'database_dir = {tmp_dir.name}/data\n'
                f'view_index_dir = {tmp_dir.name}/data\n'
                f'max_dbs_open = 10000\n'
                f'users_db_security_editable = true\n'  # for CouchDB 3+
                f'\n'
                f'[cluster]\n'
                f'q=2\n'  # Change this to match your origin cluster `q`
                f'n=1\n'
                f'\n'
                f'[smoosh]\n'
                f'db_channels = ,\n'
                f'view_channels = ,\n'
                f'\n'
                f'[admins]\n'
                f'%s = %s\n' % creds)

    print('[untar...]')
    await subprocess(f'tar -I pigz --strip-components=2 '
                     f'-xf {archive} -C {tmp_dir.name}/data')

    env = dict(os.environ,
               COUCHDB_ARGS_FILE=tmp_dir.name + '/etc/vm.args',
               COUCHDB_INI_FILES=(tmp_dir.name + '/etc/default.ini ' +
                                  tmp_dir.name + '/etc/local.ini ' +
                                  tmp_dir.name + '/etc/local.d'))
    log = open(tmp_dir.name + '/log', 'w')
    process = await asyncio.create_subprocess_exec(
        'couchdb', env=env, stdout=log, stderr=log)

    async with await couch_conn(
            f'http://localhost:{port1}', creds[0], creds[1]) as couch:
        dbs = await couch.keys(limit=1)
        if not len(dbs):
            print('No databases listed inside CouchDB')
            print(f'Launched CouchDB instance at '
                  f'http://{":".join(creds)}@localhost:{port1}')
            await process.wait()
            return
        _, data = await couch._server._get(f'/_node/_local/_dbs/{dbs[0]}')
        shard_ranges = sorted(list(data['by_range'].keys()))
        q_from_archive = len(shard_ranges)
        _, data = await couch._server._get('/_node/_local/_config')
        q_from_cluster = int(data['cluster']['q'])
        assert q_from_cluster == q_from_archive, (
            f'Error q from CouchDB != q from archive, {q_from_cluster} != '
            f'{q_from_archive}, you need to change the `q` value used by '
            f'CouchDB. For more infos see the README.')

        # Update cluster metadata on CouchDB first node.
        # To understand what below code do, have a look at
        # GET /_node/_local/_dbs/{db} endpoint:
        # https://docs.couchdb.org/en/3.1.1/cluster/sharding.html#updating-cluster-metadata-to-reflect-the-new-target-shard-s
        print('[Updating CouchDB metadata...]')

        async def update_one_db_metadata(couch, db):
            _, data = await couch._server._get(f'/_node/_local/_dbs/{db}')
            data['changelog'] = [["add", shard_range, node_name]
                                 for shard_range in shard_ranges]
            data['by_node'] = {node_name: shard_ranges}
            data['by_range'] = {shard_range: [node_name]
                                for shard_range in shard_ranges}
            await couch._server._put(f'/_node/_local/_dbs/{db}', data=data)

        await do_in_parallel(update_one_db_metadata, aio_all_dbs(couch),
                             f'http://localhost:{port1}', creds[0], creds[1])

    print(f'Launched CouchDB instance at '
          f'http://{":".join(creds)}@localhost:{port1}')
    await process.wait()


async def aio_all_dbs(couch):
    last = None
    while True:
        # Be reasonable and limit to 1000 results per call.
        dbs = await couch.keys(start_key=last, limit=1000)
        if len(dbs) == 0:
            break
        for db_name in dbs:
            yield db_name

        # Use \u0020 (space) because \u0000 is not accepted by CouchDB UCA
        # (Unicode Collation Algorithm) sorter.
        last = '"' + db_name + '\u0020"'


async def restore(archive, cred, hostnames, paths, ports, names, force,
                  couchdb_start, couchdb_stop):
    user, password = cred.split(':')
    urls = [f'http://{hostname if hostname else "localhost"}:{port}'
            for hostname, port in zip(hostnames, ports)]

    # First CouchDB API use
    print('[Checking CouchDB nodes names and n...]')
    ssh = f'ssh {hostnames[0]} ' if hostnames[0] != 'localhost' else ''
    await subprocess(f'{ssh}{couchdb_start}')
    async with await couch_conn(urls[0], user, password) as couch:
        current_names = sorted((
            await couch._server._get('/_membership'))[1]['cluster_nodes'])
        assert current_names == sorted(names), (
            f'Error in names: {current_names} != {sorted(names)}. Try to '
            f'change nodes names with nodename arguments.')
        _, data = await couch._server._get('/_node/_local/_config')
        assert int(data['cluster']['n']) >= len(names), (
            'Error n < nodes count, this is not supported, for more infos see '
            'the README.')

    # Stop CouchDB and delete existing data
    if not force:
        folders = ' & '.join([hostname + ':' + path if hostname else path
                              for hostname, path in zip(hostnames, paths)])
        print(f'This command will wipe-out folders {folders}, is it OK? [y/N]')
        answer = input()
        if answer not in ('Y', 'y'):
            print('Operation aborted.')
            sys.exit(1)
    print('[rm...]')
    for hostname, path in zip(hostnames, paths):
        ssh = f'ssh {hostname} ' if hostname != 'localhost' else ''
        await subprocess(f'{ssh}{couchdb_stop}')
        await subprocess(
            f'{ssh}sudo rm -rf {path}/_dbs.couch {path}/_users.couch '
            f'{path}/.delete {path}/._users_design {path}/.shards '
            f'{path}/shards')

    distant = hostnames[0] != 'localhost'
    if distant:
        # There is a strange issue: if a majority of CouchDB nodes don't
        # have the `shards` folder on startup, `_security` of databases are
        # reseted to their default values.
        # This issue is possibly related to:
        # https://github.com/apache/couchdb/issues/1611
        # A workaround is to copy `shards` folder to all nodes, it's what is
        # done here.
        async def rsync(hostname, path):
            await subprocess(
                f'rsync -av {archive} {hostname}:/tmp/couchcopy.tar.gz')

        async def untar(hostname, path):
            # Untar `_dbs.couch` only for the first node.
            exclude = ('' if hostname is hostnames[0] else
                       ' --exclude=_dbs.couch')
            await subprocess(f'ssh {hostname} sudo tar -I pigz '
                             f'--strip-components=2 -xf /tmp/couchcopy.tar.gz '
                             f'-C {path} {exclude}')
            await subprocess(
                f'ssh {hostname} sudo chown -R couchdb:couchdb {path}')
            # `tar` overwrite permissions, restore them
            await subprocess(f'ssh {hostname} sudo chmod +rx {path}')

        print('[rsync...]')
        await asyncio.gather(*(rsync(hostname, path)
                               for hostname, path in zip(hostnames, paths)))
        print('[untar...]')
        await asyncio.gather(*(untar(hostname, path)
                               for hostname, path in zip(hostnames, paths)))
    else:
        print('[untar...]')
        await subprocess(f'sudo tar -I pigz --strip-components=2 '
                         f'-xf {archive} -C {paths[0]}')
        await subprocess(f'sudo chown -R couchdb:couchdb {paths[0]}')
        # `tar` overwrite permissions, restore them
        await subprocess(f'sudo chmod +rx {paths[0]}')

    # Start first CouchDB node
    ssh = f'ssh {hostnames[0]} ' if hostnames[0] != 'localhost' else ''
    await subprocess(f'{ssh}{couchdb_start}')

    # Do a few checks on data from the first database
    async with await couch_conn(urls[0], user, password) as couch:
        dbs = await couch.keys(limit=1)
        if not len(dbs):
            print('No databases listed inside CouchDB')
            return
        _, data = await couch._server._get(f'/_node/_local/_dbs/{dbs[0]}')
        current_names = data['by_node'].keys()
        shard_ranges = sorted(list(data['by_range'].keys()))
        q_from_archive = len(shard_ranges)
        _, data = await couch._server._get('/_node/_local/_config')
        q_from_cluster = int(data['cluster']['q'])
        assert q_from_cluster == q_from_archive, (
            f'Error q from CouchDB != q from archive, {q_from_cluster} != '
            f'{q_from_archive}, you need to change the `q` value used by '
            f'CouchDB. For more infos see the README.')
        if sorted(names) == sorted(current_names):
            print('CouchDB nodes already good in shards')
            return

    # Update cluster metadata on CouchDB first node.
    # metadata are automatically transfered to the other nodes by CouchDB.
    # To understand what below code do, have a look at
    # GET /_node/_local/_dbs/{db} endpoint:
    # https://docs.couchdb.org/en/3.1.1/cluster/sharding.html#updating-cluster-metadata-to-reflect-the-new-target-shard-s
    print('[Updating CouchDB metadata...]')

    async def update_one_db_metadata(couch, db):
        _, data = await couch._server._get(f'/_node/_local/_dbs/{db}')
        data['changelog'] = [["add", shard_range, name]
                             for shard_range in shard_ranges
                             for name in names]
        data['by_node'] = {name: shard_ranges for name in names}
        data['by_range'] = {shard_range: names for shard_range in shard_ranges}
        await couch._server._put(f'/_node/_local/_dbs/{db}', data=data)

    async with await couch_conn(urls[0], user, password) as couch:
        await do_in_parallel(update_one_db_metadata, aio_all_dbs(couch),
                             urls[0], user, password)

    print(f'CouchDB node {names[0]} is now restored, you can use it!')

    # Start other CouchDB nodes
    for hostname in hostnames[1:]:
        ssh = f'ssh {hostname} ' if hostname != 'localhost' else ''
        await subprocess(f'{ssh}{couchdb_start}')

    # Wait for the same number of databases on each nodes.
    print('[Waiting for CouchDB cluster synchronization...]')
    async with await couch_conn(urls[0], user, password) as couch:
        _, data = await couch._server._get('/_dbs')
        node1_dbs_count = data['doc_count'] + data['doc_del_count']
    couchs = [await couch_conn(url, user, password) for url in urls[1:]]
    try:
        dones = []
        while len(dones) < len(couchs):
            for couch, name in zip(couchs, names[1:]):
                if name in dones:
                    continue
                _, data = await couch._server._get('/_dbs')
                dbs_count = data['doc_count'] + data['doc_del_count']
                print(
                    f'{name} sync {(dbs_count / node1_dbs_count) * 100:.0f} %')
                if dbs_count >= node1_dbs_count:
                    dones.append(name)
            await asyncio.sleep(2)
    finally:
        for couch in couchs:
            await couch.close()


async def main():
    examples = (
        'Examples:\n'
        '  couchcopy backup old-server,/var/lib/couchdb backup.tar.gz\n'
        '  couchcopy load backup.tar.gz\n'
        '  couchcopy restore backup.tar.gz \\\n'
        '      admin:password@cluster_vm1,/var/lib/couchdb \\\n'
        '      admin:password@cluster_vm2,/var/lib/couchdb \\\n'
        '      admin:password@cluster_vm3,/var/lib/couchdb\n')

    parser = argparse.ArgumentParser(
            prog='couchcopy', epilog=examples,
            # needed for examples
            formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-v', '--version', action='store_true')
    subparsers = parser.add_subparsers(dest='action')
    sub = {}
    sub['backup'] = subparsers.add_parser(
        'backup', description=('Backup a CouchDB cluster thanks to data of '
                               'one of its node.'))
    sub['backup'].add_argument('couchdb',
                               metavar='hostname,/couchdb/data/folder')
    sub['backup'].add_argument('archive', metavar='backup.tar.gz')
    sub['backup'].add_argument('--rsync-reuse-folder', help=(
        'folder on the local machine to store data reused between executions, '
        'if not set rsync start from scratch'))
    sub['load'] = subparsers.add_parser(
        'load', description='Spawn a local CouchDB and load ata into it.')
    sub['load'].add_argument('archive', metavar='backup.tar.gz')
    # TODO load reuse folder so we don't redo the whole API crap
    sub['restore'] = subparsers.add_parser(
        'restore', description=('Overwrite data of an existing CouchDB. '
                                'Useful to restore a full production cluster '
                                'from a backup.'))
    sub['restore'].add_argument('archive', metavar='backup.tar.gz')
    meta = '[root:password@]hostname[:5984],/couchdb/data/folder[,nodename]'
    sub['restore'].add_argument(
        'couchdbs', metavar=meta, nargs='+', help=(
            'data needed to connect and overwrite existing CouchDB node. If '
            'hostname is not "localhost", ssh will be used to connect to the '
            'remote machine. nodename default is "couchdb@127.0.0.1" if '
            'hostname is "localhost", otherwise it is "couchdb@hostname"'))
    sub['restore'].add_argument('--couchdb-start',
                                default='sudo systemctl start couchdb',
                                help='command-line used to start CouchDB')
    sub['restore'].add_argument('--couchdb-stop',
                                default='sudo systemctl stop couchdb',
                                help='command-line used to stop CouchDB')
    sub['restore'].add_argument('-y', action='store_true', help=(
        'delete existing CouchDB files without asking for confirmation'))

    args = parser.parse_args()
    if args.version:
        print(__version__)
        return
    elif not args.action:
        parser.error('Needs action')
    elif args.action == 'backup':
        splitted = args.couchdb.split(',')
        if len(splitted) != 2:
            sub['backup'].error('wrong "hostname,/couchdb/data/folder"')
        hostname, path = splitted
        if hostname:
            if ':' in hostname or '@' in hostname:
                sub['backup'].error('wrong "hostname,/couchdb/data/folder"')

        hostname = shlex.quote(hostname)
        path = shlex.quote(path)
        archive = shlex.quote(args.archive)
        rsync_reuse_folder = shlex.quote(args.rsync_reuse_folder) \
            if args.rsync_reuse_folder else None

        await backup(hostname, path, archive, rsync_reuse_folder)
    elif args.action == 'load':
        await load(shlex.quote(args.archive))
    elif args.action == 'restore':
        creds = []
        hostnames = []
        ports = []
        paths = []
        names = []
        for couchdb in args.couchdbs:
            splitted = couchdb.split(',', 1)
            if len(splitted) != 2:
                sub['restore'].error(f'wrong {meta} {couchdb}')
            access, couchdb_internal = splitted
            cred, hostname_and_port = ['admin:password', access] \
                if len(access.split('@')) == 1 else access.split('@')
            if len(cred.split(':')) != 2:
                sub['restore'].error('wrong credential')
            hostname, port = ([hostname_and_port, '5984']
                              if len(hostname_and_port.split(':')) == 1
                              else hostname_and_port.split(':'))
            default_name = 'couchdb@' + (
                '127.0.0.1' if hostname == 'localhost' else hostname)
            path, name = ([couchdb_internal, default_name]
                          if len(couchdb_internal.split(',')) == 1
                          else couchdb_internal.split(','))
            if len(name.split('@')) != 2:
                sub['restore'].error(f'wrong nodename {name}')
            creds.append(shlex.quote(cred))
            hostnames.append(shlex.quote(hostname))
            ports.append(shlex.quote(port))
            paths.append(shlex.quote(path))
            names.append(shlex.quote(name))

        archive = shlex.quote(args.archive)
        # For couchdb_start and couchdb_stop we cannot escape with
        # `shlex.quote`, we have to trust the user.
        couchdb_start = args.couchdb_start
        couchdb_stop = args.couchdb_stop

        await restore(archive, creds[0], hostnames, paths, ports, names,
                      args.y, couchdb_start, couchdb_stop)

    print('Done!')


if __name__ == '__main__':
    asyncio.run(main())
