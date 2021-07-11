from command.analysis_commands.find_command import FindCommand
from command.analysis_commands.len_command import LenCommand
from command.creation_commands.dup_command import DupCommand
from command.creation_commands.load_command import LoadCommand
from command.creation_commands.new_command import NewCommand
from command.management_commands.del_command import DelCommand
from command.management_commands.save_command import SaveCommand
from command.manipulation_commands.pair_command import PairCommand
from command.manipulation_commands.slice_command import SliceCommand


class CommandsFactory:
    def __init__(self):
        self.__commands = {
            "new": NewCommand,
            "load": LoadCommand,
            "dup": DupCommand,
            "slice": SliceCommand,
            "pair": PairCommand,
            "del": DelCommand,
            "save": SaveCommand,
            "len": LenCommand,
            "find": FindCommand
        }

    def get_command(self, command_name):
        if command_name not in self.__commands:
            return None
        return self.__commands[command_name]()
