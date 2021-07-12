from command.batch_commands.batch_command import BatchCommand
from terminal.batch import Batch


class RunBatchCommand(BatchCommand):
    def __init__(self):
        super().__init__()
        self.__batch = Batch()

    def execute(self, *args):
        if len(args) == 0:
            raise Exception("Exception: batch name is required")
        batch = self.get_batch_collection().get_batch(args[0])
        results = []
        for command in batch:
            results.append(self.__batch.execute_command(command))
        return '\n'.join(map(str, results))