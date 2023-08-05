from easyglue.utils import writer_method

from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame


class S3Mixin:
    glue: GlueContext
    dyf: DynamicFrame

    data_format: str
    connection_options_dict: dict
    format_options_dict: dict

    @writer_method
    def _write_to_s3(self, path: str, data_format: str, transformation_ctx: str = ""):
        self._validate_mandatory_parameters(path, data_format)
        self.glue.write_dynamic_frame.from_options(frame=self.dyf,
                                                   connection_type="s3",
                                                   connection_options=self.connection_options_dict,
                                                   format=self.data_format,
                                                   format_options=self.format_options_dict,
                                                   transformation_ctx=transformation_ctx)

    def _validate_mandatory_parameters(self, path: str, data_format: str):
        self.connection_options_dict['path'] = path
        self.data_format = data_format
        if not self.connection_options_dict.get('path'):
            raise ValueError(f'S3 path was not provided')
        if not self.data_format:
            raise ValueError(f'Data format was not provided')

    def csv(self, path: str, transformation_ctx: str = ""):
        self._write_to_s3(path=path, data_format="csv", transformation_ctx=transformation_ctx)

    def json(self, path: str, transformation_ctx: str = ""):
        self._write_to_s3(path=path, data_format="json", transformation_ctx=transformation_ctx)

    def avro(self, path: str, transformation_ctx: str = ""):
        self._write_to_s3(path=path, data_format="avro", transformation_ctx=transformation_ctx)

    def orc(self, path: str, transformation_ctx: str = ""):
        self._write_to_s3(path=path, data_format="orc", transformation_ctx=transformation_ctx)

    def parquet(self, path: str, transformation_ctx: str = ""):
        self._write_to_s3(path=path, data_format="parquet", transformation_ctx=transformation_ctx)

    def glueparquet(self, path: str, transformation_ctx: str = ""):
        self._write_to_s3(path=path, data_format="glueparquet", transformation_ctx=transformation_ctx)
