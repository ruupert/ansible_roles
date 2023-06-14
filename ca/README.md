ca
==

Creates a private certificate authority

Requirements
------------

A pile of salt

Host Variables
--------------

e.g.

    secret_ca_passphrase: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          .................

Dependencies
------------

    ruupert_reusable_handlers
