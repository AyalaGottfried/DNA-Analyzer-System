from command.command import Command
from command.management_commands.management_command import ManagementCommand
from terminal.confirm import Confirm
from data_base.dna_collection_manager import DnaCollectionManager


class DelCommand(ManagementCommand):
    def __init__(self):
        super().__init__()
        self.__confirm = Confirm()

    def execute(self, *args):
        if len(args) == 0:
            return "Exception: sequence id or name is required"
        try:
            sequence_to_delete = self.get_sequence(args[0])
            user_confirm = self.__confirm.run(
                "Do you really want to delete {}: {}?".format(sequence_to_delete.get_name(),
                                                              sequence_to_delete.get_dna_sequence()))
            if user_confirm:
                self.get_dna_collection().remove_sequence(sequence_to_delete)
                return "Deleted: [{}] {}: {}".format(sequence_to_delete.get_id(), sequence_to_delete.get_name(),
                                                     sequence_to_delete.get_dna_sequence())
            return "Delete cancelled"
        except Exception as e:
            return e.args[0]
