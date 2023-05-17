ruupert.cis
===========

An ansible role for applying partially CIS recommended hardenings. Basing on the Ubuntu 18.04 PDF. 

Requirements
------------

A pile of salt.

Role Variables
--------------

    enable_aide: <BOOL>

Dependencies
------------

    ruupert.reusable-handlers

Example
-------

In your role meta/main.yml:

    dependencies:
      - { role: ruupert.reusable-handlers }

