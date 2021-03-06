from command.batch_commands import BatchCommand


class SaveBatchCommand(BatchCommand):
    def execute(self, *args):
        if len(args) == 0:
            raise Exception("Exception: batch name is required")
        if len(args) > 2:
            file_name = "{}.dnabatch".format(args[2])
        else:
            file_name = "{}.dnabatch".format(args[0])
        batch_to_save = self.get_batch_collection().get_batch(args[0])
        with open(file_name, "w") as file:
            file.write('\n'.join(batch_to_save))
        return "Saved to {}: batch {}".format(file_name, args[0])
