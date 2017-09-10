import sys

from lib.anchor import Anchor
from lib.plugins.firebase import FirebasePlugin
from lib.utils.gradle import get_react_native_project_name
from lib.services.firebase_service import Firebase
from lib.services.stdio_service import get_login_credentials

class InvitationService(Anchor):

    def __init__(self, role, email):
        super().__init__();
        self.apply(FirebasePlugin())
        self.role = role
        self.target_email = email


    def delegate(self):
        try:
            proj_name = get_react_native_project_name()
        except Exception as e:
            print(e.message)
            sys.exit(1)

        self.login_with_email()
        self.apply_plugins('add_user', email=self.target_email, role=self.role, project_name=proj_name)


    def login_with_email(self):
        ''' Login a user with email via auth service. '''
        email, password = get_login_credentials()
        try:
            Firebase().login_with_email(email, password)
            print('\nLogged in successfully.\n')
        except Exception as e:
            print('\nAn error occurred. Please check your connection, credentials and try again.\n')
            sys.exit(1)
