from command.creation_commands.creation_command import CreationCommand
from data_base.dna_sequence import DnaSequence


class NewCommand(CreationCommand):
    __next_name_index = 0

    def __init__(self):
        super().__init__()

    def execute(self, *args):
        if len(args) == 0:
            raise Exception("Exception: dna sequence is required")
        dna_sequence = args[0]
        last_name_index = NewCommand.__next_name_index
        if len(args) < 2:
            NewCommand.__next_name_index += 1
            while self.get_dna_collection().is_name_exists("seq{}".format(NewCommand.__next_name_index)):
                NewCommand.__next_name_index += 1
        try:
            return self._save_sequence(args, "seq{}".format(NewCommand.__next_name_index),DnaSequence(dna_sequence), "new")
        except Exception as e:
            if len(args) < 2:
                NewCommand.__next_name_index = last_name_index
            raise e
