import warnings
with warnings.catch_warnings():
    warnings.simplefilter(action='ignore', category=FutureWarning)
    from arctic import Arctic, CHUNK_STORE
import logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)


class ArcticConnection(Arctic):

    def __init__(self, username, password, host='mongo', port='27017'):
        self.mongo_host = 'mongodb://{}:{}@{}:{}/?authSource=admin'.format(
            username, password, host, port)
        super().__init__(self.mongo_host)
        for library in ["EXTRACTED", "TRANSFORMED", "LOADED"]:
            if library not in self.list_libraries():
                logging.info(
                    'library {} not found in MongoDB instance - creating it'.format(library))
                self.initialize_library(library, CHUNK_STORE)

    def write(self, name, data, library, chunk_size='M'):
        self.get_library(library).write(name, data, chunk_size)

    def read(self, name, library, chunk_range=None):
        return self.get_library(library).read(name, chunk_range)
