from command.command import Command
from terminal.confirm import Confirm
from data_base.dna_collection_manager import DnaCollectionManager


class DelCommand(Command):
    def __init__(self):
        self.__dna_collection = DnaCollectionManager()
        self.__confirm = Confirm()

    def execute(self, *args):
        if len(args) == 0:
            return "Exception: sequence id or name is required"
        try:
            sequence_to_delete = self._get_sequence_identify(args[0], self.__dna_collection)
            user_confirm = self.__confirm.run(
                "Do you really want to delete {}: {}?".format(sequence_to_delete.get_name(),
                                                              sequence_to_delete.get_dna_sequence()))
            if user_confirm:
                self.__dna_collection.remove_sequence(sequence_to_delete)
                return "Deleted: [{}] {}: {}".format(sequence_to_delete.get_id(), sequence_to_delete.get_name(),
                                                     sequence_to_delete.get_dna_sequence())
            return "Delete cancelled"
        except Exception as e:
            return e.args[0]
