from command.command import Command
from data_base.dna_collection_manager import DnaCollectionManager
from data_base.dna_sequence import DnaSequence


class AnalysisCommand(Command):
    def __init__(self):
        self.__dna_collection = DnaCollectionManager()

    def get_dna_collection(self):
        return self.__dna_collection

    def perform_analyze(self, args):
        if len(args) < 2:
            raise Exception("Exception: at least two arguments are required")
        sequence_to_find_in = self._get_sequence_identify(args[0], self.__dna_collection)
        if args[1][0] == '@' or args[1][0] == '#':
            sequence_to_be_found = self._get_sequence_identify(args[1], self.__dna_collection)
            dna_sequence_to_be_found = sequence_to_be_found.get_dna_sequence()
        else:
            dna_sequence_to_be_found = DnaSequence(args[1])
        return sequence_to_find_in.get_dna_sequence(), dna_sequence_to_be_found
