# Import modules
import json
import requests
from . import rest_api
from . import misc

# Classes

class ZammadApi:
    """Work with the Zammad API"""

    api_endpoint = ''
    description = ''
    
    def __init__(self, target, api_key, filter_string=None, obj_id=None, json_data=None):
        self.target = f'{target}/api/v1/'
        self.api_key = api_key
        self.json_data = json.dumps(json_data)
        self.obj_id = str(obj_id)
        self.api_endpoint = self.target + self.api_endpoint
        if filter_string:
            self.filter_string = str(filter_string)
        else:
            self.filter_string = None
        
        # if self.obj_id:
        #     self.api_endpoint = self.target + self.api_endpoint + '/{' + str(self.obj_id) + '}'
        # else:
        #     self.api_endpoint = self.target + self.api_endpoint
    
    # Disallow direct instantiation of this parent class
    # TODO This isn't working for some reason....
    # def __new__(cls, *args, **kwargs):
    #     print(cls)
    #     if cls is ZammadApi:
    #         raise TypeError("The parent class ZammadApi can not be directly instantiated")
    #     return object.__new__(cls, *args, **kwargs)

    def action(self, method):
        """Call Zammad rest api

        Args:
            method: What method to use with requests. One of GET, PUT, POST or DELETE
        
        Returns:
            Whatever is returned from the rest_api function. Being data or an error message
        """

        if self.json_data:
            self.result = rest_api.req(method, self.api_endpoint, self.api_key, self.json_data)
        else:
            self.result = rest_api.req(method, self.api_endpoint, self.api_key)
        
        if 'error' in self.result:
            err_func = self.result.get('error')[0]
            err_msg = self.result.get('error')[1]
            print(f'API error from function {err_func}\nError message: {err_msg}')
            exit(1)
        else:
            return self.result


    # --clone
    def clone(self):
        # TODO clone will probably not be handled in the class?
        pass
    
    # --list
    def list_obj(self):
        self.results = self.objs = self.action('GET')
        if self.filter_string:
            self.filter_hits = []
            for self.result in self.results:
                for _, self.value in self.result.items():
                    if self.filter_string.lower() in str(self.value).lower():
                        self.filter_hits.append(self.result)
                        break
            if len(self.filter_hits) > 0:
                return self.filter_hits
            else:
                return {'error': f'No {self.description}s containing {self.filter_string} was found'}

        else:
            return self.results

    # --get
    def get(self):
        self.objs = self.action('GET')
        for self.obj in self.objs:
            if self.obj.get('obj_id') == self.obj_id:
                return self.obj
        return {'error': f'{self.description} with obj_id {self.obj_id} not found'}
    
    # --new
    def new(self):
        return self.action('POST')
    
    # --update
    def update(self):
        # Print old and new data
        print('You are about to change\n')
        misc.pp_json(self.get())
        print('\nto\n')
        misc.pp_json(self.json_data)

        # Ask for confirmation
        self.confirmation = input('\nDo you want to continue? [y/N] ')
        if self.confirmation.lower() == 'y':
            return self.action('PUT')

    # --delete
    def delete(self):
        # Print old and new data
        print('You are about to delete:\n')
        misc.pp_json(self.json_data)

        # Ask for confirmation
        self.confirmation = input('\nDo you want to continue? [y/N] ')
        if self.confirmation.lower() == 'y':
            return self.action('DELETE')


class Tag(ZammadApi):

    api_endpoint = 'tag_list'
    description = 'tag'

    def __init__(self, target, api_key, filter_string=None, obj_id=None, json_data=None):
        super().__init__(target, api_key, filter_string, obj_id, json_data)

    def list_obj(self):
        if self.filter_string:
            self.api_endpoint = self.api_endpoint.replace('tag_list', 'tag_search') + '?term=' + self.filter_string

        self.results = self.action('GET')

        if len(self.results) > 0:
            return self.results
        else:
            return {'error': f'No {self.description}s containing {self.filter_string} was found'}


class EmailFilter(ZammadApi):

    api_endpoint = 'postmaster_filters'
    description = 'email filter_string'

    def __init__(self, target, api_key, filter_string=None, obj_id=None, json_data=None):
        super().__init__(target, api_key, filter_string, obj_id, json_data)


