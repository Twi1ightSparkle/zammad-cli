# Import modules
import argparse
from argparse import HelpFormatter
import json


# Global vars
version = '0.1 alfa. Released May 31, 2020. Copyright Twilight Sparkle 2020'

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