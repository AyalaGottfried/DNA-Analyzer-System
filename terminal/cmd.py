from command.commands_invoker import CommandsInvoker
from terminal.cli import Cli


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
        try:
            res = self.__invoker.run_command(args[0], *args[1:])
        except Exception as e:
            return e.args[0]
        return res


if __name__ == "__main__":
    Cmd().run()
