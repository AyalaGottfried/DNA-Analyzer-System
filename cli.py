from command.commands_invoker import CommandsInvoker


class CLI:
    def __init__(self):
        self.__invoker = CommandsInvoker()

    def run(self):
        while True:
            command = input("> cmd >>> ")
            res = self.__manage_command(command)
            print(res)

    def __manage_command(self, command):
        args = command.split()
        res = self.__invoker.run_command(args[0], *args[1:])
        return res


if __name__ == "__main__":
    CLI().run()
