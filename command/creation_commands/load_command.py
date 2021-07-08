from command.creation_commands.creation_command import CreationCommand
from data_base.dna_sequence import DnaSequence


class LoadCommand(CreationCommand):
    def __init__(self):
        super().__init__()

    def execute(self, *args):
        if len(args) == 0:
            return "Exception: file name is required"
        file_name = args[0]
        if file_name.split(".")[-1] != "rawdna" or len(file_name.split(".")) < 2:
            return "Exception: file extension is not supported"
        try:
            with open(file_name) as file:
                dna_sequence = file.readline()
            return self._save_sequence(args, file_name, DnaSequence(dna_sequence))
        except FileNotFoundError:
            return "Exception: file not found"
        except Exception as e:
            return e.args[0]
