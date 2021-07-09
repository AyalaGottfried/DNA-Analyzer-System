from command.creation_commands.creation_command import CreationCommand


class DupCommand(CreationCommand):
    def __init__(self):
        super().__init__()

    def execute(self, *args):
        if len(args) == 0:
            return "Exception: sequence id or name is required"
        try:
            sequence_to_copy = self._get_sequence_identify(args[0], self.get_dna_collection())
            dna_sequence = sequence_to_copy.get_dna_sequence().assignment()
            new_name = self._get_next_name(self.get_dna_collection(), sequence_to_copy.get_name(), "")
            return self._save_sequence(args, new_name, dna_sequence)
        except Exception as e:
            return e.args[0]
