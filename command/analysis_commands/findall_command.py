from command.analysis_commands.analysis_command import AnalysisCommand
from data_base.dna_sequence import DnaSequence


class FindallCommand(AnalysisCommand):
    def __init__(self):
        super().__init__()

    def execute(self, *args):
        if len(args) < 2:
            raise Exception("Exception: at least two arguments are required")
        sequence_to_find_in = self._get_sequence_identify(args[0], self.get_dna_collection())
        if args[1][0] == '@' or args[1][0] == '#':
            sequence_to_be_found = self._get_sequence_identify(args[1], self.get_dna_collection())
            dna_sequence_to_be_found = sequence_to_be_found.get_dna_sequence()
        else:
            dna_sequence_to_be_found = DnaSequence(args[1])
        res = sequence_to_find_in.get_dna_sequence().find_all(dna_sequence_to_be_found)
        if len(res) == 0:
            raise Exception("Exception: this sub-sequence is not exists in this sequence")
        return ' '.join(map(str, res))
