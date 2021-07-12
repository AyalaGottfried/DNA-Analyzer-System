from command.batch_commands import BatchCommand


class LoadBatchCommand(BatchCommand):
    def execute(self, *args):
        if len(args) == 0:
            raise Exception("Exception: file name is required")
        file_name = args[0]
        if file_name.split(".")[-1] != "dnabatch" or len(file_name.split(".")) < 2:
            raise Exception("Exception: file extension is not supported")
        if len(args) > 1:
            if args[1] != ':':
                raise Exception("Exception: the third command is appears and not equal to :")
            if len(args) < 2:
                raise Exception("Exception: new batch name after : is required")
            if args[2][0] != "@":
                raise Exception("Exception: batch name does not start with @")
            batch_name = args[2][1:]
        else:
            batch_name = ''.join(file_name.split('.')[:-1])
        try:
            with open(file_name) as file:
                commands = file.readlines()
                commands = map(lambda c: c.replace('\n', ''), commands)
        except FileNotFoundError:
            raise Exception("Exception: the file is not exists")
        self.get_batch_collection().add_batch(batch_name, commands)
        return "Loaded from {}: batch {}".format(file_name, batch_name)
