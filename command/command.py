class Command:
    def execute(self, *args):
        raise Exception("You must implement execute method in {}".format(self.__class__))

    def _get_sequence_identify(self, arg, dna_collection):
        if arg[0] != "#" and arg[0] != "@":
            raise Exception("Exception: sequence id or name does not start with # or with @")
        sequence_identify = arg[1:]
        if arg[0] == "#":
            try:
                return dna_collection.read_sequence_by_id(int(sequence_identify))
            except ValueError:
                raise Exception("Exception: invalid sequence id")
        return dna_collection.read_sequence_by_name(sequence_identify)

    def _get_next_name(self, dna_collection, old_name, prefix):
        copy = 1
        while dna_collection.is_name_exists("{}_{}{}".format(old_name, prefix, copy)):
            copy += 1
        return "{}_{}{}".format(old_name, prefix, copy)
