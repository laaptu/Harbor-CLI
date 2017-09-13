'''
Helpers for standard I/O work.
'''
import sys
import click
import getpass

from lib.utils import git
from lib.utils.validators import is_valid_email

RELEASE_LOG_TEXT = '''
# Please enter a change log for this release. Everything below this line is ignored, and an
# empty message aborts the release.

# On branch {0}
'''

def get_login_credentials():
    ''' Get login creds from user. Also includes some validation. '''
    while True:
        email = input('Enter your email address: ')
        if is_valid_email(email):
            break
        print('You entered an invalid email address.')

    password = getpass.getpass()
    return (email, password)

def login_with_email(login):
    ''' Login a user with email via auth service. '''
    email, password = get_login_credentials()
    try:
        login(email, password)
        print('\nLogged in successfully.\n')
    except Exception:  #pylint: disable=broad-except
        print('\nAn error occurred. Please check your connection, credentials and try again.\n')
        sys.exit(1)

def get_changelog():
    '''
    Opens up EDITOR, and allows user to enter changelog.
    Splits by the boilerplate text and returns user input
    '''
    current_branch = git.branch()
    data = click.edit(
        text=RELEASE_LOG_TEXT.format(current_branch),
        require_save=True
    )
    serialized = data.split(RELEASE_LOG_TEXT.format(current_branch))

    return serialized[0]
