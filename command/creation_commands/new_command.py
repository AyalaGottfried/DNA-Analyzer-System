from command.creation_commands.creation_command import CreationCommand


class NewCommand(CreationCommand):
    __next_name_index = 0

    def __init__(self):
        super().__init__()

    def execute(self, *args):
        if len(args) == 0:
            return "Exception: dna sequence is required"
        dna_sequence = args[0]
        if len(args) < 2:
            NewCommand.__next_name_index += 1
        try:
            return self._save_sequence(args, "seq{}".format(NewCommand.__next_name_index), dna_sequence)
        except Exception as e:
            if len(args) < 2:
                NewCommand.__next_name_index -= 1
            return e.args[0]
