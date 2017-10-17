'''
Authentication module.
'''

import sys

from lib.logger import logger
from lib.services.firebase_service import Firebase

def login(email=None, password=None):
    ''' Login using email/password. '''
    try:
        logger().info('Logging in..\n')
        Firebase().login_with_email(email, password)
        logger().info('Login succesful.\n')
    except Exception:  #pylint: disable=broad-except
        logger().error('Could not login. Check your connection and credentials.')
        sys.exit(1)

def get_saved_credentials():
    ''' Get saved preferences. '''
    pass
