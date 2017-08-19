import pyrebase

from lib.config.firebase_config import firebase_config
from lib.utils.singleton import Singleton

class Firebase(metaclass=Singleton):
    '''
    Handle firebase comm. with this class. Make this a singleton using a metaclass.
    '''

    def __init__(self, config=firebase_config):
        self.config = config
        self.firebase = pyrebase.initialize_app(self.config)
        self.auth = self.firebase.auth()
        self.db = self.firebase.database()
        self.storage = self.firebase.storage()
        self.user = None

    def login_with_email(self, email, password):
        self.user = self.auth.sign_in_with_email_and_password(email, password)

    def __refresh_token__(self):
        self.user = self.auth.refresh(self.user['refreshToken'])

    def upload(self, output_path, input_path):
        self.storage.child(output_path).put(input_path, self.user['idToken'])
