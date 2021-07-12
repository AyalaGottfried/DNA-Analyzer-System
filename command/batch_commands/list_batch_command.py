from command.batch_commands.batch_command import BatchCommand


class ListBatchCommand(BatchCommand):
    def __init__(self):
        super().__init__()

    def execute(self, *args):
        batches = self.get_batch_collection().get_all_batches_names()
        return '\t'.join(batches)
