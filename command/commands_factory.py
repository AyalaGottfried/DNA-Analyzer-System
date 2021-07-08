from command.creation_commands.dup_command import DupCommand
from command.creation_commands.load_command import LoadCommand
from command.creation_commands.new_command import NewCommand
from command.manipulation_commands.slice_command import SliceCommand


class CommandsFactory:
    def __init__(self):
        self.__commands = {"new": NewCommand, "load": LoadCommand, "dup": DupCommand, "slice": SliceCommand}

    def get_command(self, command_name):
        if command_name not in self.__commands:
            return None
        return self.__commands[command_name]()
