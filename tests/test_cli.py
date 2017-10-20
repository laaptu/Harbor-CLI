'''
Tests that the CLI runs correctly.
'''

from lib.cli import cli
from lib import __version__
from click.testing import CliRunner

DEPLOY_HELP = 'Deploy your project once it has been registered.'
REGISTER_HELP = 'Register your project/user on the server.'
INVITE_HELP = 'Invite someone to the project.'


def test_option_version():
    ''' Test the --version option. '''
    runner = CliRunner()

    result = runner.invoke(cli, ['--version'])
    assert result.exit_code == 0
    assert __version__ in result.output


def test_deploy():
    ''' Test the deploy command. '''
    runner = CliRunner()

    result = runner.invoke(cli, ['deploy', '--help'])
    assert result.exit_code == 0
    assert DEPLOY_HELP in result.output


def test_register():
    ''' Test the register command. '''
    runner = CliRunner()

    result = runner.invoke(cli, ['register', '--help'])
    assert result.exit_code == 0
    assert REGISTER_HELP in result.output


def test_invite():
    ''' Test the invite command. '''
    runner = CliRunner()

    result = runner.invoke(cli, ['invite', '--help'])
    assert result.exit_code == 0
    assert INVITE_HELP in result.output
