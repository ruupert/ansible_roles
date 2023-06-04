ruupert_cis
===========

An ansible role for applying partially CIS recommended hardenings for Ubuntu 18.04 (bionic) and Debian 11 (bullseye)
Basing on the Ubuntu 18.04 and Debian 11 CIS PDFs.

Requirements
------------

A pile of salt.

Role Variables
--------------

    enable_aide: <BOOL>

Dependencies
------------

    ruupert_reusable_handlers

Example
-------

Just run against a set of inventory hosts.
