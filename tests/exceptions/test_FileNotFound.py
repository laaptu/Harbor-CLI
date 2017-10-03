'''
Test for FileNotFoundException
'''
from lib.exceptions.FileNotFound import FileNotFoundException

def test_with_second_param():
    ''' should show custom message if the second parameter is given. '''
    try:
        raise FileNotFoundException('package.json', 'This is a custom message.')
    except FileNotFoundException as error:
        assert error.message == 'This is a custom message.'

def test_without_second_param():
    ''' should show default message formatted with path, when second param is not given. '''
    try:
        raise FileNotFoundException('package.json')
    except FileNotFoundException as error:
        assert error.message == 'File {0} does not exist.'.format('package.json')
