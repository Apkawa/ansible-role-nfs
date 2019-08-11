Ansible role: nfs
=================
[![Build Status](https://travis-ci.org/apkawa/ansible-role-nfs.svg?branch=master)](https://travis-ci.org/apkawa/ansible-role-nfs)

[![Ansible role](https://img.shields.io/ansible/role/%replace%.svg)](https://galaxy.ansible.com/apkawa/nfs)
[![Ansible role downloads](https://img.shields.io/ansible/role/d/%replace%.svg)](https://galaxy.ansible.com/apkawa/nfs)
[![Ansible role quality](https://img.shields.io/ansible/quality/%replace%.svg)](https://galaxy.ansible.com/apkawa/nfs)

Ansible role for NFS client and/or NFS server

Requirements
------------

None

Role Variables
--------------

Available variables are listed below, along with default values (see `defaults/main.yml`):
```yaml

nfs_client: yes

nfs_client_mounts:
  - src: example.com:/export/
    mount_point: /mnt/example_nfs/
    # optional
    opts: rw,async
    deleted: false

# NFS server. disabled by default
nfs_server: no

nfs_server_shares:
  - path: /path/to/export
    # optional
    mount_from: /real_path/what/you/hide
    # default *
    allow:
      - 127.0.0.1
      - ip: 10.0.0.2
        # override for ip
        options:
          - ro
          - sync
      - ip: 10.0.0.4
        options: (rw,sync)
    # default
    options: (rw,sync)
    delete: no
```


Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - role: apkawa.nfs
```

License
-------

MIT 

Author Information
------------------

Apkawa 


Contributing
------------

1. [Install docker](https://docs.docker.com/install/linux/docker-ce/debian/)
2. [Install pipenv](https://docs.pipenv.org/en/latest/install/#installing-pipenv)
3. Initialize pipenv:
    ```
    pipenv install --dev
    ```
4. Run tests
    ``` 
    pipenv run -- tox -e centos7
    ```