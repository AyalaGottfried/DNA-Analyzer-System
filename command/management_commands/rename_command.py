from command.management_commands.management_command import ManagementCommand


class RenameCommand(ManagementCommand):
    def execute(self, *args):
        if len(args) == 0:
            raise Exception("Exception: sequence id or name is required")
        if len(args) < 2:
            raise Exception("Exception: new name is required")
        sequence_to_rename = self.get_sequence(args[0])
        if args[1][0] != "@":
            raise Exception("Exception: sequence name does not start with @")
        sequence_to_rename.set_name(args[1][1:])
        return sequence_to_rename
