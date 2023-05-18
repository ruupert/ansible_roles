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
rtorrent:
  user: "rtorrent"
  home: "/opt/rtorrent"
  dir: "/opt/rtorrent/rt"
  port_range: "45000-50000"
  dht: "enable/disable"   
```
