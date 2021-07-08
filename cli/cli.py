from cmd import Cmd


class Cli:
    def run(self, *args):
        raise Exception("You must implement run method in {}".format(self.__class__))

    def _get_input(self, prefix):
        return input("> {} >>> ".format(prefix))

    def _print_to_user(self, message):
        print(message)

if __name__ == "__main__":
    Cmd().run()
