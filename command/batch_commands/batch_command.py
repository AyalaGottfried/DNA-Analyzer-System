from command.command import Command
from data_base.batch_collection_manager import BatchCollectionManager


class BatchCommand(Command):
    def __init__(self):
        self.__batch_collection = BatchCollectionManager()

    def get_batch_collection(self):
        return self.__batch_collection