from command.commands_factory import CommandsFactory


class CommandsInvoker:
    def __init__(self):
        self.__factory = CommandsFactory()

    def run_command(self, command_name, *args):
        command = self.__factory.get_command(command_name)
        if command is None:
            return "Exception: invalid command"
        res = command.execute(*args)
        return res
