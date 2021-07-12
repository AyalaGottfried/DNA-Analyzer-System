from command.control_commands.control_command import ControlCommand

DEFAULT_NUM_CHARS = 99


class ShowCommand(ControlCommand):
    def execute(self, *args):
        if len(args) == 0:
            raise Exception("Exception: sequence id or name is required")
        sequence_to_show = self.get_sequence(args[0])
        if len(args) > 1:
            try:
                num_chars = min(int(args[1]), len(sequence_to_show.get_dna_sequence()))
            except ValueError:
                raise Exception("Exception: invalid num chars")
        else:
            num_chars = min(DEFAULT_NUM_CHARS, len(sequence_to_show.get_dna_sequence()))
        lst_to_print = [
            "[{}] {} {}".format(sequence_to_show.get_id(), sequence_to_show.get_name(), sequence_to_show.get_status())]
        dna_to_print = sequence_to_show.get_dna_sequence()[:num_chars]
        for i in range(0, len(dna_to_print), 99):
            lst_to_print.append(str(dna_to_print[i:i+99]))
        return '\n'.join(lst_to_print)