class EmailSignature(ZammadApi):

    api_endpoint = 'signatures'
    description = 'email signature'

    def __init__(self, target, api_key, filter_string=None, obj_id=None, json_data=None):
        super().__init__(target, api_key, filter_string, obj_id, json_data)


class Group(ZammadApi):

    api_endpoint = 'groups'
    description = 'group'

    def __init__(self, target, api_key, filter_string=None, obj_id=None, json_data=None):
        super().__init__(target, api_key, filter_string, obj_id, json_data)


class KnowledgeBase(ZammadApi):

    api_endpoint = ''
    description = 'knowledge base'

    def __init__(self, target, api_key, filter_string=None, obj_id=None, json_data=None):
        super().__init__(target, api_key, filter_string, obj_id, json_data)


class Macro(ZammadApi):

    api_endpoint = 'macros'
    description = 'macro'

    def __init__(self, target, api_key, filter_string=None, obj_id=None, json_data=None):
        super().__init__(target, api_key, filter_string, obj_id, json_data)

    def get(self):
        self.api_endpoint = self.api_endpoint + '/#' + self.obj_id
        print(self.api_endpoint)
        return self.action('GET')

        # self.objs = self.action('GET')
        # for self.obj in self.objs:
        #     if self.obj.get('obj_id') == self.obj_id:
        #         return self.obj
        # return {'error': f'{self.description} with obj_id {self.obj_id} not found'}


class Organization(ZammadApi):

    api_endpoint = 'organizations'
    description = 'organization'

    def __init__(self, target, api_key, filter_string=None, obj_id=None, json_data=None):
        super().__init__(target, api_key, filter_string, obj_id, json_data)

    def list_obj(self):
        if self.filter_string:
            self.api_endpoint = self.api_endpoint + '/search?query=' + self.filter_string + '&limit=999999999999999'

        self.results = self.action('GET')

        if len(self.results) > 0:
            return self.results
        else:
            return {'error': f'No {self.description}s containing {self.filter_string} was found'}


class Overview(ZammadApi):

    api_endpoint = 'overviews'
    description = 'overview'

    def __init__(self, target, api_key, filter_string=None, obj_id=None, json_data=None):
        super().__init__(target, api_key, filter_string, obj_id, json_data)


class Role(ZammadApi):

    api_endpoint = 'roles'
    description = 'role'

    def __init__(self, target, api_key, filter_string=None, obj_id=None, json_data=None):
        super().__init__(target, api_key, filter_string, obj_id, json_data)


class Ticket(ZammadApi):

    api_endpoint = ''
    description = 'ticket'

    def __init__(self, target, api_key, filter_string=None, obj_id=None, json_data=None):
        super().__init__(target, api_key, filter_string, obj_id, json_data)


class Trigger(ZammadApi):

    api_endpoint = 'triggers'
    description = 'trigger'

    def __init__(self, target, api_key, filter_string=None, obj_id=None, json_data=None):
        super().__init__(target, api_key, filter_string, obj_id, json_data)


class User(ZammadApi):

    api_endpoint = 'users'
    description = 'user'

    def __init__(self, target, api_key, filter_string=None, obj_id=None, json_data=None):
        super().__init__(target, api_key, filter_string, obj_id, json_data)

    def list_obj(self):
        if self.filter_string:
            self.api_endpoint = self.api_endpoint + '/search?query=' + self.filter_string
            self.results = self.action('GET')
        else:
            self.api_endpoint_static = self.api_endpoint
            self.pagination = 0
            self.res_counter = 1
            self.results = []
            while self.res_counter > 0:
                self.pagination += 1
                self.api_endpoint = self.api_endpoint_static + '?page=' + str(self.pagination) + '&per_page=500'
                self.temp = self.action('GET')
                self.res_counter = len(self.temp)
                self.results += self.temp

        if len(self.results) > 0:
            return self.results
        else:
            return {'error': f'No {self.description}s containing {self.filter_string} was found'}


class Collection(ZammadApi):

    api_endpoint = ''
    description = 'collection'

    def __init__(self, target, api_key, filter_string=None, obj_id=None, json_data=None):
        super().__init__(target, api_key, filter_string, obj_id, json_data)
