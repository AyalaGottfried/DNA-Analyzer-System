from command.manipulation_commands.manipulation_command import ManipulationCommand


class ReplaceCommand(ManipulationCommand):
    def __get_replace(self, index, args, sequence):
        for i in range(1, index, 2):
            sequence[int(args[i])] = args[i + 1]
        return sequence

    def execute(self, *args):
        if len(args) < 3:
            raise Exception("Exception: at least three argument is required")
        try:
            index = args.index(':')
        except ValueError:
            index = len(args)
        sequence_to_replace = self.get_sequence(args[0])
        old_dna = self.__get_replace(index, args, sequence_to_replace.get_dna_sequence())
        new_dna = self.__get_replace(index, args, sequence_to_replace.get_dna_sequence().assignment())
        return self.manipulate_sequence(sequence_to_replace, args, index, new_dna, old_dna, 'r')