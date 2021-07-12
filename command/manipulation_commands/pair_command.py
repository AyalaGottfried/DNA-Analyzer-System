from command.manipulation_commands.manipulation_command import ManipulationCommand


class PairCommand(ManipulationCommand):
    def __init__(self):
        super().__init__()
        self.__pair_dict = {"T":"A", "A":"T", "C":"G", "G":"C"}

    def __get_pair(self, sequence):
        for i in range(len(sequence)):
            sequence[i] = self.__pair_dict[sequence[i]]
        return sequence

    def execute(self, *args):
        if len(args) == 0:
            raise Exception( "Exception: sequence id or name is required")
        sequence_to_pair = self._get_sequence_identify(args[0], self.get_dna_collection())
        old_dna = self.__get_pair(sequence_to_pair.get_dna_sequence())
        new_dna = self.__get_pair(sequence_to_pair.get_dna_sequence().assignment())
        return self.manipulate_sequence(sequence_to_pair, args, 1, new_dna, old_dna, 'p')
