ruupert_ansible_bootstrap
=========================

A slightly naive role for creating the ansible user for the standard cloud image based Ubuntu and Centos servers.

Does not run the inventory population and thus does not use the ansible reported OS version.

Requirements
------------

A pile of salt.

Role Variables
--------------

    ansible_public_key: "<SSH id_rsa.pub string>"

Dependencies
------------

    ruupert_reusable_handlers

Example
-------

In your role meta/main.yml:

    dependencies:
      - { role: ruupert_reusable_handlers }

