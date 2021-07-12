from command.manipulation_commands.manipulation_command import ManipulationCommand


class SliceCommand(ManipulationCommand):
    def __init__(self):
        super().__init__()

    def execute(self, *args):
        if len(args) < 3:
            raise Exception( "Exception: at least three argument is required")
        sequence_to_slice = self.get_sequence(args[0])
        start_index = int(args[1])
        end_index = int(args[2])
        return self.manipulate_sequence(sequence_to_slice, args, 3, sequence_to_slice.get_dna_sequence().assignment()[start_index:end_index], sequence_to_slice.get_dna_sequence()[start_index:end_index], 's')

