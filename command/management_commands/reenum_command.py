from command.management_commands.management_command import ManagementCommand


class ReenumCommand(ManagementCommand):
    def execute(self, *args):
        self.get_dna_collection().re_enumerates()
        return "The data was re-enumerated"
