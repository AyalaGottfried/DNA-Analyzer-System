from command.management_commands.management_command import ManagementCommand


class SaveCommand(ManagementCommand):
    def execute(self, *args):
        if len(args) == 0:
            return "Exception: sequence id or name is required"
        try:
            sequence_to_save = self.get_sequence(args[0])
            if len(args) > 1:
                file_name = args[1]
                if file_name.split(".")[-1] != "rawdna" or len(file_name.split(".")) < 2:
                    return "Exception: file extension is not supported"
            else:
                file_name = sequence_to_save.get_name()+".rawdna"
            with open(file_name, "w") as file:
                file.write(str(sequence_to_save.get_dna_sequence()))
            return "Saved to {}: [{}] {}: {}".format(file_name, sequence_to_save.get_id(), sequence_to_save.get_name(),
                                                     sequence_to_save.get_dna_sequence())
        except FileNotFoundError:
            return "Exception: file not found"
        except Exception as e:
            return e.args[0]
