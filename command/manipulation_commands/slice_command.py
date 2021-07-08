from command.command import Command
from data_base.dna_collection_manager import DnaCollectionManager


class SliceCommand(Command):
    def __init__(self):
        self.__dna_collection = DnaCollectionManager()

    def execute(self, *args):
        if len(args) < 3:
            return "Exception: at least three argument is required"
        try:
            sequence_to_slice = self._get_sequence_identify(args[0], self.__dna_collection)
            start_index = int(args[1])
            end_index = int(args[2])
            if len(args) > 3:
                if args[3] != ":":
                    return "Exception: the third command is appears and not equal to :"
                if len(args) < 5:
                    return "Exception: new sequence name after : is required"
                if args[4][0] != "@":
                    return "Exception: sequence name does not start with @"
                new_sequence_name = args[4][1:]
                if new_sequence_name == "@":
                    copy = 1
                    while self.__dna_collection.is_name_exists("{}_s{}".format(sequence_to_slice.get_name(), copy)):
                        copy += 1
                    new_sequence_name = "{}_s{}".format(sequence_to_slice.get_name(), copy)
                dna_sequence = sequence_to_slice.get_dna_sequence().assignment()
                dna_sequence = dna_sequence[start_index:end_index]
                new_sequence = self.__dna_collection.save_sequence(new_sequence_name, dna_sequence)
                return "[{}] {}: {}".format(new_sequence.get_id(), new_sequence_name, dna_sequence)
            else:
                sequence_to_slice.set_dna_sequence(sequence_to_slice.get_dna_sequence()[start_index:end_index])
                return "[{}] {}: {}".format(sequence_to_slice.get_id(), sequence_to_slice.get_name(),
                                            sequence_to_slice.get_dna_sequence())

        except Exception as e:
            return e.args[0]
