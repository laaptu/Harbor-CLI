import pyrebase

from lib.config.firebase_config import firebase_config
from lib.utils.singleton import Singleton

class Firebase(metaclass=Singleton):
    '''
    Handle firebase comm. with this class. Make this a singleton using a metaclass.
    '''

    def __init__(self, config=firebase_config):
        ''' Initialize auth, db, storage handles. '''
        self.config = config
        self.firebase = pyrebase.initialize_app(self.config)
        self.auth = self.firebase.auth()
        self.db = self.firebase.database()
        self.storage = self.firebase.storage()
        self.user = None


    def login_with_email(self, email, password):
        ''' Login via email. '''
        self.user = self.auth.sign_in_with_email_and_password(email, password)


    def __refresh_token__(self):
        ''' Refresh user token '''
        self.user = self.auth.refresh(self.user['refreshToken'])


    def upload(self, output_path, input_path):
        ''' Upload file to a output path. '''
        self.storage.child(output_path).put(input_path, self.user['idToken'])

        return self.storage.child(output_path).get_url()


    def signup_via_email(self, email, password):
        ''' Create an account. '''
        self.auth.create_user_with_email_and_password(email, password)


    def register_project(self, output_path, data):
        ''' Register a project. '''
        self.db.child('projects').child(output_path).set(data)

        # Firebase doesn't suppporty dynamic key deep queries.
        # So, we resort to client side filtering.
        userdata =  self.db.child('users').get()
        serializeddata = dict(userdata.val())
        filter_user_email = lambda data: data['email'] == self.user['email']
        user_details = list(filter(filter_user_email, [serializeddata[v] for v in serializeddata]))[0]

        self.db.child('members').child(output_path).set({
            user_details['uid']: True
        })


    def upload_project(self, output_path, data):
        ''' Upload a project. '''
        pass
