class Cli:
    def __init__(self, prefix):
        self.__prefix = prefix

    def run(self, *args):
        raise Exception("You must implement run method in {}".format(self.__class__))

    def _get_input(self):
        return input("> {} >>> ".format(self.__prefix))

    def _print_to_user(self, message):
        print(message)

