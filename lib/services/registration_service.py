import sys

from lib.anchor import Anchor
from lib.constants.paths import paths
from lib.services.stdio_service import get_login_credentials
from lib.services.firebase_service import Firebase
from lib.utils.gradle import get_react_native_project_name
from lib.utils.json_parser import json_parse
from lib.exceptions.FileNotFound import FileNotFoundException
from lib.plugins.firebase import FirebasePlugin
from lib.utils.decorators import requires_presence_of_file

class RegistrationService(Anchor):

    def __init__(self):
        super().__init__()
        self.apply(FirebasePlugin())


    def delegate(self, is_user_registration=False):
        ''' Delegate for the CLI. The only public method. '''
        if is_user_registration:
            email, password = get_login_credentials()
            self.apply_plugins('register_user', email=email, password=password)

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
            icon_path = Firebase().upload(package_json_name + '/icon.png', paths['ICONS_XXHDPI'])
        except FileNotFoundException as e:
            icon_path = None
            print(e.message)

        self.apply_plugins('register_project', name=package_json_name, package_name=package_name, iconUrl=icon_path)

    @requires_presence_of_file(
        paths['ICONS_XXHDPI'],
        lambda path: 'Cannot find icons in path {0}. Skipping..'.format(path)
    )
    def find_icons(self):
        return True


    def login_with_email(self):
        ''' Login a user with email via auth service. '''
        email, password = get_login_credentials()
        try:
            Firebase().login_with_email(email, password)
            print('\nLogged in successfully.\n')
        except Exception as e:
            print('\nAn error occurred. Please check your connection, credentials and try again.\n')
            sys.exit(1)

