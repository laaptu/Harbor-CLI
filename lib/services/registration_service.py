import sys

from lib.services.stdio_service import get_login_credentials
from lib.utils.gradle import get_react_native_project_name
from lib.utils.json_parser import json_parse
from lib.exceptions.FileNotFound import FileNotFoundException
from lib.utils.decorators import requires_presence_of_file
from lib.constants.paths import paths

class RegistrationService():

    def __init__(
        self,
        auth_service_instance,
        storage_instance
    ):
        self.auth = auth_service_instance
        self.storage = storage_instance


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
            package_name = get_react_native_project_name()
            package_json = json_parse('package.json')
            package_json_name = package_json['name']
        except FileNotFoundException as e:
            print(e.message)
            sys.exit(1)

        try:
            print('Searching for icons..')
            self.find_icons()
            icon_path = self.storage.upload(package_json_name + '/icon.png', paths['ICONS_XXXHDPI'])
        except FileNotFoundException as e:
            print(e.message)

        data = {
            'uploads': {},
            'iconUrl': icon_path,
            'name': package_json_name,
            'packageName': package_name
        }

        print('Registering project: ', package_name)
        self.storage.register_project(self.__compose_project_output_path__(package_name), data)
        print('Done.')

    @requires_presence_of_file(
        paths['ICONS_XXXHDPI'],
        lambda path: 'Cannot find icons in path {0}. Skipping..'.format(path)
    )
    def find_icons(self):
        return True


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
