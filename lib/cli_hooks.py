''' All CLI hooks are handled through here. '''

from lib.services import registration_service

import click

@click.group()
def cli():
    ''' CLI for the Harbor application. '''
    pass


@click.command()
def register():
    ''' Register your project on the server. '''
    registration_service.delegate()


@click.command()
def deploy():
    ''' Deploy your project once it's registered. '''
    deploy_service.delegate()


cli.add_command(register)
cli.add_command(deploy)
