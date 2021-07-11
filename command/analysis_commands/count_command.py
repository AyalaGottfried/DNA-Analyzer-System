from command.analysis_commands.analysis_command import AnalysisCommand
from data_base.dna_sequence import DnaSequence


class CountCommand(AnalysisCommand):
    def __init__(self):
        super().__init__()

    def execute(self, *args):
        dna_to_find_in, dna_to_be_found = self.perform_analyze(args)
        return dna_to_find_in.count(dna_to_be_found)
