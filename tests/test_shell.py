''' Test for shell module '''
from lib.shell import run

def test_run():
    ''' Should run a shell command using Popen. '''
    exitcode, _, _ = run('ls -la')

    assert exitcode == 0
