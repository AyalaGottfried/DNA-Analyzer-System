from command import BatchCommand


class ShowBatchCommand(BatchCommand):
    def __init__(self):
        super().__init__()

    def execute(self, *args):
        if len(args) == 0:
            raise Exception("Exception: batch name is required")
        batch = self.get_batch_collection().get_batch(args[0])
        return '\n'.join(batch)
