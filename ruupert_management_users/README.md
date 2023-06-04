ruupert.management-users
========================

Ensures that local management users are added with their public keys and ensures other usesrs are not present. Also sets root password.

At the moment just for Ubuntu 18.04, but I do not see why this would not work of most linux boxes.

Requirements
------------

A pile of salt.

Role Variables
--------------

    users: [{username:"",public_key:""},...]
    remove_users: ["username", ...]
    root_password_hash: "<password hash>"

Dependencies
------------

    ruupert.reusable-handlers

Example
-------

In your role meta/main.yml:

    dependencies:
      - { role: ruupert.reusable-handlers }

Variables for adding management users and ensuring other management users are not present anymore:

    users: [
      {
        username: "user1",
        public_key: "<user1 ssh public key string>"
      },{
        username: "user2",
        public_key: "<user2 ssh public key string>\n<user2 ssh public key2 string>"
      }
    ]

    remove_users: [
      "user5",
      "user6"
    ]



