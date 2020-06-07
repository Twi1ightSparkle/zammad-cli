# Import modules
import argparse
from argparse import HelpFormatter
import json
import pydoc


# Global vars
version = '0.02 alfa'

# Functions
def validate_json(json_data):
    """Validate JSON

    Validate JSON data. Exit if error or return the JSON data if successful.

    Args:
        json_data: JSON data string
    
    Returns:
        JSON encoded data if successful.
    """

    try:
        return json.loads(json_data)
    except json.decoder.JSONDecodeError:
        print('Invalid JSON data')
        exit(1)


def pp_json(json_data, less=False):
    """Pretty print JSON less or stdout

    Args:
        json_data: Some JSON data
        less: use less instead of printing to stdout. Default False
    
    Returns:
        Nothing
    """

    if less:
        pydoc.pager(json.dumps(json_data, indent=4))
    else:
        print(json.dumps(json_data, indent=2))



# Classes
class CustomHelp(HelpFormatter):
    """Format --help"""

    def _format_action_invocation(self, action):
        if not action.option_strings:
            default = self._get_default_metavar_for_positional(action)
            metavar, = self._metavar_formatter(action, default)(1)
            return metavar

        else:
            parts = []

            # if the Optional doesn't take a value, format is:
            #    -s, --long
            if action.nargs == 0:
                parts.extend(action.option_strings)

            # if the Optional takes a value, format is:
            #    -s ARGS, --long ARGS
            else:
                default = self._get_default_metavar_for_optional(action)
                args_string = self._format_args(action, default)
                for option_string in action.option_strings:
                    parts.append(option_string)

                return '%s %s' % (', '.join(parts), args_string)

            return ', '.join(parts)

    def _get_default_metavar_for_optional(self, action):
        return action.dest.upper()