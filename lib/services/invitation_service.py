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

        proj_members_path = self.__compose_member_path__(target_uid)
        user_details_for_proj = {
            self.__compose_proj_path__(proj_name): {
                'role': self.role,
                'notificationLevel': self.role
            }
        }

        self.storage.add_user_to_project(proj_members_path, user_details_for_proj)
        print('Invited "{0}" to "{1}" as "{2}"'.format(self.target_email, proj_name, self.role))


    def __compose_member_path__(self, target_uid):
        ''' Returns the database  path for new uploads to a project. '''
        return target_uid

    def __compose_proj_path__(self, proj_name):
        return ''.join(proj_name.split('.'))

