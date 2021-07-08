nucleotides = ["A", "C", "G", "T"]


class DnaSequence:
    def __init__(self, sequence):
        if any([let not in nucleotides for let in sequence]):
            raise Exception("Exception: invalid sequence")
        self.__sequence = sequence

    def get_sequence(self):
        return self.__sequence

    def set_sequence(self, sequence):
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
        return self.__sequence[key]

    def __len__(self):
        return len(self.__sequence)