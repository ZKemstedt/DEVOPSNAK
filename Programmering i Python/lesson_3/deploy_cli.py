import cmd
import sys

from cli_tool.api import deploy, restart
from cli_tool.validation import return_on_except
from cli_tool.utils import parse


class DeployTool(cmd.Cmd):
    intro = 'Welcome to the deployment tool. Type help or ? to list commands.\n'
    prompt = '(Deployment tool) '

    def do_bye(self, arg):
        'Close the deployment tool, and exit'
        return True

    @return_on_except
    def do_deploy(self, arg):
        'Deploy with arguments: service=backend conf=test'
        return deploy(**parse(arg))

    @return_on_except
    def do_restart(self, arg):
        'Restart service'
        return restart(**parse(arg))

    def postcmd(self, stop, line):
        """Hook method executed just after a command dispatch is finished."""
        if isinstance(stop, int):
            sys.exit(stop)
        return stop


if __name__ == '__main__':
    DeployTool().cmdloop()
