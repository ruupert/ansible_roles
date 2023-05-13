ruupert_iptables
========================

Configures ans maintains IPtables rules. Work in progress.... 

Requirements
------------

A pile of salt

Role Variables
--------------

None at the moment

Dependencies
------------

    ruupert_reusable_handlers

Example
-------

Have your default mgmt ip set in group_vars/all.yml 

```
mgmt_iptables:
  - port: 22
    src: "1.2.3.4/32"
    proto: tcp

host_vars_iptables:
```

Override default mgmt ip in host_vars/<host>.yml

And then per host allows in similarly in host_vars/<host>.yml:
```
host_vars_iptables:
  allow:
    tcp:
      - port: 22
        src: "1.2.3.4"
      - port: 80
        src: "2.3.4.5"
```
