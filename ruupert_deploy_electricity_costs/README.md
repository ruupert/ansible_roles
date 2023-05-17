ruupert_deploy_electricity_costs
================================

Deploys https://github.com/ruupert/electricity_costs onto a server.

- creates a user
- installs dependency packages
- git clone / force pull the sources
- initializes a python virtualenv in users home dir and installs the requirements.txt packages into it
- creates a cron schedule to run daily

ToDo: modify ruupert/electricity_costs to accept config file alternatively -> add task here to create the config file and modify the cron definition.

Requirements
------------

A pile of salt

Role Variables
--------------

in progress... 

Dependencies
------------

    ruupert.reusable-handlers

Example
-------

later
