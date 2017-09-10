import sys
import time
from datetime import datetime
import calendar

from lib.anchor import Anchor
from lib.plugins.firebase import FirebasePlugin
from lib.services.builder_service import builder
from lib.services.firebase_service import Firebase
from lib.services.stdio_service import get_login_credentials
from lib.exceptions.FileNotFound import FileNotFoundException

class DeployService(Anchor):

    def __init__(self, release_type):
        super().__init__()
        self.apply(FirebasePlugin())
        self.builder = builder()()
        self.release_type =  release_type


    def delegate(self):
        build_details = self.builder.build()
        self.login_with_email()
        self.apply_plugins('deploy_project',
                           build_details=build_details,
                           release_type=self.release_type
                           )


    def login_with_email(self):
        ''' Login a user with email via auth service. '''
        email, password = get_login_credentials()
        try:
            Firebase().login_with_email(email, password)
            print('\nLogged in successfully.\n')
        except Exception as e:
            print('\nAn error occurred. Please check your connection, credentials and try again.\n')
            sys.exit(1)
