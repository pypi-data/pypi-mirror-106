from typing import Any

from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame

from easyglue.utils import reader_method


class OthersMixin:
    glue_context: GlueContext
    connection_options_dict: dict

    @reader_method
    def _read_from_others(self, connection_type: str, table_name: str = None, database_name: str = None,
                          transformation_ctx: str = "", **kwargs: Any) -> DynamicFrame:
        """
        Reads from NoSQL sources such as DynamoDB or MongoDB by calling create_dynamic_frame.from_options with the
        right configuration options
        :param connection_type: Connection type, can be "dynamodb", "mongodb" or "documentdb"
        :param table_name: Name of the table/collection to read from
        :param database_name: Name of the database (if any) holding the table
        :param transformation_ctx: Glue transformation context
        :param kwargs: Keyword arguments
        :return: DynamicFrame representing the dataset
        """
        if connection_type == "dynamodb" and table_name:
            self.connection_options_dict['dynamodb.input.tableName'] = table_name
        if connection_type in ["mongodb", "documentdb"] and database_name and table_name:
            self.connection_options_dict['database'] = database_name
            self.connection_options_dict['collection'] = table_name

        return self.glue_context.create_dynamic_frame_from_options(connection_type=connection_type,
                                                                   connection_options=self.connection_options_dict,
                                                                   transformation_ctx=transformation_ctx,
                                                                   kwargs=kwargs
                                                                   )

    def dynamodb(self, table_name: str = None, transformation_ctx: str = None, **kwargs: Any) -> DynamicFrame:
        """
        Reads a DynamoDB dataset by calling _read_from_others with the right configuration
        :param table_name: Name of the DynamoDB table
        :param transformation_ctx: Glue transformation context
        :param kwargs: Keyword arguments
        :return: DynamicFrame representing the dataset
        """
        return self._read_from_others(connection_type="dynamodb", table_name=table_name,
                                      transformation_ctx=transformation_ctx, kwargs=kwargs)

    ddb = dynamodb  # Same method with an easier, shorter syntax

    def mongodb(self, database: str = None, collection: str = None, transformation_ctx: str = "",
                **kwargs: Any) -> DynamicFrame:
        """
        Reads a MongoDB dataset with calling _read_from_others with the right configuration
        :param database: Name of the MongoDB database
        :param collection: Name of the MongoDB collection
        :param transformation_ctx: Glue transformation context
        :param kwargs: Keyword arguments
        :return: DynamicFrame representing the dataset
        """
        return self._read_from_others(connection_type="mongodb", table_name=collection, database_name=database,
                                      transformation_ctx=transformation_ctx, kwargs=kwargs)

    def documentdb(self, database: str = None, collection: str = None, transformation_ctx: str = "",
                   **kwargs: Any) -> DynamicFrame:
        """
        Reads a DocumentDB dataset with calling _read_from_others with the right configuration
        :param database: Name of the DocumentDB database
        :param collection: Name of the DocumentDB collection
        :param transformation_ctx: Glue transformation context
        :param kwargs: Keyword arguments
        :return: DynamicFrame representing the dataset
        """
        return self._read_from_others(connection_type="documentdb", table_name=collection, database_name=database,
                                      transformation_ctx=transformation_ctx, kwargs=kwargs)
