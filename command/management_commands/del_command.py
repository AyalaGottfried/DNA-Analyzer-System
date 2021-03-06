from command.management_commands.management_command import ManagementCommand
from terminal.confirm import Confirm


class DelCommand(ManagementCommand):
    def __init__(self):
        super().__init__()
        self.__confirm = Confirm()

    def execute(self, *args):
        if len(args) == 0:
            raise Exception( "Exception: sequence id or name is required")
        sequence_to_delete = self.get_sequence(args[0])
        user_confirm = self.__confirm.run(
            "Do you really want to delete {}: {}?".format(sequence_to_delete.get_name(),
                                                          sequence_to_delete.get_dna_sequence()))
        if user_confirm:
            self.get_dna_collection().remove_sequence(sequence_to_delete)
            return "Deleted: {}".format(sequence_to_delete)
        return "Delete cancelled"
