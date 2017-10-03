'''
Test for UserNotFoundException
'''
from lib.exceptions.UserNotFound import UserNotFoundException

def test_with_message_param():
    ''' should show custom message if the message parameter is given. '''
    message = 'User was not found.'
    try:
        raise UserNotFoundException(message)
    except UserNotFoundException as error:
        assert error.message == message

def test_without_message_param():
    ''' should show default message formatted with path, when second param is not given. '''
    try:
        raise UserNotFoundException()
    except UserNotFoundException as error:
        assert error.message == 'User not found.'
