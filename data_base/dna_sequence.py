import re

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
        if value not in nucleotides:
            raise Exception("Exception: invalid sequence")
        self.__sequence = self.__sequence[:key] + value + self.__sequence[key + 1:]

    def __len__(self):
        return len(self.__sequence)

    def index(self, other_dna_sequence):
        return self.__sequence.index(other_dna_sequence.__sequence)

    def count(self, other_dna_sequence):
        matches = re.finditer("(?={})".format(other_dna_sequence.__sequence), self.__sequence)
        return len(list(matches))

    def find_all(self, other_dna_sequence):
        matches = re.finditer("(?={})".format(other_dna_sequence.__sequence), self.__sequence)
        return [match.start() for match in matches]
