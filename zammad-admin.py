# Import modules
import argparse
import configparser
import os
from util import misc


if __name__ == '__main__':
    # Parse command line options
    parser = argparse.ArgumentParser(
        formatter_class=misc.CustomHelp,
        add_help=False,
        description='Work with and automate Zammad configuration using the Zammad API',
    )

    info = parser.add_argument_group(title='Program information')
    config = parser.add_argument_group(title='Program configuration options', description='One or more can be specified')    
    category_group = parser.add_argument_group(title='Categories', description='Categories to work on. Exactly one must be specified')
    category = category_group.add_mutually_exclusive_group(required=True)
    action_group = parser.add_argument_group(title='Actions', description='Action to perform. Exactly one must be specified')
    action = action_group.add_mutually_exclusive_group(required=True)
    
    info.add_argument('-h', '--help', default=argparse.SUPPRESS,                action='help',          help='Show this help message and exit')
    info.add_argument('-V', '--version', version='%(prog)s, v{}'.format(misc.version), action='version', help='Show program version')

    config.add_argument('-aw', '--api-key',     type=str,   metavar='KEY',      action='store',         help='API key with all permissions, including all admin')
    config.add_argument('-ar', '--api-read-key', type=str,  metavar='KEY',      action='store',         help='API key to read Zammad with all permissions, including all admin')
    config.add_argument('-c', '--config',       type=str,   metavar='PATH',     action='store',         help='/path/to/config.ini (. for same directory as %(prog)s)')
    config.add_argument('-fi', '--filter',      type=str,   metavar='STRING',   action='store',         help='Filter object. Used with -L')
    config.add_argument('-j', '--json',         type=str,   metavar='JSON',     action='store',         help='JSON data')
    config.add_argument('-J', '--json-file',    type=str,   metavar='PATH',     action='store',         help='JSON data file path')
    config.add_argument('-rt', '--read-target', type=str,   metavar='URL',      action='store',         help='Zammad URL to read from')
    config.add_argument('-wt', '--write-target', type=str,  metavar='URL',      action='store',         help='Zammad URL to work with')
    config.add_argument('-v', '--verbose',                                      action='count',         help='Show debug logging')

    category.add_argument('-a', '--all',                                        action='store_true',    help='Manage all categories. Cannot be used with -DGNU')
    category.add_argument('-co', '--collection',                                action='store_true',    help='Manage a collection. This currently mean -fgor')
    category.add_argument('-f', '--email-filter',                               action='store_true',    help='Manage email filters')
    category.add_argument('-s', '--email-signature',                            action='store_true',    help='Manage email signatures')
    category.add_argument('-g', '--group',                                      action='store_true',    help='Manage groups')
    category.add_argument('-k', '--knowledge-base',                             action='store_true',    help='Manage knowledge base. Not implemented. Planned for v2')
    category.add_argument('-m', '--macro',                                      action='store_true',    help='Manage macros')
    category.add_argument('-or', '--organization',                              action='store_true',    help='Manage organizations')
    category.add_argument('-o', '--overview',                                   action='store_true',    help='Manage overviews')
    category.add_argument('-r', '--role',                                       action='store_true',    help='Manage roles')
    category.add_argument('-ta', '--tag',                                       action='store_true',    help='Manage tags')
    category.add_argument('-ti', '--ticket',                                    action='store_true',    help='Manage tickets. Not implemented. Planned for v2')
    category.add_argument('-tr', '--trigger',                                   action='store_true',    help='Manage triggers')
    category.add_argument('-u', '--user',                                       action='store_true',    help='Manage users')

    action.add_argument('-C', '--clone',                                        action='store_true',    help='Clone one Zammad to another. Use with -R, -W and for example -A')
    action.add_argument('-D', '--delete',       type=int,   metavar='ID',       action='store',         help='Delete object')
    action.add_argument('-G', '--get',          type=int,   metavar='ID',       action='store',         help='Get an object')
    action.add_argument('-L', '--list',                                         action='store_true',    help='List all objects')
    action.add_argument('-N', '--new',                                          action='store_true',    help='New object. -j or -J must be specified')
    action.add_argument('-U', '--update',       type=int,   metavar='ID',       action='store',         help='Update object. -j or -J must be specified')

    args = parser.parse_args()


    # Check if option not yet implemented is used
    if args.filter or args.all or args.email_filter or args.email_signature or args.group or args.knowledge_base or args.macro or args.organization or \
        args.overview or args.role or args.ticket or args.trigger or args.user or args.clone or args.delete or args.get or args.new or args.update:
        print('''Following options not yet implemented:\n--filter\n--all\n--email-filter\n--email-signatures\n--group\n--knowledge-base\n--macro\n--organization
--overview\n--role\n--ticket\n--trigger\n--user\n--clone\n--delete\n--get\n--new\n--update''')
    
    # Check that --json(-file) is set if --new or --update
    if (args.new or args.update) and (not args.json and not args.json_file):
        print('--json or --json-file must be used with --new and --update')
        exit(1)
    
    # --filter can only be used with --list
    if args.filter and args.list:
        print('--filter can only be used with --list')
        exit(1)
    
    # Check that only --list is used with --all
    if args.all and (args.delete or args.get or args.new or args.update):
        print('--all cannot be used with --delete, --get, --new or --update')
        exit(1)
    
    # Check that target or api keys are not set if config file is specified
    if args.config and (args.api_key or args.api_read_key or args.read_target or args.write_target):
        print('--api-key, --api-read-key, --read-target or --write target cannot be used with --config')
        exit(1)
    
    # Check that --write-target and --api-key is set if no config is specified
    if not args.config and (not args.api_key and not args.write_target):
        print('When --config is not set, --api-key and --write-target must be specified')
        exit(1)
    
    # Check that not both --json and --json-file is specified
    if args.json and args.json_file:
        print('Only one of --json and --json-file must be set')
        exit(1)
    
    # Check that --read-target and --api-read-key is set if --clone is set
    if args.clone and (not args.read_target and not args.api_read_key):
        print('--read-target and --api-read-key must be used with --clone')
        exit(1)


    # Set paths and stuff

    work_dir = os.path.dirname(os.path.realpath(__file__)) # Get the path for the directory this python file is stored in
    
    if args.config == '.':
        config_file = os.path.join(work_dir, 'config.ini')
    elif args.config:
        config_file = args.config
    else:
        config_file = None


    # Validate supplied JSON data
    if args.json:
        json_data = misc.validate_json(args.json)

    # Load and Validate JSON data file
    if config_file:
        if os.path.isfile(config_file):
            f = open(config_file, 'r')
            temp_json = f.read()
            f.close()
            json_data = misc.validate_json(temp_json)
        else:
            print('JSON file not found')
            exit(1)
        
    # Check that config file exist
    if not args.api_key and not args.write_target:
        if not os.path.isfile(config_file):
            print('Config file not found')
            exit(1)
    
    # Try loading config file
    if config_file:
        try:
            config = configparser.ConfigParser()
            config.read(config_file)
            write_url =     config.get('Global',     'url')
            write_api_key = config.get('Global',     'api_key')
            read_url =      config.get('ReadZammad', 'url')
            read_api_key =  config.get('ReadZammad', 'api_key')
        except configparser.NoOptionError as err:
            print('Error loading config from file.\n' + str(err))
            exit(1)
    else:
        write_url = args.write_target
        write_api_key = args.api_key
        read_url = args.read_target
        read_api_key = args.api_read_key
