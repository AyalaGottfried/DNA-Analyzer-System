from command.analysis_commands.analysis_command import AnalysisCommand
from data_base.dna_sequence import DnaSequence


class CountCommand(AnalysisCommand):
    def __init__(self):
        super().__init__()

    def execute(self, *args):
        return self.perform_analyze(args, "count")
