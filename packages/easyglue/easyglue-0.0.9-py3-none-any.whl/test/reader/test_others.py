import unittest

import easyglue
from easyglue.utils import get_connection_options_from_secret
from test.reader import ReaderTest

documentdb_connection_options = get_connection_options_from_secret("documentdb")
documentdb_connection_options.update({"ssl": "true",
                                      "ssl.domain_match": "false",
                                      "partitioner": "MongoSamplePartitioner",
                                      "partitionerOptions.partitionSizeMB": "10",
                                      "partitionerOptions.partitionKey": "_id"})


class TestReadOthers(ReaderTest):

    def test_dynamodb(self):
        data = self.glue.read.dynamodb("easyglue")
        self.assertEqual(4, data.count())

    def test_ddb(self):
        data = self.glue.read.ddb("easyglue")
        self.assertEqual(4, data.count())

    def test_documentdb(self):
        print(documentdb_connection_options)
        data = self.glue.read.connection_options(documentdb_connection_options).\
            documentdb(database="test", collection="collection")
        self.assertEqual(1, data.count())

    # TODO test mongo


if __name__ == '__main__':
    unittest.main()
