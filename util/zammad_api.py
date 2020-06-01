# Import modules
import json
import requests
from . import rest_api


# Classes

class ZammadApi:
    """Work with the Zammad API"""

    api_endpoint = ''
    
    def __init__(self, target, api_key, json_data=None):
        self.target = f'{target}/api/v1/'
        self.api_key = api_key
        self.json_data = json_data

    # TODO These functions should all be children of a master function. Ref the returnign a function I watched Saturday

    def clone(self):
        pass

    def delete(self):
        """List data from Zammad"""
        result = rest_api.req('DELETE', self.api_endpoint, self.api_key)

        if 'error' in result:
            print(f'API error from function \n{result.get('error')[0]}\nError message: {result.get('error')[1]}')
            exit(1)
        else:
            return result
    
    def get(self):
        pass
    
    def list_all(self):
        pass
    
    def new(self):
        pass
    
    def update(self):
        pass




class Tag(ZammadApi):

    api_endpoint = 'tag_list'

    def __init__(self, target, api_key, json_data):
        super().__init__(target, api_key, json_data)
        self.api_endpoint = self.target + self.api_endpoint
    
