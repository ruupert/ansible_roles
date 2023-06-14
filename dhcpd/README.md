dhcpd
=====

Installs and configures isc-dhcp-server

Requirements
------------

A pile of salt

Host Variables
--------------

e.g.

    dhcpd_default_lease: "600"
    dhcpd_max_lease: "7200"
    dhcpd_subnets:
      - subnet: "1.2.3.0"
        netmask: "255.255.255.0"
        gateway: "1.2.3.1"
        broadcast: "1.2.3.255"
        nameserver: "1.2.3.2"
        start: "1.2.3.3"
        stop: "1.2.3.254"
    dhcpd_no_service:
      - subnet: "2.4.5.0"
        netmask: "255.255.255.0"
    dhcpd_fixed_addresses:
      - name: "hostname"
        hw: "aa:bb:cc:dd:ee:ff"
        ip: "1.2.3.4"
    dhcpd_listen_interfaces: "eth0"


Dependencies
------------

    ruupert_reusable_handlers
