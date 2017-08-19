''' All CLI hooks are handled through here. '''

from lib.services import deploy_service, registration_service
from lib.services.firebase_service import Firebase
from lib.services.builder_service import builder

import click

@click.group()
def cli():
    ''' CLI for the Harbor application. '''
    pass


@click.command()
def register():
    ''' Register your project on the server. '''
    registration_service.RegistrationService(
        Firebase()
    ).delegate()


@click.command()
def deploy():
    ''' Deploy your project once it's registered. '''
    deploy_service.DeployService(
        Firebase(),
        Firebase(),
        builder()()
    ).delegate()


cli.add_command(register)
cli.add_command(deploy)
