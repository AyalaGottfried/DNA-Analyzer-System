from command.control_commands.control_command import ControlCommand


class ListCommand(ControlCommand):
    def __init__(self):
        super().__init__()
        self.__status_dic = {"new": 'o', "up to date": '-', "modified": '*'}

    def execute(self, *args):
        sequences = self.get_all_sequences()
        lst = []
        for seq in sequences:
            lst.append("{} {}".format(self.__status_dic[seq.get_status()], seq))
        return '\n'.join(lst)
