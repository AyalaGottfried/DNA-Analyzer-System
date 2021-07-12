class BatchCollectionManager(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not BatchCollectionManager.__instance:
            BatchCollectionManager.__instance = object.__new__(cls)
            cls.__batches = {}
        return BatchCollectionManager.__instance

    def add_batch(self, batch_name, batch):
        if batch_name in self.__batches:
            raise Exception("Exception: this batch name is in use")
        self.__batches[batch_name] = batch

    def get_batch(self, batch_name):
        if batch_name not in self.__batches:
            raise Exception("Exception: this batch name is not exist")
        return self.__batches[batch_name]

    def get_all_batches_names(self):
        return self.__batches.keys()
