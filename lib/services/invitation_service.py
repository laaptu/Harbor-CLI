import sys

from lib.utils.gradle import get_react_native_project_name
from lib.exceptions.FileNotFound import FileNotFoundException
from lib.exceptions.UserNotFound import UserNotFoundException

class InvitationService():

    def __init__(self, email, storage_instance):
        self.email = email
        self.storage = storage_instance


    def delegate(self):
        try:
            proj_name = get_react_native_project_name()
        except FileNotFoundException as e:
            print(e.message)
            sys.exit(1)

        try:
            data = self.storage.get_details_for_user_by_email(self.email)()
            print('data:: ', data)
        except UserNotFoundException as e:
            print(e.message)
            sys.exit(1)


    def __compose_member_output_path(self, proj_name):
        ''' Returns the database  path for new uploads to a project. '''
        return 'members' + '/' + ''.join(proj_name.split('.'))
