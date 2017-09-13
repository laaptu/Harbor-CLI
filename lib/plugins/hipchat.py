'''
HipChat plugin.
'''
import requests
from lib.services import config
from lib.utils import git
from lib.utils.destructure import destructure


class HipChatPlugin():
    '''
    Must be a class with an apply method to be applied as a plugin.
    '''

    def __init__(self):
        self.hipchat_url = "https://{0}.hipchat.com/v2/room/{1}/notification?auth_token={2}"
        self.deploying_message = "{0} is deploying a {1} build from branch {2}."
        self.deployed_message = "{0} deployed a {1} build from branch {2}. See the changelog {3}."

    def apply(self, compiler):
        ''' Register plugins. '''
        compiler.plugin('deploy/will_upload', self.pre_deploy)
        compiler.plugin('deploy/did_deploy', self.did_deploy)

    def pre_deploy(self, compilation):
        ''' Send a notification before deploying. '''
        # hipchatdetails = destructure(compilation)('hipchatdetails')
        if not config.is_hipchat_configured():
            return
        release_type, branch = destructure(compilation)(
            'release_type', 'branch'
        )

        hipchat_details = config.get()['hipchat']
        company_name, room_id, auth_token = destructure(hipchat_details)(
            'company_name', 'room_id', 'auth_token'
        )
        notification_data = {
            'color': "green",
            'message': self.deploying_message.format(
                git.whoami(), release_type, branch
            ),
            'notify': True,
            'message_format': "html"
        }
        requests.post(
            self.hipchat_url.format(company_name, room_id, auth_token),
            data=notification_data
        )

    def did_deploy(self, compilation):
        ''' Send a notification after deploying. '''
        pass
