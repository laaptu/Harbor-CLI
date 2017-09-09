''' All CLI hooks are handled through here. '''
import sys

from lib.services import deploy_service, registration_service, invitation_service
from lib.services.firebase_service import Firebase
from lib.services.builder_service import builder
from lib.constants.release_types import ReleaseTypes
from lib.utils.validators import is_valid_email

import click

@click.group()
def cli():
    ''' CLI for the Harbor application. '''
    pass


@click.command()
@click.option('-u', is_flag=True, help='Flag to indicate if a user is to be registered.')
def register(u):
    ''' Register your project/user on the server. '''
    registration_service.RegistrationService().delegate(True if u else False)


@click.command()
@click.option('--type', help='Release type [qa, uat, dev]. This affects the audience that receives notice of this release. Default value of "dev" is assumed')
def deploy(type):
    ''' Deploy your project once it has been registered. '''
    if type is None:
        type = ReleaseTypes.DEV.value

    if type.lower() not in [release_type.value.lower() for release_type in ReleaseTypes]:
        print('"{0}" is not a valid release type. Please use "uat", "qa" or "dev".'.format(type))
        sys.exit(1)

    deploy_service.DeployService(
        type,
        Firebase(),
        Firebase(),
        builder()()
    ).delegate()


@click.command()
@click.argument('email')
@click.option('--role', help='Role to register the user under. [qa, uat, dev]. This affects how they receive updates regarding releases. Default value of "dev" is assumed.')
def invite(email, role):
    ''' Invite someone to the project. '''
    if role is None:
        role = ReleaseTypes.DEV.value

    if role.lower() not in [release_type.value.lower() for release_type in ReleaseTypes]:
        print('"{0}" is not a valid role. Please use "uat", "qa" or "dev".'.format(role))
        sys.exit(1)

    if not is_valid_email(email):
        print('"{0}" is not a valid email.'.format(email))
        sys.exit(1)

    invitation_service.InvitationService(
        role,
        email,
        Firebase()
    ).delegate()


cli.add_command(register)
cli.add_command(deploy)
cli.add_command(invite)
