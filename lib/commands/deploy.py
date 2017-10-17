''' Service for deploy command. '''
import sys

from lib import android
from lib.anchor import Anchor
from lib.logger import logger
from lib.firebase.auth import login
from lib.inqurires import (
    getchangelog,
    getversionnumber,
    getlogincredentials
)


DEPLOY_TYPES = ['uat', 'dev', 'qa']


class Deploy(Anchor):
    '''
    Service class for deployment. Subclasses Anchor to expose lifecycle events.
    '''
    def __init__(self, deploy_type):
        super().__init__()

        self.version = None
        self.changelog = None
        self.deploy_type = sanitize_deploy_type(deploy_type)

    def deploy(self):
        ''' Deploy project. '''
        email, password = getlogincredentials()
        login(email, password)
        self.version = getversionnumber()
        self.changelog = getchangelog()
        clean_and_build()

def sanitize_deploy_type(incoming_deploy_type):
    ''' For unpermitted incoming deploy type, fallback to 'dev'.  '''
    if incoming_deploy_type not in DEPLOY_TYPES:
        logger().warning('Unspecified or unpermitted deploy type - Falling back to "dev"')
        return 'dev'

    return incoming_deploy_type

def clean_and_build():
    ''' Clean and build the android project. '''
    if not android.is_android():
        logger().error('Not in a valid android project.')
        sys.exit(1)

    logger().info('Cleaning the project..')
    clean_exitcode, _, _ = android.clean()
    if clean_exitcode is not 0:
        logger().error('Clean failed. Please check that your project is valid. code = ')
        sys.exit(1)

    logger().info('Clean succesful')
    logger().info('Building the project..')
    build_exitcode, _, _ = android.build()
    if build_exitcode is not 0:
        logger().error('Build failed. Please check that your project is valid.')
        sys.exit(1)

    logger().info('Build complete.')
