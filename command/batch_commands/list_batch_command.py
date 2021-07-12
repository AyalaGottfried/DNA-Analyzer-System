from command.batch_commands.batch_command import BatchCommand


class ListBatchCommand(BatchCommand):
    def execute(self, *args):
        batches = self.get_batch_collection().get_all_batches_names()
        return '\n'.join(batches)
