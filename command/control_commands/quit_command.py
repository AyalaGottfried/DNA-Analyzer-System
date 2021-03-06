from command.control_commands.control_command import ControlCommand
from terminal.confirm import Confirm


class QuitCommand(ControlCommand):
    def __init__(self):
        super().__init__()
        self.__confirm = Confirm()

    def execute(self, *args):
        sequences = self.get_all_sequences()
        modified_num = 0
        new_num = 0
        for seq in sequences:
            if seq.get_status() == "modified":
                modified_num += 1
            elif seq.get_status() == "new":
                new_num += 1
        if modified_num != 0 or new_num != 0:
            if modified_num == 0:
                message = "There are {} new sequences. Are you sure you want to quit?".format(new_num)
            elif new_num == 0:
                message = "There are {} modified sequences. Are you sure you want to quit?".format(modified_num)
            else:
                message = "There are {} modified and {} new sequences. Are you sure you want to quit?".format(
                    modified_num, new_num)
            user_confirm = self.__confirm.run(message)
            if not user_confirm:
                return "Quit cancelled"
        return "Thank you for using Dnalanyzer."
