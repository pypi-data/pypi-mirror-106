from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame

from easyglue.utils import writer_method


class OthersMixin:
    glue: GlueContext
    dyf: DynamicFrame

    connection_options_dict: dict

    @writer_method
    def _write_to_others(self, connection_type: str, table_name: str = None, database_name: str = None,
                         transformation_ctx: str = ""):
        """
        Internal method to write to DDB tables
        :param table_name: Name of the DynamoDB table
        :param transformation_ctx: Glue transformation context
        :return: None
        """
        if connection_type == "dynamodb" and table_name:
            self.connection_options_dict['dynamodb.output.tableName'] = table_name
        if connection_type in ["mongodb", "documentdb"] and database_name and table_name:
            self.connection_options_dict['database'] = database_name
            self.connection_options_dict['collection'] = table_name
        self.glue.write_dynamic_frame.from_options(frame=self.dyf,
                                                   connection_type=connection_type,
                                                   connection_options=self.connection_options_dict,
                                                   transformation_ctx=transformation_ctx
                                                   )

    def dynamodb(self, table_name: str, transformation_ctx: str = ""):
        """
        Write a DynamoDB dataset by calling _write_to_others with the right configuration
        :param table_name: Name of the DynamoDB table
        :param transformation_ctx: Glue transformation context
        :return: None
        """
        self._write_to_others(connection_type="dynamodb", table_name=table_name, transformation_ctx=transformation_ctx)

    ddb = dynamodb

    def mongodb(self, database: str = None, collection: str = None, transformation_ctx: str = ""):
        """
        Write a MongoDB dataset by calling _write_to_others with the right configuration
        :param database: Name of the database to write to
        :param collection: Name of the collection to write to
        :param transformation_ctx: Glue transformation context
        :return: None
        """
        self._write_to_others(connection_type="mongodb", table_name=collection, database_name=database,
                              transformation_ctx=transformation_ctx)

    def documentdb(self, database: str = None, collection: str = None, transformation_ctx: str = ""):
        """
        Write a DocumentDB dataset by calling _write_to_others with the right configuration
        :param database: Name of the database to write to
        :param collection: Name of the collection to write to
        :param transformation_ctx: Glue transformation context
        :return: None
        """
        self._write_to_others(connection_type="documentdb", table_name=collection, database_name=database,
                              transformation_ctx=transformation_ctx)
