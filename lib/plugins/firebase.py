'''
Firebase plugin module.
Writes to db/storage done from here
'''
import sys
from pyspin.spin import make_spin, Default

from lib.anchor import Anchor
from lib.plugins.hipchat import HipChatPlugin
from lib.utils.destructure import destructure
from lib.services.firebase_service import Firebase
from lib.utils.gradle import get_react_native_project_name
from lib.utils.colorprinter import colorprint, print_with_spinner

EMAIL_EXISTS_ERROR_MESSAGE = 'An error occurred.\
        Please check your connection, credentials and try again.\n'
EXISTING_PACKAGE_ERROR = 'This package name is already registered.\
        If you want to update your details, please use the "--resync" flag\
        with admin credentials.'

class FirebasePlugin(Anchor):
    '''
    Handles firebase parts of any process.
    Generally, services will apply plugins which in turn apply their own.
    This is called somewhere down the tree.
    '''

    def __init__(self):
        super().__init__()
        super().apply(HipChatPlugin())

    def apply(self, compiler):
        compiler.plugin('register_user', self.register_user)
        compiler.plugin('add_user', self.add_user_to_project)
        compiler.plugin('register_project', self.register_project)

    def register_user(self, **kwargs):
        ''' Register a single user. '''
        def handle_error(error):
            '''
            Handle error when creating a user.
            The check we are interested in is EMAIL_EXISTS.
            '''
            error = eval(error.args[1])
            if error['error']['message'] == 'EMAIL_EXISTS':
                colorprint('RED')('\nThis email has already been registered. Please try another one.')
            else:
                colorprint('RED')(EMAIL_EXISTS_ERROR_MESSAGE)
            sys.exit(1)

        email, password = destructure(kwargs)('email', 'password')
        try:
            Firebase().signup_via_email(email, password)
            colorprint('GREEN')('\nSigned up successfully.\n')
            sys.exit(0)
        except Exception as error:
            handle_error(error)

    def register_project(self, **kwargs):
        '''
        Registers a project.
        Checks to see if there is a duplicate project with the same package name.
        Registers the current user as an admin.
        '''
        def project_output_path(proj_name):
            ''' Returns the database path  for projects. '''
            return ''.join(proj_name.split('.'))

        def members_output_path(user):
            ''' Returns the database path for members. '''
            return 'members/' + user['uid']

        name, package_name, icon_url = destructure(kwargs)('name', 'package_name', 'iconUrl')
        existing = Firebase().get_from_db('projects/' + project_output_path(package_name))
        if existing.val() is not None:
            colorprint('RED')(EXISTING_PACKAGE_ERROR)
            sys.exit(1)
        project_data = {
            'name': name,
            'uploads': {},
            'iconUrl': icon_url,
            'packageName': package_name,
        }
        member_admin_data = {
            'role': 'admin',
            'notificationLevel': 'all'
        }
        Firebase().write_to_db(
            'projects/' + project_output_path(package_name),
            project_data
        )
        Firebase().write_to_db(
            members_output_path(Firebase().get_current_user_details()) +
            '/' +
            project_output_path(package_name),
            member_admin_data,
            update=True
        )
        colorprint('GREEN')('Successfully registered.')
