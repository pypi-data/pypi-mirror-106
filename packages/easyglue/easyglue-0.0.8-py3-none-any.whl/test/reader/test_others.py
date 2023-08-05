import unittest

import easyglue
from test.reader import ReaderTest


class TestReadOthers(ReaderTest):

    def test_dynamodb(self):
        data = self.glue.read().dynamodb("easyglue")
        self.assertEqual(4, data.count())

    def test_ddb(self):
        data = self.glue.read().ddb("easyglue")
        self.assertEqual(4, data.count())


if __name__ == '__main__':
    unittest.main()
