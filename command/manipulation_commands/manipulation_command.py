from command.command import Command
from data_base.dna_collection_manager import DnaCollectionManager


class ManipulationCommand(Command):
    def __init__(self):
        self.__dna_collection = DnaCollectionManager()

    def get_dna_collection(self):
        return self.__dna_collection

    def get_sequence(self, identify):
        return self._get_sequence_identify(identify, self.__dna_collection)

    def manipulate_sequence(self, sequence_to_manipulate, args, index, dna_for_new, dna_for_old, prefix):
        if len(args) > index:
            if args[index] != ":":
                raise Exception("Exception: the third command is appears and not equal to :")
            if len(args) < index + 2:
                raise Exception("Exception: new sequence name after : is required")
            if args[index + 1][0] != "@":
                raise Exception("Exception: sequence name does not start with @")
            new_sequence_name = args[index + 1][1:]
            if new_sequence_name == "@":
                new_sequence_name = self._get_next_name(self.__dna_collection, sequence_to_manipulate.get_name(), prefix)
            dna_sequence = dna_for_new
            status = "new"
        else:
            new_sequence_name = sequence_to_manipulate.get_name()
            dna_sequence = dna_for_old
            status = sequence_to_manipulate.get_status()
        new_sequence = self.__dna_collection.save_sequence(new_sequence_name, dna_sequence, status)
        return new_sequence
