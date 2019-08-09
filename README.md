Role Name
=========
[![Build Status](https://travis-ci.org/apkawa/ansible-role-.svg?branch=master)](https://travis-ci.org/apkawa/ansible-role-)

[![Ansible role](https://img.shields.io/ansible/role/%replace%.svg)](https://galaxy.ansible.com/apkawa/%replace%)
[![Ansible role downloads](https://img.shields.io/ansible/role/d/%replace%.svg)](https://galaxy.ansible.com/apkawa/%replace%)
[![Ansible role quality](https://img.shields.io/ansible/quality/%replace%.svg)](https://galaxy.ansible.com/apkawa/%replace%)

A brief description of the role goes here.

Requirements
------------

None

Role Variables
--------------

Available variables are listed below, along with default values (see `defaults/main.yml`):
```yaml
```


Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - role: ansible-role-

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