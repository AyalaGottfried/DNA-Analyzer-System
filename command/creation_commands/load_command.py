from command.creation_commands.creation_command import CreationCommand
from data_base.dna_sequence import DnaSequence


class LoadCommand(CreationCommand):
    def __init__(self):
        super().__init__()

    def execute(self, *args):
        if len(args) == 0:
            raise Exception( "Exception: file name is required")
        file_name = args[0]
        if file_name.split(".")[-1] != "rawdna" or len(file_name.split(".")) < 2:
            raise Exception( "Exception: file extension is not supported")
        with open(file_name) as file:
            dna_sequence = file.readline()
        raise Exception( self._save_sequence(args, file_name, dna_sequence))
