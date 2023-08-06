import unittest

from pyspark.sql.types import *

import easyglue
from test.reader import ReaderTest


class TestRDDRead(ReaderTest):

    @classmethod
    def setUpClass(cls) -> None:
        super(ReaderTest, cls).setUpClass()
        cls.sc = cls.glue.sparkSession.sparkContext

    def test_rdd(self):
        data = [["Mark,", 1], ["Anne", 2], ["Carlos", 3], ["Ghada", 4], ["Mikhail", 5]]
        rdd = self.sc.parallelize(data)

        schema_string = "name id"
        fields = [StructField(field_name, StringType(), True) for field_name in schema_string.split()]
        schema = StructType(fields)

        dyf = self.glue.read.rdd(rdd, "test_rdd", schema)
        self.assertEqual(5, dyf.count())


if __name__ == '__main__':
    unittest.main()
