import unittest

from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame

import easyglue
from test.writer import WriterTest


class TestS3Read(WriterTest):
    _glue: GlueContext
    dataset: DynamicFrame

    def test_no_params(self):
        self.assertRaises(ValueError, self.dataset.write.csv, "")

    def test_validate_mandatory_parameters(self):
        self.assertRaises(ValueError, self.dataset.write._validate_mandatory_parameters, '', '')
        self.assertRaises(ValueError, self.dataset.write._validate_mandatory_parameters, 'a', '')
        self.assertRaises(ValueError, self.dataset.write._validate_mandatory_parameters, '', 'a')

    def test_csv(self):
        output_path = "s3://bertolb/test/easyglue/outputs/csv/"
        self.dataset.write.csv(output_path)
        data = self.glue.create_dynamic_frame. \
            from_options(connection_type="s3",
                         connection_options={"paths": [output_path]},
                         format="csv",
                         format_options={"withHeader": True})
        self.assertEqual(1000, data.count())

    def test_json(self):
        output_path = "s3://bertolb/test/easyglue/outputs/json/"
        self.dataset.write.json(output_path)
        data = self.glue.create_dynamic_frame. \
            from_options(connection_type="s3",
                         connection_options={"paths": [output_path]},
                         format="json")
        self.assertEqual(1000, data.count())

    def test_avro(self):
        output_path = "s3://bertolb/test/easyglue/outputs/avro/"
        self.dataset.write.avro(output_path)
        data = self.glue.create_dynamic_frame. \
            from_options(connection_type="s3",
                         connection_options={"paths": [output_path]},
                         format="avro")
        self.assertEqual(1000, data.count())

    def test_orc(self):
        output_path = "s3://bertolb/test/easyglue/outputs/orc/"
        self.dataset.write.orc(output_path)
        data = self.glue.create_dynamic_frame. \
            from_options(connection_type="s3",
                         connection_options={"paths": [output_path]},
                         format="orc")
        self.assertEqual(1000, data.count())

    def test_parquet(self):
        output_path = "s3://bertolb/test/easyglue/outputs/parquet/"
        self.dataset.write.parquet(output_path)
        data = self.glue.create_dynamic_frame. \
            from_options(connection_type="s3",
                         connection_options={"paths": [output_path]},
                         format="parquet")
        self.assertEqual(1000, data.count())

    def test_glueparquet(self):
        output_path = "s3://bertolb/test/easyglue/outputs/glueparquet/"
        self.dataset.write.glueparquet(output_path)
        data = self.glue.create_dynamic_frame. \
            from_options(connection_type="s3",
                         connection_options={"paths": [output_path]},
                         format="parquet")
        self.assertEqual(1000, data.count())


if __name__ == '__main__':
    unittest.main()
