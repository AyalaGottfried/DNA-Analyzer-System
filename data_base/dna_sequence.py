nucleotides = ["A", "C", "G", "T"]


class DnaSequence:
    def __init__(self, sequence):
        if len(sequence) == 0:
            raise Exception("Exception: empty sequence")
        if any([let not in nucleotides for let in sequence]):
            raise Exception("Exception: invalid sequence")
        self.__sequence = sequence

    def get_sequence(self):
        return self.__sequence

    def set_sequence(self, sequence):
        if len(sequence) == 0:
            raise Exception("Exception: empty sequence")
        self.__sequence = sequence

    def insert(self, nucleotide, index):
        if nucleotide not in nucleotides:
            raise Exception("Exception: invalid sequence")
        self.__sequence = self.__sequence[:index] + nucleotide + self.__sequence[index:]

    def assignment(self):
        return DnaSequence(self.__sequence)

    def __str__(self):
        return self.__sequence

    def __eq__(self, other):
        return self.__sequence == other.get_sequence()

    def __ne__(self, other):
        return self.__sequence != other.get_sequence()

    def __getitem__(self, key):
        if isinstance(key, slice):
            return DnaSequence(self.__sequence[key])
        return self.__sequence[key]

    def __setitem__(self, key, value):
        self.__sequence = self.__sequence[:key]+value+self.__sequence[key+1:]

    def __len__(self):
        return len(self.__sequence)
