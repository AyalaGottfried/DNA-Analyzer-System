class Command:
    def execute(self, *args, **kwargs):
        pass

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

