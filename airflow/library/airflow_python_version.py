#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import platform
DOCUMENTATION = r'''
---
module: airflow_python_version

short_description: return python major.minor version

version_added: "1.0.0"

description: return python major.minor version 

author:
    - Raul Becker (@ruupert)
'''

from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = dict(
    )
    result = dict(
        airflow_python_version=None
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )
    if module.check_mode:
        module.exit_json(**result)
    
    try:
        result['ansible_facts'] = { 'airflow_python_version': f"{platform.sys.version_info.major}.{platform.sys.version_info.minor}"}
        ok = True
    except:
        result['ansible_facts'] = None
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