''' All CLI hooks are handled through here. '''
import sys
import click
from pyfiglet import Figlet

from lib.logger import init_logger, logger
from lib.utils.validators import is_valid_email
from lib.constants.release_types import ReleaseTypes
from lib.services import deploy_service, registration_service, invitation_service

from lib.commands.deploy import Deploy

REGISTER_HELP_TEXT = 'Flag to indicate if a user is to be registered.'
DEPLOY_HELP_TEXT = 'Release type [qa, uat, dev].\
        This affects the audience that receives notice of this release.\
        Default value of "dev" is assumed'
INVITATION_HELP_TEXT = 'Role to register the user under [qa, uat, dev].\
        This affects how they receive updates regarding releases.\
        Default value of "dev" is assumed.'
INVALID_ROLE = 'Role {0} is not valid. Please use one of ["qa", "uat", "dev"] '
INVALID_DEPLOY_TYPE = 'Please use "uat", "qa" or "dev" as the deploy type'
INVALID_EMAIL = '"{0}" is not a valid email.'

# Clear the screen.
click.clear()

# Show a ASCII art on the screen.
print(Figlet().renderText('HARBOR'))

# Initalize logger.
init_logger()

@click.group()
def cli():
    ''' CLI for the Harbor application. '''
    pass


@click.command()
@click.option('--user', is_flag=True, help=REGISTER_HELP_TEXT)
def register(user):
    ''' Register your project/user on the server. '''
    registration_service.RegistrationService().delegate(True if user else False)


@click.command()
@click.option('--deploy-type', help=DEPLOY_HELP_TEXT)
def deploy(deploy_type):
    ''' Deploy your project after registration. '''
    Deploy(deploy_type).deploy()


@click.command()
@click.argument('email')
@click.option('--role', help=INVITATION_HELP_TEXT)
def invite(email, role):
    ''' Invite someone to the project. '''
    def validate_role(role, accepted_values):
        '''  Check if role is in list of accepted_values. '''
        if role.lower() not in accepted_values:
            logger().error(INVALID_ROLE.format(role))
            sys.exit(1)

    if role is None:
        role = ReleaseTypes.DEV.value
    validate_role(role, [release_type.value.lower() for release_type in ReleaseTypes])

    if not is_valid_email(email):
        logger().error(INVALID_EMAIL.format(email))
        sys.exit(1)

    invitation_service.InvitationService(role, email).delegate()


cli.add_command(register)
cli.add_command(deploy)
cli.add_command(invite)
