import sys
from lib.services.firebase_service import Firebase

class FirebasePlugin():

    def apply(self, compiler):
        compiler.plugin('register_user', self.register_user)
        compiler.plugin('did_register', self.did_register)
        compiler.plugin('will_register', self.will_register)


    def register_user(self, **kwargs):
        def handle_error(e):
            error = eval(e.args[1])
            if error['error']['message'] == 'EMAIL_EXISTS':
                print('\nThis email has already been registered. Please try another one.')
            else:
                print('\nAn error occurred. Please check your connection, credentials and try again.\n')
            sys.exit(1)

        email = kwargs['email']
        password = kwargs['password']
        try:
            Firebase().signup_via_email(email, password)
            print('\nSigned up successfully.\n')
            sys.exit(0)
        except Exception as e:
            handle_error(e)


    def will_register(self, compilation):
        pass

    def did_register(self, compilation):
        pass
