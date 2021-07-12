from command.analysis_commands.analysis_command import AnalysisCommand


class CountCommand(AnalysisCommand):

    def execute(self, *args):
        dna_to_find_in, dna_to_be_found = self.perform_analyze(args)
        return dna_to_find_in.count(dna_to_be_found)
