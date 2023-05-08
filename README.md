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

Have your hostvars set

```
host_vars_iptables:
  allow:
    tcp:
      - port: 22
        src: "1.2.3.4"
        rulenum: 1
      - port: 80
        src: "2.3.4.5"
        rulenum: 2
```

I dare you to just run against a set of inventory hosts.

Non working defaults for now