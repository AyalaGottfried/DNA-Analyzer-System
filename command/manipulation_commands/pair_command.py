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
            return "Exception: sequence id or name is required"
        try:
            sequence_to_pair = self._get_sequence_identify(args[0], self.get_dna_collection())
            return self._validations(sequence_to_pair, args, 1, self.__get_pair(sequence_to_pair.get_dna_sequence().assignment()), self.__get_pair(sequence_to_pair.get_dna_sequence()))
        except Exception as e:
            return e.args[0]