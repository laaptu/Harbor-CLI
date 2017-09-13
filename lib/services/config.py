import os

from lib.constants.paths import PATHS
from lib.utils.json_parser import json_parse
from lib.exceptions.FileNotFound import FileNotFoundException

def get():
    ''' Gets the config file details. '''
    if not exists():
        raise FileNotFoundException(
            PATHS['CONFIG_PATH'],
            'Configuration file not found.'
        )
    return json_parse(PATHS['CONFIG_PATH'])


def exists():
    ''' Returns a bool indicating whther the config file exists. '''
    return os.path.isfile(PATHS['CONFIG_PATH'])


def is_hipchat_configured():
    '''
    Returns true if config object has a hipchat property
    '''
    if not exists():
        return False
    options = get()
    if 'hipchat' not in options:
        return False
    return True
