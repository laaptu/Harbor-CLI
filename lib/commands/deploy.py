''' Service for deploy command. '''
import sys
from terminaltables import SingleTable

from lib import android, git
from lib.anchor import Anchor
from lib.logger import logger
from lib.firebase.auth import login
from lib.utils.colorprinter import colorprint
from lib.inqurires import (
    getchangelog,
    getversionnumber,
    getlogincredentials,
    getdeploymentconfirmation
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
        self.projectdetails = None
        self.builddetails = None
        self.deploy_type = sanitize_deploy_type(deploy_type)

    def deploy(self):
        ''' Deploy project. '''
        # email, password = getlogincredentials()
        # login(email, password)

        self.version = getversionnumber()

        self.changelog = getchangelog()

        # clean_and_build()

        self.projectdetails = android.project_details()
        self.builddetails = android.build_details()

        self.show_summary()

        is_confirmed = getdeploymentconfirmation()

        if not is_confirmed:
            logger().warning('Deployment aborted.')
            sys.exit(1)

        logger().info('Deployment confirmation obtained.')


    def show_summary(self):
        '''
        This shows the summary of the current deployment process to the user.
        No more user interaction happens after this point.
        '''
        # TODO: colors not working properly
        green = colorprint('GREEN', bail_result=True)
        yellow = colorprint('YELLOW', bail_result=True)
        red = colorprint('RED', bail_result=True)

        summary_data = [
            [
                'Detail Item',
                'Description'
            ],
            [
                green('Package Name: '),
                yellow(self.projectdetails['packagename'])
            ],
            [
                green('Name: '),
                yellow(self.projectdetails['name'] or self.projectdetails['packagename'])
            ],
            [
                green('Deploy version: '),
                yellow(self.version) if self.version else red('N/A')
            ],
            [
                green('APK Size: '),
                yellow('~' + str(self.builddetails['size']) + 'MB')
            ],
            [
                green('Signed Status: '),
                yellow('Signed' if self.builddetails['is_signed'] else 'Not Signed')
            ],
            [
                green('Current deployer: '),
                yellow(git.username())
            ],
            [
                green('Current branch: '),
                yellow(git.branch())
            ]
        ]
        table = SingleTable(summary_data)

        print(table.table)

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


