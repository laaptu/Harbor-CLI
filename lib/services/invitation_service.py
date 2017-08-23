import sys

from lib.utils.gradle import get_react_native_project_name

class InvitationService():

    def __init__(self, role, email, storage_instance):
        self.role = role
        self.target_email = email
        self.storage = storage_instance


    def delegate(self):
        try:
            proj_name = get_react_native_project_name()
            data = self.storage.get_details_for_user_by_email(self.target_email)()
            target_uid = data['uid']
        except Exception as e:
            print(e.message)
            sys.exit(1)

        proj_members_path = self.__compose_member_output_path__(proj_name)
        user_details = {
            target_uid: {
                'role': self.role,
                'notificationLevel': 'all'
            }
        }

        self.storage.add_user_to_project(proj_members_path, user_details)
        print('Invited "{0}" to "{1}" as "{2}"'.format(self.target_email, proj_name, self.role))


    def __compose_member_output_path__(self, proj_name):
        ''' Returns the database  path for new uploads to a project. '''
        return ''.join(proj_name.split('.'))
