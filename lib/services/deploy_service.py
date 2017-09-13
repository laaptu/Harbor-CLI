'''
Handle deployments from here.
'''
from lib.utils import git
from lib.anchor import Anchor
from lib.plugins.firebase import FirebasePlugin
from lib.services.builder_service import builder
from lib.services.firebase_service import Firebase
from lib.services.stdio_service import login_with_email, get_changelog


class DeployService(Anchor):
    '''
    An Anchor class to deploy a project.
    While the bulk of the work is done by the plugins, this class
    does supplementary work.
    '''
    def __init__(self, release_type):
        super().__init__()
        self.apply(FirebasePlugin())
        self.build = builder()
        self.release_type = release_type

    def delegate(self):
        ''' Public method used as the CLI hook. '''
        build_details = self.build()
        login_with_email(Firebase().login_with_email)
        changelog = get_changelog()
        self.apply_plugins('deploy_project',
                           changelog=changelog,
                           branch=git.branch(),
                           build_details=build_details,
                           release_type=self.release_type
                          )
