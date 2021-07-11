from command.management_commands.management_command import ManagementCommand


class SaveCommand(ManagementCommand):
    def execute(self, *args):
        if len(args) == 0:
            raise Exception( "Exception: sequence id or name is required")
        sequence_to_save = self.get_sequence(args[0])
        if len(args) > 1:
            file_name = args[1]
            if file_name.split(".")[-1] != "rawdna" or len(file_name.split(".")) < 2:
                raise Exception( "Exception: file extension is not supported")
        else:
            file_name = sequence_to_save.get_name()+".rawdna"
        with open(file_name, "w") as file:
            file.write(str(sequence_to_save.get_dna_sequence()))
        return "Saved to {}: [{}] {}: {}".format(file_name, sequence_to_save.get_id(), sequence_to_save.get_name(),
                                                 sequence_to_save.get_dna_sequence())
