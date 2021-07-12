from command import Command
from data_base.dna_collection_manager import DnaCollectionManager


class ControlCommand(Command):
    def __init__(self):
        self.__dna_collection = DnaCollectionManager()
