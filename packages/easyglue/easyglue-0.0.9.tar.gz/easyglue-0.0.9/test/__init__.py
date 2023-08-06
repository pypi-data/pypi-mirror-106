import unittest

from pyspark.context import SparkContext
from awsglue.context import GlueContext


class EasyGlueTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.glue = GlueContext(SparkContext.getOrCreate())
