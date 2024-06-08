import logging
from elasticsearch import Elasticsearch, helpers
from elasticsearch.client import IndicesClient

from schema import configurations

INDEX_NAME = "git-repo"

logging.basicConfig(level=logging.INFO)

class Seed():

    def __init__(self, server: Elasticsearch) -> None:
        self.es = server
        self.propigate()

    # define a function that will load a text file
    def get_data_from_text_file(self, filename):
        """the function will return a list of docs"""
        return [l for l in open(filename, encoding="utf8", errors='ignore')]

    def load_data(self):
        """
        1. read a json for data
        2. bulk insert data loop
        3. bulk insert leftover data from loop
        """
        i = 1 # counter for our list
        doc_list = [] # holds json objects 
        data = self.get_data_from_text_file("data.json")
        for line in data:
            doc_list += [line] # append

            if i % 1000 == 0: # when we reach limit insert
                helpers.bulk( self.es, doc_list, index = INDEX_NAME, doc_type = "_doc")
                i = 1
                doc_list.clear()
            else:
                i += 1

        helpers.bulk( self.es, doc_list, index = INDEX_NAME, doc_type = "_doc") # insert the leftover

    def create_index(self):
        """ create index if does not exists otherwise throws exception """
        client = IndicesClient(self.es)
        client.create(index=INDEX_NAME, body=configurations)

    def propigate(self):
        """keeps from reindexing and duplicate data"""
        try:
            self.create_index()
            self.load_data()
        except:
            logging.warning("Index already exists")
            pass