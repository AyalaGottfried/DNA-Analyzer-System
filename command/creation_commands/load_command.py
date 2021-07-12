from command.creation_commands.creation_command import CreationCommand


class LoadCommand(CreationCommand):
    def __init__(self):
        super().__init__()

    def execute(self, *args):
        if len(args) == 0:
            raise Exception( "Exception: file name is required")
        file_name = args[0]
        if file_name.split(".")[-1] != "rawdna" or len(file_name.split(".")) < 2:
            raise Exception("Exception: file extension is not supported")
        with open(file_name) as file:
            dna_sequence = file.readline()
        return self._save_sequence(args, ''.join(file_name.split('.')[:-1]), dna_sequence)
