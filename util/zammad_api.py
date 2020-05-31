# Import modules
import json
import requests
from . import rest_api


class Tags:
    def __init__(self, target, token, tag=None):
        self.target = target
        self.token = token
        self.tag = tag

    def list(self):
        print(rest_api.req('list', self.target, self.token))