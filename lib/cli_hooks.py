''' All CLI hooks are handled through here. '''
import sys

from lib.services import deploy_service, registration_service
from lib.services.firebase_service import Firebase
from lib.services.builder_service import builder
from lib.constants.release_types import ReleaseTypes

import click

@click.group()
def cli():
    ''' CLI for the Harbor application. '''
    pass


@click.command()
@click.option('-u', is_flag=True, help='Flag to indicate if a user is to be registered.')
def register(u):
    ''' Register your project/user on the server. '''
    registration_service.RegistrationService(
        Firebase(),
        Firebase()
    ).delegate(True if u else False)


@click.command()
@click.option('--type', help='Release type [qa, uat, dev]')
def deploy(type):
    if type.lower() not in [release_type.value.lower() for release_type in ReleaseTypes]:
        print('{0} is not a valid release type'.format(type))
        sys.exit(1)
    ''' Deploy your project once it's registered. '''
    deploy_service.DeployService(
        Firebase(),
        Firebase(),
        builder()()
    ).delegate()


cli.add_command(register)
cli.add_command(deploy)
