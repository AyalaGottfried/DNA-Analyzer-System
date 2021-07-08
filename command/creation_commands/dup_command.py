from command.command import Command
from data_base.dna_collection_manager import DnaCollectionManager


class DupCommand(Command):
    def __init__(self):
        self.__dna_collection = DnaCollectionManager()

    def execute(self, *args):
        if len(args) == 0:
            return "Exception: sequence id or name is required"
        try:
            sequence_to_copy = self._get_sequence_identify(args[0], self.__dna_collection)
            if len(args) < 2:
                sequence_name = self._get_next_name(self.__dna_collection, sequence_to_copy.get_name(), "")
            else:
                if args[1][0] != "@":
                    return "Exception: sequence name does not start with @"
                sequence_name = args[1][1:]
            dna_sequence = sequence_to_copy.get_dna_sequence().assignment()
            sequence = self.__dna_collection.save_sequence(sequence_name, dna_sequence)
        except Exception as e:
            return e.args[0]
        return "[{}] {}: {}".format(sequence.get_id(), sequence_name, dna_sequence)

