from command.commands_invoker import CommandsInvoker
from terminal.cli import Cli


class Batch(Cli):
    def __init__(self):
        super().__init__("batch")
        self.__invoker = CommandsInvoker()

    def run(self):
        batch = []
        while True:
            command = self._get_input()
            if command == "end":
                return batch
            batch.append(command)

    def execute_command(self, command):
        return self._manage_command(command, self.__invoker)
