#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import subprocess
import json
DOCUMENTATION = r'''
---
module: airflow_db_migrate

short_description: return paused jobs

version_added: "1.0.0"

description: Returns job list yaml 

author:
    - Raul Becker (@ruupert)
'''

from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = dict(
        airflow_bin_path=dict(type='str', required=True),
    )
    result = dict(
        airflow_db_migrate=None
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )
    if module.check_mode:
        module.exit_json(**result)
    
    if module.params['airflow_bin_path']:
        output = subprocess.run(args=f"{module.params['airflow_bin_path']} db migrate", shell=True, check=True, capture_output=True, encoding="utf-8")
        result['ansible_info'] = output.returncode
        ok = True
    else:
        result['ansible_info'] = 1
        ok = False

    if (ok):
        res = dict(changed=False, ansible_facts=result)
        module.exit_json(**res)
    else:
        module.fail_json(msg="Something went wrong")


def main():
    run_module()


if __name__ == '__main__':
    main()