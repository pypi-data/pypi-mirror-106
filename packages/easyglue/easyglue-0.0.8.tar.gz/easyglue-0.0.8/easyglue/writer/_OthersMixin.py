from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame

from easyglue.utils import writer_method


class OthersMixin:
    glue: GlueContext
    dyf: DynamicFrame

    connection_options_dict: dict

    @writer_method
    def _write_to_ddb(self, table_name: str, transformation_ctx: str = ""):
        """
        Internal method to write to DDB tables
        :param table_name: Name of the DynamoDB table
        :param transformation_ctx: Glue transformation context
        :return: None
        """
        self.connection_options_dict['dynamodb.output.tableName'] = table_name
        self.glue.write_dynamic_frame.from_options(frame=self.dyf,
                                                   connection_type="dynamodb",
                                                   connection_options=self.connection_options_dict,
                                                   transformation_ctx=transformation_ctx
                                                   )

    def dynamodb(self, table_name: str, transformation_ctx: str = ""):
        """
        Write a DynamoDB dataset by calling write_dynamic_frame_from_options with the right configuration
        :param table_name: Name of the DynamoDB table
        :param transformation_ctx: Glue transformation context
        :return: None
        """
        self._write_to_ddb(table_name=table_name, transformation_ctx=transformation_ctx)

    def ddb(self, table_name: str, transformation_ctx: str = ""):
        """
        Write a DynamoDB dataset by calling write_dynamic_frame_from_options with the right configuration
        :param table_name: Name of the DynamoDB table
        :param transformation_ctx: Glue transformation context
        :return: None
        """
        self._write_to_ddb(table_name=table_name, transformation_ctx=transformation_ctx)
