import sys
from lib.services.firebase_service import Firebase
from lib.utils.destructure import destructure

class FirebasePlugin():

    def apply(self, compiler):
        compiler.plugin('register_user', self.register_user)
        compiler.plugin('add_user', self.add_user_to_project)
        compiler.plugin('register_project', self.register_project)


    def register_user(self, **kwargs):
        ''' Register a single user. '''
        def handle_error(e):
            error = eval(e.args[1])
            if error['error']['message'] == 'EMAIL_EXISTS':
                print('\nThis email has already been registered. Please try another one.')
            else:
                print('\nAn error occurred. Please check your connection, credentials and try again.\n')
            sys.exit(1)

        email, password = destructure(kwargs)('email', 'password')
        try:
            Firebase().signup_via_email(email, password)
            print('\nSigned up successfully.\n')
            sys.exit(0)
        except Exception as e:
            handle_error(e)


    def register_project(self, **kwargs):
        '''
        Registers a project.
        Checks to see if there is a duplicate project with the same package name.
        Registers the current user as an admin.
        '''
        def project_output_path(proj_name):
            return ''.join(proj_name.split('.'))

        def members_output_path(user):
            return user['uid']

        name, package_name, iconUrl = destructure(kwargs)('name', 'package_name', 'iconUrl')
        existing  = Firebase().get_from_db('projects/' + project_output_path(package_name))
        if existing.val() is not None:
            print('This package name is already registered. If you want to update your details, please use the "--resync" flag with admin credentials.')
            sys.exit(1)
        project_data = {
            'name': name,
            'uploads': {},
            'iconUrl': iconUrl,
            'packageName': package_name,
        }
        member_admin_data = {
            'role': 'admin',
            'notificationLevel': 'all'
        };
        Firebase().write_to_db(
            'projects/' + project_output_path(package_name),
            project_data
        )
        Firebase().write_to_db(
            'members/' + members_output_path(Firebase().get_current_user_details()) + '/' + project_output_path(package_name),
            member_admin_data,
            update=True
        )
        print('Successfully registered.')


    def add_user_to_project(self, **kwargs):
        def proj_path(proj_name):
            return ''.join(proj_name.split('.'))

        def members_output_path(user, proj_name):
            return 'members/' + user['uid'] + '/' + proj_path(proj_name)

        target_email, role, project_name = destructure(kwargs)('email', 'role', 'project_name')
        user = Firebase().get_details_for_user_by_email(target_email)()
        data = {
            'role': role,
            'notificationLevel': role
        }
        Firebase().write_to_db(
            members_output_path(user, project_name),
            data,
            update=True
        )
        print('Invited "{0}" to "{1}" as "{2}"'.format(target_email, project_name, role))


    def will_register(self, compilation):
        pass

    def did_register(self, compilation):
        pass
