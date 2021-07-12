from command.commands_invoker import CommandsInvoker
from terminal.cli import Cli


class Cmd(Cli):
    def __init__(self):
        super().__init__("cmd")
        self.__invoker = CommandsInvoker()

    def run(self):
        while True:
            command = self._get_input()
            res = self._manage_command(command, self.__invoker)
            self._print_to_user(res)



if __name__ == "__main__":
    Cmd().run()
