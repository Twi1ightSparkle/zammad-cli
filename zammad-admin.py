# Import modules
import configparser
import os
from util import rest_api
from util import zammad_api


if __name__ == "__main__":
    # Read config
    work_dir = os.path.dirname(os.path.realpath(__file__)) # Get the path for the directory this python file is stored in
    config = configparser.ConfigParser()
    config.read(os.path.join(work_dir, 'config.ini'))
    cg_url =        config.get('Global',     'url')
    cg_api_key =    config.get('Global',     'api_key')
    cr_url =        config.get('ReadZammad', 'url')
    cr_api_key =    config.get('ReadZammad', 'api_key')

    # print(rest_api.req('GET', f'{cg_url}:, cg_api_key))
    # print(rest_api.tags('list', cr_url, cr_api_key))
    
    print(zammad_api.Tags.list(cr_url, cr_api_key))
