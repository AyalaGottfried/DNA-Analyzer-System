from command.analysis_commands.analysis_command import AnalysisCommand


class FindallCommand(AnalysisCommand):
    def __init__(self):
        super().__init__()

    def execute(self, *args):
        dna_to_find_in, dna_to_be_found = self.perform_analyze(args)
        res = dna_to_find_in.find_all(dna_to_be_found)
        if len(res) == 0:
            raise Exception("Exception: this sub-sequence is not exists in this sequence")
        return ' '.join(map(str, res))
