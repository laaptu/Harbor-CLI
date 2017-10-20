''' Service for register command. '''
import sys

from lib.anchor import Anchor
from lib.logger import logger
from lib.utils.validators import is_valid_email
from lib.inqurires import getlogincredentials
from lib.services.firebase_service import Firebase

class Register(Anchor):
    '''
    Service class for register command.
    '''

    def __init__(self, user_registration):
        super().__init__()

        self.is_user_registration = user_registration or False

    def execute(self):
        ''' Register a user or a project. '''
        if self.is_user_registration:
            self.register_user()
        else:
            self.register_project()

    def register_user(self):
        ''' Register a user. '''
        # Signup credentials.
        email, password = getlogincredentials()

        if not is_valid_email(email):
            logger().error('Invalid email. Please try another one.')
            sys.exit(1)

        try:
            Firebase().signup_via_email(email, password)
        except Exception as e: #pylint: disable=broad-except
            print('error = ', e)
            logger().error('Cannot register this email. Please try another one.')
            sys.exit(1)

        success = 'Signed up successfully with email "%s"' % email

        logger().info(success)

    def register_project(self):
        ''' Register a project. '''
        logger().info('Register project.')
