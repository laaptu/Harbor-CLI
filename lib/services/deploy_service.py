import sys
import time

from lib.services.stdio_service import get_login_credentials
from lib.utils.gradle import get_react_native_project_name
from lib.exceptions.FileNotFound import FileNotFoundException

class DeployService():

    def __init__(
        self,
        release_type,
        auth_service_instance,
        storage_instance,
        builder_instance
    ):
        self.release_type =  release_type
        self.timestamp = str(int(time.time()))
        self.builder = builder_instance
        self.storage = storage_instance
        self.auth = auth_service_instance


    def delegate(self):
        build_details = self.builder.build()
        self.login_with_email()
        try:
            proj_name = get_react_native_project_name()
        except FileNotFoundException as e:
            print(e.message)
            sys.exit(1)

        print('\nUploading %s...' % (build_details['apk_path']))
        download_url = self.storage.upload(self.__get_storage_output_path__(build_details), build_details['apk_path'])

        print('uploading with release_type: ', self.release_type)
        upload_data = {
            self.timestamp: {
                'releasedBy': self.storage.get_current_user_details()['uid'],
                'download_url': download_url,
                'releaseType': self.release_type
            }
        }

        self.storage.upload_project(self.__compose_project_output_path__(proj_name), upload_data)

        print('\nUpload successful. APK was deployed.')


    def __compose_project_output_path__(self, proj_name):
        return 'projects' + '/' + ''.join(proj_name.split('.')) + '/uploads'


    def __get_storage_output_path__(self, build_details):
        ''' Compose the output path of files to be stored in the server. '''
        name = build_details['metainf']['name']

        return name + '/' + name + '_' +  self.timestamp + '.apk'


    def login_with_email(self):
        ''' Login a user with email via auth service. '''
        email, password = get_login_credentials()
        try:
            self.auth.login_with_email(email, password)
            print('\nLogged in successfully.\n')
        except Exception as e:
            print('\nAn error occurred. Please check your connection, credentials and try again.\n')
            sys.exit(1)
