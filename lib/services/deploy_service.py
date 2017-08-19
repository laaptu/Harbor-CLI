import sys
import time

from lib.services.stdio_service import get_login_credentials

class DeployService():

    def __init__(
        self,
        auth_service_instance,
        storage_instance,
        builder_instance
    ):
        self.builder = builder_instance
        self.storage = storage_instance
        self.auth = auth_service_instance

    def delegate(self):
        self.login_with_email()
        build_details = self.builder.build()
        print('\nUploading %s...' % (build_details['apk_path']))
        self.storage.upload(self.__get_output_path__(build_details), build_details['apk_path'])

        print('\nUpload successful. APK was deployed.')

    def __get_output_path__(self, build_details):
        name = build_details['metainf']['name']
        timestamp = time.time()

        return name + '/' + name + '_' + str(int(timestamp)) + '.apk'

    def login_with_email(self):
        email, password = get_login_credentials()
        try:
            self.auth.login_with_email(email, password)
            print('\nLogged in successfully.\n')
        except Exception as e:
            print('\nAn error occurred. Please check your connection, credentials and try again.\n')
            sys.exit(1)
