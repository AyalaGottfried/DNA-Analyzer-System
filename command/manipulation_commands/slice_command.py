from command.command import Command
from command.manipulation_commands.manipulation_command import ManipulationCommand


class SliceCommand(ManipulationCommand):
    def __init__(self):
        super().__init__()

    def execute(self, *args):
        if len(args) < 3:
            return "Exception: at least three argument is required"
        try:
            sequence_to_slice = self._get_sequence_identify(args[0], self.__dna_collection)
            start_index = int(args[1])
            end_index = int(args[2])
            return self._validations(sequence_to_slice, args, 3, sequence_to_slice.get_dna_sequence().assignment()[start_index:end_index], sequence_to_slice.get_dna_sequence()[start_index:end_index])
        except Exception as e:
            return e.args[0]
