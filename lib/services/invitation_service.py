import sys

from lib.anchor import Anchor
from lib.utils.gradle import get_react_native_project_name
from lib.plugins.firebase import FirebasePlugin

class InvitationService(Anchor):

    def __init__(self, role, email):
        super().__init__();
        self.apply(FirebasePlugin())
        self.role = role
        self.target_email = email


    def delegate(self):
        try:
            proj_name = get_react_native_project_name()
        except Exception as e:
            print(e.message)
            sys.exit(1)

        self.apply_plugins('add_user', email=self.target_email, role=self.role, project_name=proj_name)
