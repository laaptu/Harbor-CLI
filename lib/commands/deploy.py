''' Service for deploy command. '''
import sys
from terminaltables import SingleTable

from lib import android, git
from lib.shell import whoami
from lib.anchor import Anchor
from lib.logger import logger
from lib.utils.colorprinter import colorprint
from lib.services.firebase_service import Firebase
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

        self.now = now()
        self.version = None
        self.apk_url = None
        self.changelog = None
        self.builddetails = None
        self.projectdetails = None
        self.deployer = git.username() or whoami()
        self.deploy_type = sanitize_deploy_type(deploy_type)

    def deploy(self):
        ''' Deploy project. '''
        email, password = getlogincredentials()
        Firebase().login_with_email(email, password)

        self.version = getversionnumber()

        self.changelog = getchangelog()

        clean_and_build()

        self.projectdetails = android.project_details()
        self.builddetails = android.build_details()

        self.show_summary()

        is_confirmed = getdeploymentconfirmation()

        if not is_confirmed:
            logger().warning('Deployment aborted.')
            sys.exit(1)

        logger().info('Deployment confirmation obtained.')

        logger().info('Uploading APK to remote server..')

        self.upload()
        self.update_project()

        logger().info('Upload complete. Deployment successful.')

    def upload(self):
        ''' Upload the APK to storage. '''
        path = '{packagename}/{packagename}_{timenow}.apk'

        sanitizedpackagename = ''.join(self.projectdetails['packagename'].split('.'))

        self.apk_url = Firebase().upload(
            path.format(
                packagename=sanitizedpackagename,
                timenow=self.now
            ),
            self.builddetails['apk_path']
        )

    def update_project(self):
        ''' Upload the database to reflect a new release. '''
        user = Firebase().get_current_user_details()

        upload_data = {
            'releasedBy': user,
            'branch': git.branch(),
            'version': self.version,
            'changelog': self.changelog,
            'download_url': self.apk_url,
            'deployerName': self.deployer,
            'releaseType': self.deploy_type
        }

        Firebase().write_to_db(
            get_projectpath(self.projectdetails['packagename'], self.now),
            upload_data,
            update=True
        )

        metadata = {
            'lastReleasedBy': user,
            'lastReleasedOn': self.now,
            'deployerName': self.deployer,
            'currentVersion': self.version
        }

        Firebase().write_to_db(
            metadata_path(self.projectdetails['packagename']),
            metadata
        )

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
                yellow(self.deployer)
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

    logger().info('Clean succesful.')
    logger().info('Building the project..')
    build_exitcode, _, _ = android.build()
    if build_exitcode is not 0:
        logger().error('Build failed. Please check that your project is valid.')
        sys.exit(1)

    logger().info('Build complete.')

def now():
    ''' A helper to get current timestamp. '''
    from datetime import datetime
    import calendar
    timenow = datetime.utcnow()
    return str(calendar.timegm(timenow.utctimetuple()))

def get_projectpath(packagename, timenow):
    ''' Get the project path for a packagename. '''
    path = 'projects/{0}/uploads/{1}'

    sanitizedpackagename = ''.join(packagename.split('.'))

    return path.format(sanitizedpackagename, timenow)

def metadata_path(packagename):
    ''' Get the db path to metadata for a packagename. '''
    path = 'projects/{0}/metadata'

    sanitizedpackagename = ''.join(packagename.split('.'))

    return path.format(sanitizedpackagename)
