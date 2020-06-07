# Import modules
import json
import requests


# Functions

def req(method, target, token, data=None):
    '''Read or write to rest API

    Args:
        method: Must be one of GET, PUT, POST, DELETE
        target: Link and port to connect to
        token: API token
        data: Optional, default Null. What data to PUT
    
    Returns:
        Decoded JSON data or error in JSON format
    '''

    # Check method valid
    if method not in ['GET', 'PUT', 'POST', 'DELETE']:
        return {'error': ['rest_api.req', f'Invalid method {method}']}
    
    # Check that data supplied with PUT and POST
    if (method == 'PUT' or method == 'POST') and not data:
        return {'error': ['rest_api.req', f'data must be supplied when {method} is used']}

    # Build header and data
    if data:
        headers = {'Authorization': f'Token token={token}', 'Content-Type': 'application/json'}
        try:
            data = json.loads(data)
        except json.decoder.JSONDecodeError:
            return {'error': ['rest_api.req', 'Supplied data is not valid JSON']}
    else:
        headers = {'Authorization': f'Token token={token}'}

    # Try connecting
    try:
        response = requests.request(method=method, url=target, headers=headers, data=data)

    except Exception as error:
        return {'error': ['rest_api.req', f'Error connecting to {target}. Error message: {error}']}

    # If not 200 or 201
    if not response.status_code == 200 and not response.status_code == 201:
        return {'error': ['rest_api.req', f'Error connecting to {target}. Status code {response.status_code}']}
    
    # Try and decode json
    try:
        return response.json()

    # If converting to json fails
    except json.decoder.JSONDecodeError as error:
        return {'error': ['rest_api.req', f'Error decoding JSON {error}']}
