'''
Test for DirNotFoundException
'''
from lib.exceptions.DirNotFound import DirNotFoundException

def test_with_second_param():
    ''' should show custom message if the second parameter is given.'''
    try:
        raise DirNotFoundException('nonexistentdirectory', 'This is a custom message.')
    except DirNotFoundException as error:
        assert error.message == 'This is a custom message.'

def test_without_second_param():
    ''' should show default message formatted with path, when second param is not given. '''
    try:
        raise DirNotFoundException('nonexistentdirectory')
    except DirNotFoundException as error:
        assert error.message == 'Directory {0} does not exist.'.format('nonexistentdirectory')
