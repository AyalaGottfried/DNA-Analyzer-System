from command.batch_commands.batch_command import BatchCommand
from terminal.batch import Batch


class BatchCreationCommand(BatchCommand):
    def __init__(self):
        super().__init__()
        self.__batch = Batch()

    def execute(self, *args):
        if len(args) == 0:
            raise Exception("Exception: batch name is required")
        batch = self.__batch.run()
        self.get_batch_collection().add_batch(args[0], batch)
        return "Batch {} created".format(args[0])
