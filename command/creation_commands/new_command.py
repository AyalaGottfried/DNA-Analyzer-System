from command.command import Command
from data_base.dna_collection_manager import DnaCollectionManager
from data_base.dna_sequence import DnaSequence


class NewCommand(Command):
    __next_name_index = 1

    def __init__(self):
        self.__data_manager = DnaCollectionManager()

    def execute(self, *args):
        if len(args) == 0:
            return "Exception: dna sequence is required"
        dna_sequence = args[0]
        if len(args) < 2:
            sequence_name = "seq{}".format(NewCommand.__next_name_index)
            NewCommand.__next_name_index += 1
        else:
            sequence_name = args[1]
            if sequence_name[0] != "@":
                return "Exception: sequence name does not start with @"
            sequence_name = sequence_name[1:]
        try:
            sequence = self.__data_manager.save_sequence(sequence_name, DnaSequence(dna_sequence))
        except Exception as e:
            if len(args) < 2:
                NewCommand.__next_name_index -= 1
            return e.args[0]
        return "[{}] {}: {}".format(sequence.get_id(), sequence_name, dna_sequence)
