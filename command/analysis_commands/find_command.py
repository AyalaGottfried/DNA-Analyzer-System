from command.analysis_commands.analysis_command import AnalysisCommand
from data_base.dna_sequence import DnaSequence


class FindCommand(AnalysisCommand):
    def __init__(self):
        super().__init__()

    def execute(self, *args):
        try:
            return self.perform_analyze(args, "find")
        except ValueError:
            raise Exception("Exception: this sub-sequence is not exists in this sequence")
