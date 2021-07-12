from command.control_commands.control_command import ControlCommand

COMMANDS = {
    "new": "Creates a new sequence",
    "load": "Loads a sequence from a file",
    "dup": "Duplicates a sequence",
    "slice": "Slices a sequence by the given indexes",
    "replace": "Replaces in a sequence the nucleotides in the given indexes with the given nucleotides",
    "concat": "Concatenates sequences each to other",
    "pair": "Replaces each nucleotide in a sequence with its pair nucleotide",
    "rename": "Renames the name of a sequence to the new name",
    "del": "Deletes a sequence",
    "reenum": "Re-enumerates all the sequences so that their numbers are 1..n",
    "save": "Saves a sequence to a file",
    "len": "Prints the length of a sequence",
    "find": "Prints the index of the first appearance of the given sub-sequence within a sequence",
    "count": "Prints the number of instances of the given sub-sequence within a sequence",
    "findall": "Prints the indexes of all indices of the given sub-sequence within a sequence",
    "help": "Lists all the available commands",
    "list": "Shows all the sequences in the system, by order",
    "show": "Shows a sequence: Its ID, its name, its status and the sequence itself",
    "quit": "Exists the application",
    "batch": "Creates a new batch",
    "run": "Runs a batch",
    "batchlist": "Shows a list of all the batch names",
    "batchshow": "Shows the content of a batch",
    "batchsave": "Saves a batch to a file",
    "batchload": "Loads a batch from a file",
}


class HelpCommand(ControlCommand):
    def execute(self, *args):
        if len(args) == 0:
            return '\n'.join(COMMANDS.keys())
        try:
            return COMMANDS[args[0]]
        except KeyError:
            raise Exception("Exception: invalid command. Type help to see the available commands")
