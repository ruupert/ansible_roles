ruupert_rtorrent
================

Installs rtorrent, configures it and runs it in tmux as a systemd service

Requirements
------------

A pile of salt

Role Variables
--------------

Only some sensible defaults for later. 

Dependencies
------------

    ruupert_reusable_handlers

Example
-------

For the host the role is applied on define its vars. E.g.
```
rtorrent_directory: "/home/user/rtorrent"
rtorrent_user: "user"
rtorrent_home: "/home/user"
rtorrent_port_range: "45123-45123" (optional, default:"45000-50000")
rtorrent_dht: "enable"   (optional, default: "disable")
```
