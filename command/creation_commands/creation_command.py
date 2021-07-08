from command.command import Command
from data_base.dna_collection_manager import DnaCollectionManager
from data_base.dna_sequence import DnaSequence


class CreationCommand(Command):
    def __init__(self):
        self.__dna_collection = DnaCollectionManager()

    def _save_sequence(self, args, new_name, dna_sequence):
        if len(args) < 2:
            sequence_name = new_name
        else:
            if args[1][0] != "@":
                raise Exception("Exception: sequence name does not start with @")
            sequence_name = args[1][1:]
        sequence = self.__dna_collection.save_sequence(sequence_name, DnaSequence(dna_sequence))
        return "[{}] {}: {}".format(sequence.get_id(), sequence_name, dna_sequence)

