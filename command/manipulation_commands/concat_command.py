from command.manipulation_commands.manipulation_command import ManipulationCommand
from data_base.dna_sequence import DnaSequence


class ConcatCommand(ManipulationCommand):
    def __get_concat(self, index, args, sequence):
        for i in range(1, index):
            sequence += self.get_sequence(args[i]).get_dna_sequence()
        return sequence

    def execute(self, *args):
        if len(args) < 2:
            raise Exception("Exception: at least two sequence identifiers is required")
        try:
            index = args.index(':')
        except ValueError:
            index = len(args)
        sequence_to_concat = self.get_sequence(args[0])
        old_dna = self.__get_concat(index, args, sequence_to_concat.get_dna_sequence())
        new_dna = self.__get_concat(index, args, sequence_to_concat.get_dna_sequence().assignment())
        return self.manipulate_sequence(sequence_to_concat, args, index, new_dna, old_dna, 'c')