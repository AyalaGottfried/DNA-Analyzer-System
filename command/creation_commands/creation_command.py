from command.command import Command
from data_base.dna_collection_manager import DnaCollectionManager


class CreationCommand(Command):
    def __init__(self):
        self.__dna_collection = DnaCollectionManager()

    def get_dna_collection(self):
        return self.__dna_collection

    def _save_sequence(self, args, new_name, dna_sequence, status):
        if len(args) < 2:
            sequence_name = new_name
        else:
            if args[1][0] != "@":
                raise Exception("Exception: sequence name does not start with @")
            sequence_name = args[1][1:]
        sequence = self.__dna_collection.save_sequence(sequence_name, dna_sequence, status)
        return sequence

