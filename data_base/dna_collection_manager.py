from data_base.sequence import Sequence


class DnaCollectionManager(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not DnaCollectionManager.__instance:
            DnaCollectionManager.__instance = object.__new__(cls)
            cls.__dna_sequences = []
            cls.__ids = {}
            cls.__names = {}
        return DnaCollectionManager.__instance

    def save_sequence(self, sequence_name, dna_sequence):
        if sequence_name not in self.__names:
            index = len(self.__dna_sequences)
            sequence = Sequence(sequence_name, dna_sequence)
            self.__dna_sequences.append(sequence)
            self.__ids[sequence.get_id()] = index
            self.__names[sequence.get_name()] = index
        else:
            index = self.__names[sequence_name]
            sequence = self.__dna_sequences[index]
            sequence.set_dna_sequence(dna_sequence)
        return sequence

    def remove_sequence(self, sequence):
        if sequence.get_id() not in self.__ids:
            raise Exception("Exception: the sequence is not exists")
        if len(self.__dna_sequences) == 1:
            self.__dna_sequences = []
            self.__ids = {}
            self.__names = {}
            return
        index = self.__ids[sequence.get_id()]
        last_id = self.__dna_sequences[-1].get_id()
        last_name = self.__dna_sequences[-1].get_name()
        self.__ids[last_id] = index
        self.__names[last_name] = index
        self.__dna_sequences[index] = self.__dna_sequences[-1]
        del self.__dna_sequences[-1]
        del self.__ids[sequence.get_id()]
        del self.__names[sequence.get_name()]

    def read_sequence_by_id(self, sequence_id):
        if sequence_id not in self.__ids:
            raise Exception("Exception: sequence not found")
        index = self.__ids[sequence_id]
        return self.__dna_sequences[index]

    def read_sequence_by_name(self, sequence_name):
        if sequence_name not in self.__names:
            raise Exception("Exception: sequence not found")
        index = self.__names[sequence_name]
        return self.__dna_sequences[index]

    def is_name_exists(self, sequence_name):
        return sequence_name in self.__names
