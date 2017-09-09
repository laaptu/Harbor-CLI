import sys

from lib.services.stdio_service import get_login_credentials
from lib.utils.gradle import get_react_native_project_name
from lib.exceptions.FileNotFound import FileNotFoundException
from lib.anchor import Anchor
from lib.plugins.firebase import FirebasePlugin

class RegistrationService(Anchor):

    def __init__(
        self,
        auth_service_instance,
        storage_instance
    ):
        super().__init__()
        self.auth = auth_service_instance
        self.storage = storage_instance
        self.apply(FirebasePlugin())


    def delegate(self, is_user_registration=False):
        ''' Delegate for the CLI. The only public method. '''
        if is_user_registration:
            self.__create_user_with_email__()
            sys.exit(0)

        self.login_with_email()
        self.__register_project__()


    def __register_project__(self):
        ''' Register a project on the server. '''
        try:
            proj_name = get_react_native_project_name()
            self.apply_plugins('will_register', proj_name)
        except FileNotFoundException as e:
            print(e.message)
            sys.exit(1)

        data = {
            'name': proj_name,
            'uploads': {}
        }

        print('Registering project: ', proj_name)

        self.storage.register_project(self.__compose_project_output_path__(proj_name), data)
        self.apply_plugins('did_register', proj_name)
        print('Done.')


    def login_with_email(self):
        ''' Login a user with email via auth service. '''
        email, password = get_login_credentials()
        try:
            self.auth.login_with_email(email, password)
            print('\nLogged in successfully.\n')
        except Exception as e:
            print('\nAn error occurred. Please check your connection, credentials and try again.\n')
            sys.exit(1)


    def __compose_project_output_path__(self, proj_name):
        return ''.join(proj_name.split('.'))


    def __create_user_with_email__(self):
        ''' Create a new  user with  the auth service. '''
        email, password = get_login_credentials()
        try:
            self.auth.signup_via_email(email, password)
            print('\nSigned up successfully.\n')
        except Exception as e:
            # TODO: Workaround the hacky eval usage here. Need to get 'message' from request.exception class instance.
            error = eval(e.args[1])

            if error['error']['message'] == 'EMAIL_EXISTS':
                print('\nEmail already registered.')
            else:
                print('\nAn error occurred. Please check your connection, credentials and try again.\n')
            sys.exit(1)
