'''
The config module is responsible for parsing a json file
in the root of the project directory.
'''

import os
import json
import pytest

from lib.services.config import get, exists
from lib.exceptions.FileNotFound import FileNotFoundException

def test_get_v0():
    ''' Should return the json for any path when it exists '''
    testobj = {
        'name': 'HarborCLI'
    }
    with open('random.json', 'w') as jsonfile:
        json.dump(testobj, jsonfile)

    data = get('random.json')
    assert data == testobj
    os.remove('random.json')

def test_get_v1():
    ''' Should throw when the config path does not exist '''
    with pytest.raises(FileNotFoundException):
        get('random.json')

def test_exists_when_config_exists():
    ''' Should return true if config file exists. '''
    if os.path.isfile('harborConfig.json'):
        assert exists() is True

    if not os.path.isfile('harborConfig.json'):
        with open('harborConfig.json', 'w'):
            assert exists() is True
            os.remove('harborConfig.json')

def test_exists_v0():
    ''' Should return false if file does not exist. '''
    assert exists('randomfile.json') is False
