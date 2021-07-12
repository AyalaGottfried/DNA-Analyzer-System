from command.analysis_commands.analysis_command import AnalysisCommand


class FindCommand(AnalysisCommand):
    def execute(self, *args):
        try:
            dna_to_find_in, dna_to_be_found = self.perform_analyze(args)
            return dna_to_find_in.index(dna_to_be_found)
        except ValueError:
            raise Exception("Exception: this sub-sequence is not exists in this sequence")
