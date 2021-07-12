from command import analysis_commands, control_commands, management_commands, manipulation_commands, creation_commands, batch_commands


class CommandsFactory:
    def __init__(self):
        self.__commands = {
            "new": creation_commands.NewCommand,
            "load": creation_commands.LoadCommand,
            "dup": creation_commands.DupCommand,
            "slice": manipulation_commands.SliceCommand,
            "replace": manipulation_commands.ReplaceCommand,
            "concat": manipulation_commands.ConcatCommand,
            "pair": manipulation_commands.PairCommand,
            "rename": management_commands.RenameCommand,
            "del": management_commands.DelCommand,
            "save": management_commands.SaveCommand,
            "len": analysis_commands.LenCommand,
            "find": analysis_commands.FindCommand,
            "count": analysis_commands.CountCommand,
            "findall": analysis_commands.FindallCommand,
            "batch": batch_commands.BatchCreationCommand,
            "run": batch_commands.RunBatchCommand,
            "batchlist": batch_commands.ListBatchCommand,
            "batchshow": batch_commands.ShowBatchCommand,
            "batchsave": batch_commands.SaveBatchCommand,
            "batchload": batch_commands.LoadBatchCommand,
            "list": control_commands.ListCommand,
            "quit": control_commands.QuitCommand
        }

    def get_command(self, command_name):
        if command_name not in self.__commands:
            return None
        return self.__commands[command_name]()
