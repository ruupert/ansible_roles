ruupert_reusable_handlers
=========================

Provides reusable handlers for sending error messages to slack and teams. 

Requirements
------------

A pile of salt.

Role Variables
--------------

    reusable_handlers_logdir: "<path to log directory>"
    disable_teams_handlers: true
    disable_slack_handlers: true
    slack_token: ""
    teams_webhook: ""


Dependencies
------------

    community.general.slack

Example usage in a role:
----------------

Set dependency in your role (meta/main.yml) as follows:

    dependencies:
      - { role: ruupert_reusable_handlers }

In your role tasks do a block-rescue where in your rescue in case of failure:

    notify: 
        - send failed message 

