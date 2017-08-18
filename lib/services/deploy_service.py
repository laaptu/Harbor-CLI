import sys

from lib.services.stdio_service import get_login_credentials

class DeployService():

    def __init__(self, auth_service_instance, builder_instance):
        self.builder = builder_instance
        self.auth_service = auth_service_instance

    def delegate(self):
        # self.login_with_email()
        self.builder.build()

    def login_with_email(self):
        email, password = get_login_credentials()
        try:
            self.auth_service.login_with_email(email, password)
            print('\nLogged in successfully.\n')
        except Exception as e:
            print('\nAn error occurred. Please check your connection, credentials and try again.\n')
            sys.exit(1)
