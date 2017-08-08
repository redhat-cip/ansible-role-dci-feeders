# ansible-role-dci-feeders

An Ansible role that deploys the necessary playbook for a host to act as a DCI feeder


## Pre-requisites

This role heavily relies on [python-dciclient](https://github.com/redhat-cip/python-dciclient) and [dci-ansible](https://github.com/redhat-cip/dci-ansible).
If those are not installed, they should be installed before using this role.


## Role Variables


The variables of this role are :

  * `components`: A list of components to check if a new version is available.


### Example

```
---
components:
  - name: RDO-Pike
    topic: RDO-Pike
    type: snapshot_rdo
    component_types:
      -  snapshot_rdo
    url: http://trunk.rdoproject.org/centos7/current-passed-ci/delorean.repo

  - name: RDO-Ocata
    topic: RDO-Ocata
    type: snapshot_rdo
    component_types:
      -  snapshot_rdo
    url: http://trunk.rdoproject.org/centos7-ocata/current-passed-ci/delorean.repo

  - name: RDO-Newton
    topic: RDO-Newton
    type: snapshot_rdo
    component_types:
      -  snapshot_rdo
    url: http://trunk.rdoproject.org/centos7-newton/current-passed-ci/delorean.repo
```

Will ensure the latest RDO snapshots are feeded into the speficied DCI instance.


## Example playbook

Provisionning a host to act as a DCI feeder is as simple as :

```
- hosts: feeder
  roles:
    - { role: redhat-cip.dci-feeders }
```

Or if one relies on a requirement.txt kind of mechanism:

```
- hosts: feeder
  roles:
    - dci-feeders
```


## License

Apache 2.0

## Author Information

Distributed-CI Team  <distributed-ci@redhat.com>
