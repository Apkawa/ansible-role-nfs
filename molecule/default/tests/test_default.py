# flake8: noqa
import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_exports(host):
    f = host.file('/etc/exports')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

    assert f.content_string == (
        '/exports/home/   *(rw,sync)\n'
        '/exports/ro/   127.0.0.1(ro,sync)  10.0.1.0/24(ro,sync)  10.0.0.1(rw,sync)  10.0.0.2(rw,sync,nohide)\n'
    )


def test_nfs_server(host):
    cmd = host.run('showmount -e 127.0.0.1')
    assert cmd.rc == 0
    assert cmd.stdout.strip() == (
        """
Export list for 127.0.0.1:
/exports/home *
/exports/ro   10.0.1.0/24,10.0.0.2,10.0.0.1,127.0.0.1
""".strip()
    )


def test_nfs_server_mount(host):
    cmd = host.run('echo 123 > /exports/old_ro/test')
    assert cmd.rc == 0
    f2 = host.file('/exports/ro/test')
    assert f2.exists
    assert f2.content_string == '123\n'


def test_nfs_client_share(host):
    cmd = host.run('echo 123 > /exports/old_ro/test')
    assert cmd.rc == 0
    f2 = host.file('/mnt/nfs_ro/test')
    assert f2.exists
    assert f2.content_string == '123\n'


def test_nfs_client_share_permission(host):
    cmd = host.run('touch /mnt/nfs_ro/test_ro')
    assert cmd.rc == 1
    assert 'Read-only file system' in cmd.stderr

    # Todo fix touch: cannot touch ‘/mnt/nfs_home/test_rw’: Permission denied
    # cmd = host.run('touch /mnt/nfs_home/test_rw')
    # assert cmd.rc == 0
    # assert host.file('/mnt/nfs_home/test_rw').exists
