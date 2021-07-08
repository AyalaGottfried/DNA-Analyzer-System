class Confirm:
    def run(self, message):
        print(message)
        print("Please confirm by 'y' or 'Y', or cancel by 'n' or 'N'.")
        while True:
            confirm = input("> confirm >>> ")
            if confirm == "y" or confirm == "Y":
                return True
            if confirm == "n" or confirm == "N":
                return False
            print("You have typed an invalid response. Please either confirm by 'y'/'Y', or cancel by 'n'/'N'.")
