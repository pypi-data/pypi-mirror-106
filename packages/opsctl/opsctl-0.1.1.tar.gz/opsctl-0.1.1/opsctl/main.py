#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: v.stone@163.com


from getopt import getopt, GetoptError
import sys
import os
from opsctl.yamlrender import YamlRender


def print_help_tool():
    print('\n'.join([
        '\nopsctl',
        '\t'.join([
            '  yaml   ',
            'Render templates to YAML'
        ]),
        '\t'.join([
            '  version',
            'Show opsctl version'
        ]),
    ]))
    exit(1)


def print_help_cmd_yaml():
    print('\n'.join([
        '\nopsctl yaml',
        '\t'.join([
            '  --config',
            'Key-Value config file path, file type is YAML'
        ]),
        '\t'.join([
            '  --template',
            'Template root path'
        ]),
        '\t'.join([
            '  --render',
            'Render output path'
        ]),
    ]))
    exit(1)


def check_cmd_yaml_opts(cmd_yaml_opts):
    """
    config, template, render are required
    :param cmd_yaml_opts:
    :return:
    """
    _items = dict()
    for k, v in cmd_yaml_opts:
        _items['OPSCTL_%s' % k.replace('--', '').upper()] = v
    if len(_items) == 0:
        print_help_cmd_yaml()
    if not _items.get('OPSCTL_CONFIG'):
        print('--config is required')
        print_help_cmd_yaml()
    if not _items.get('OPSCTL_TEMPLATE'):
        print('--template is required')
        print_help_cmd_yaml()
    if not _items.get('OPSCTL_RENDER'):
        print('--render is required')
        print_help_cmd_yaml()
    if not os.path.isfile(_items['OPSCTL_CONFIG']):
        print('%s is not a valid file' % _items['OPSCTL_CONFIG'])
        print_help_cmd_yaml()
    if not os.path.isdir(_items['OPSCTL_TEMPLATE']):
        print('%s is not a valid dir' % _items['OPSCTL_TEMPLATE'])
        print_help_cmd_yaml()
    return _items


def main():
    try:
        tool_cmd = sys.argv[1]
    except IndexError:
        tool_cmd = ''
        print_help_tool()
    cmd_args = sys.argv[2:]
    cmd_args_items = dict()
    if tool_cmd == 'yaml':
        try:
            opts, args = getopt(
                args=cmd_args,
                shortopts='',
                longopts=[
                    'config=',
                    'template=',
                    'render=',
                ]
            )
            cmd_args_items = check_cmd_yaml_opts(opts)
        except GetoptError:
            print_help_cmd_yaml()
        yaml_render = YamlRender(
            config_file=cmd_args_items['OPSCTL_CONFIG'],
            template_dir=cmd_args_items['OPSCTL_TEMPLATE'],
            render_dir=cmd_args_items['OPSCTL_RENDER']
        )
        yaml_render.render_all()
    elif tool_cmd == 'version':
        print('opsctl v0.1.1')
    else:
        print_help_tool()


if __name__ == '__main__':
    main()
