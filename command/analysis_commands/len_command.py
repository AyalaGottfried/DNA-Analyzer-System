from command.analysis_commands.analysis_command import AnalysisCommand


class LenCommand(AnalysisCommand):
    def __init__(self):
        super().__init__()

    def execute(self, *args):
        if len(args) == 0:
            raise Exception( "Exception: sequence id or name is required")
        sequence_to_get_length = self._get_sequence_identify(args[0], self.get_dna_collection())
        return len(sequence_to_get_length.get_dna_sequence())
