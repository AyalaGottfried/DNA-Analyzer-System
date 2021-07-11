from command.analysis_commands.analysis_command import AnalysisCommand


class FindallCommand(AnalysisCommand):
    def __init__(self):
        super().__init__()

    def execute(self, *args):
        res = self.perform_analyze(args, "findall")
        if len(res) == 0:
            raise Exception("Exception: this sub-sequence is not exists in this sequence")
        return ' '.join(map(str, res))
