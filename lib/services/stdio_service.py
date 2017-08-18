import getpass

from lib.utils.validators import is_valid_email

def get_login_credentials():
    while True:
        email = input('Enter your email address: ')
        if is_valid_email(email):
            break
        print('You entered an invalid email address.')

    password = getpass.getpass()

    return (email, password)

