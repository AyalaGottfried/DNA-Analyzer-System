from command.command import Command
from data_base.dna_collection_manager import DnaCollectionManager


class PairCommand(Command):
    def __init__(self):
        self.__dna_collection = DnaCollectionManager()
        self.__pair_dict = {"T":"A", "A":"T", "C":"G", "G":"C"}

    def __get_pair(self, sequence):
        for i in range(len(sequence)):
            sequence[i] = self.__pair_dict[sequence[i]]
        return sequence

    def execute(self, *args):
        if len(args) == 0:
            return "Exception: sequence id or name is required"
        try:
            sequence_to_pair = self._get_sequence_identify(args[0], self.__dna_collection)
            if len(args) > 1:
                if args[1] != ":":
                    return "Exception: the third command is appears and not equal to :"
                if len(args) < 3:
                    return "Exception: new sequence name after : is required"
                if args[2][0] != "@":
                    return "Exception: sequence name does not start with @"
                new_sequence_name = args[2][1:]
                if new_sequence_name == "@":
                    new_sequence_name = self._get_next_name(self.__dna_collection, sequence_to_pair.get_name(), "p")
                dna_sequence = sequence_to_pair.get_dna_sequence().assignment()
                new_dna_sequence = self.__get_pair(dna_sequence)
                new_sequence = self.__dna_collection.save_sequence(new_sequence_name, new_dna_sequence)
                return "[{}] {}: {}".format(new_sequence.get_id(), new_sequence_name, new_dna_sequence)
            else:
                dna_sequence = sequence_to_pair.get_dna_sequence()
                new_dna_sequence = self.__get_pair(dna_sequence)
                sequence_to_pair.set_dna_sequence(new_dna_sequence)
                return "[{}] {}: {}".format(sequence_to_pair.get_id(), sequence_to_pair.get_name(),
                                            sequence_to_pair.get_dna_sequence())
        except Exception as e:
            return e.args[0]