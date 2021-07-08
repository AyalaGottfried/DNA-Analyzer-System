from command.command import Command
from data_base.dna_collection_manager import DnaCollectionManager


class DupCommand(Command):
    def __init__(self):
        self.__data_manager = DnaCollectionManager()

    def execute(self, *args):
        if len(args) == 0:
            return "Exception: sequence id or name is required"
        if args[0][0] != "#" and args[0][0] != "@":
            return "Exception: sequence or name id does not start with # or with @"
        old_sequence_id = args[0][1:]
        try:
            if args[0][0] == "#":
                sequence_to_copy = self.__data_manager.read_sequence_by_id(int(old_sequence_id))
            else:
                sequence_to_copy = self.__data_manager.read_sequence_by_name(old_sequence_id)
            if len(args) < 2:
                copy = 1
                while self.__data_manager.is_name_exists("{}_{}".format(sequence_to_copy.get_name(), copy)):
                    copy += 1
                sequence_name = "{}_{}".format(sequence_to_copy.get_name(), copy)
            else:
                if args[1][0] != "@":
                    return "Exception: sequence name does not start with @"
                sequence_name = args[1][1:]
            dna_sequence = sequence_to_copy.get_dna_sequence().assignment()
            sequence = self.__data_manager.save_sequence(sequence_name, dna_sequence)
        except Exception as e:
            return e.args[0]
        return "[{}] {}: {}".format(sequence.get_id(), sequence_name, dna_sequence)

