from command.command import Command
from data_base.dna_collection_manager import DnaCollectionManager
from data_base.dna_sequence import DnaSequence


class LoadCommand(Command):
    def __init__(self):
        self.__dna_collection = DnaCollectionManager()

    def execute(self, *args):
        if len(args) == 0:
            return "Exception: file name is required"
        file_name = args[0]
        if file_name.split(".")[-1] != "rawdna" or len(file_name.split(".")) < 2:
            return "Exception: file extension is not supported"
        if len(args) < 2:
            sequence_name = file_name
        else:
            if args[1][0] != "@":
                return "Exception: sequence name does not start with @"
            sequence_name = args[1][1:]
        try:
            with open(file_name) as file:
                dna_sequence = file.readline()
                sequence = self.__dna_collection.save_sequence(sequence_name, DnaSequence(dna_sequence))
        except FileNotFoundError:
            return "Exception: file not found"
        except Exception as e:
            return e.args[0]
        return "[{}] {}: {}".format(sequence.get_id(), sequence_name, dna_sequence)
