import sys
from lib.services.stdio_service import get_login_credentials

class RegistrationService():

    def __init__(
        self,
        auth_service_instance
    ):
        self.auth = auth_service_instance

    def delegate(self, is_user_registration=False):
        ''' Delegate for the CLI. The only public method. '''
        if is_user_registration:
            self.__create_user_with_email__()


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
