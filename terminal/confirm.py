from terminal.cli import Cli


class Confirm(Cli):
    def __init__(self):
        super().__init__("confirm")

    def run(self, message):
        self._print_to_user(message)
        self._print_to_user("Please confirm by 'y' or 'Y', or cancel by 'n' or 'N'.")
        while True:
            confirm = self._get_input()
            if confirm == "y" or confirm == "Y":
                return True
            if confirm == "n" or confirm == "N":
                return False
            self._print_to_user(
                "You have typed an invalid response. Please either confirm by 'y'/'Y', or cancel by 'n'/'N'.")
