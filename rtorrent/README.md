rtorrent
========

Installs rtorrent, configures it and runs it in tmux as a systemd service, and runs lighthttpd for rpccontrol for rtorrent_exporter

Requirements
------------

A pile of salt

Role Variables
--------------

Defaults:
    rtorrent_user: "rtorrent"
    rtorrent_home: "/opt/rtorrent"
    rtorrent_dir: "/opt/rtorrent/rt"
    rtorrent_port_range: "45000-50000"
    rtorrent_dht: "disable"
    rtorrent_dl_rate_kb: 8000
    rtorrent_ul_rate_kb: 1500
    rtorrent_scgi_port: 16999

Optional:
    rtorrent_webhook_url: <webhook url to send completion notification>
    rtorrent_downloads_url: <public url for downloads path>

Dependencies
------------

    handlers
