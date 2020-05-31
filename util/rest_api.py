# Import modules
import json
import requests


# Functions

def req(operation, target, token, data=None):
    """Read or write to rest API

    Args:
        operation: Must be one of GET, PUT, POST, DELETE
        target: Link and port to connect to
        token: API token
        data: Optional, default Null. What data to PUT
    
    Returns:
        Decoded JSON response or requested data
    """

    # Check operation valid
    if operation not in ['GET', 'PUT', 'POST', 'DELETE']:
        e = '{"error": ["req", "Invalid operation %s"]}' % (operation,)
        return json.loads(e)

    # Build header
    # headers = {'User-Agent': ua.random}
    headers = '{"Authorization": "Token token=%s"}' % (token,)

    print(headers)
    # Try connecting
    # try:
    response = requests.get(target, headers=headers)
    # except Exception as error:
        # e = '{"error": ["req", "Error connecting to %s. Error message: %s"]}' % (target, error,)
        # return json.loads(e)

    # If not 200
    if not response.status_code == 200:
        e = '{"error": ["req", "Error connecting to %s. Status code %s"]}' % (target, response.status_code,)
        return json.loads(e)
    
    # Try and decode json
    try:
        return response.json()

    # If converting to json fails
    except json.decoder.JSONDecodeError as error:
        e = '{"error": ["req", "Error decoding JSON %s"]}' % (error,)
        return json.loads(e)


class Tags:
    def list(self):
        return 'aaa'


def tags(operation, target, token, tag=None):
    """Operate on tags

    Args:
        operation: Must be one of add, remove, list, rename
        target: Link and port to connect to
        token: API token
        tag. Optional, default Null. Use Null to get all
    
    Returns:
        Decoded JSON response or requested data
    """

    # Check operation valid
    if operation not in ['add', 'remove', 'list', 'rename']:
        e = '{"error": ["tags", "Invalid operation %s"]}' % (operation,)
        return json.loads(e)
    
    if operation == 'list':
        target = f'{target}/api/v1/tag_list'
        return req('GET', target, token)
