import sys

from lib.services.stdio_service import get_login_credentials
from lib.services.firebase_service import Firebase

def delegate():
    ''' deploy delegate for the CLI hook.'''
    email, password = get_login_credentials()

    firebase = Firebase()

    try:
        firebase.login_with_email(email, password)
    except Exception as e:
        print('\nAn error occurred. Please check your connection, credentials and try again.')
        sys.exit(1)
