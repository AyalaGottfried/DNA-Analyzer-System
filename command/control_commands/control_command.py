from command.command import Command
from data_base.dna_collection_manager import DnaCollectionManager


class ControlCommand(Command):
    def __init__(self):
        self.__dna_collection = DnaCollectionManager()

    def get_sequence(self, identify):
        return self._get_sequence_identify(identify, self.__dna_collection)

    def get_all_sequences(self):
        return self.__dna_collection.get_all_sequences()
