from command import batch_commands
from command import analysis_commands
from command import creation_commands
from command import management_commands
from command import manipulation_commands


class CommandsFactory:
    def __init__(self):
        self.__commands = {
            "new": creation_commands.NewCommand,
            "load": creation_commands.LoadCommand,
            "dup": creation_commands.DupCommand,
            "slice": manipulation_commands.SliceCommand,
            "pair": manipulation_commands.PairCommand,
            "del": management_commands.DelCommand,
            "save": management_commands.SaveCommand,
            "len": analysis_commands.LenCommand,
            "find": analysis_commands.FindCommand,
            "count": analysis_commands.CountCommand,
            "findall": analysis_commands.FindallCommand,
            "batch": batch_commands.BatchCreationCommand,
            "run": batch_commands.RunBatchCommand,
            "batchlist": batch_commands.ListBatchCommand
        }

    def get_command(self, command_name):
        if command_name not in self.__commands:
            return None
        return self.__commands[command_name]()
