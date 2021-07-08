from cli.cli import Cli
from command.commands_invoker import CommandsInvoker


class Cmd(Cli):
    def __init__(self):
        self.__invoker = CommandsInvoker()

    def run(self):
        while True:
            command = self._get_input("cmd")
            res = self.__manage_command(command)
            self._print_to_user(res)

    def __manage_command(self, command):
        args = command.split()
        res = self.__invoker.run_command(args[0], *args[1:])
        return res


