from awsglue.context import GlueContext

from easyglue.utils import reader_method, get_connection_options_from_secret


class JDBCMixin:
    glue_context: GlueContext
    connection_options_dict: dict

    @reader_method
    def _read_from_jdbc(self, connection_type: str, transformation_ctx: str = "", push_down_predicate: str = ""):
        """
        Reads a dataset from a JDBC source by calling create_dynamic_frame.from_options with the right configuration
        :param connection_type: Connection type (database engine)
        :param transformation_ctx: Glue transformation context
        :param push_down_predicate: SQL pushdown predicate
        :return: DynamicFrame representing the JDBC table
        """
        return self.glue_context.create_dynamic_frame.from_options(connection_type=connection_type,
                                                                   connection_options=self.connection_options_dict,
                                                                   transformation_ctx=transformation_ctx,
                                                                   push_down_predicate=push_down_predicate)

    def jdbc(self, connection_options: dict = None, transformation_ctx: str = "", push_down_predicate: str = ""):
        """
        Reads a dataset from a JDBC source by calling _read_from_jdbc with the right configuration
        :param connection_options: Connection options dictionary specifying JDBC parameters
        :param transformation_ctx: Glue transformation context
        :param push_down_predicate: Push down predicate to be applied
        :return: DynamicFrame representing the JDBC table
        """
        if connection_options:
            self.connection_options_dict = connection_options
        url = self.connection_options_dict.get('url')
        db_type = url.split(':')[1]

        return self._read_from_jdbc(connection_type=db_type, transformation_ctx=transformation_ctx,
                                    push_down_predicate=push_down_predicate)

    def secret(self, table: str, secret: str, transformation_ctx: str = "", push_down_predicate: str = ""):
        """
        Reads a dataset from a JDBC source by getting the connection parameters from an AWS Secrets Manager secret
        :param table: Name of the JDBC table to read from
        :param secret: AWS Secrets Manager secret
        :param transformation_ctx: Glue transformation context
        :param push_down_predicate: SQL pushdown predicate
        :return: DynamicFrame representing the JDBC table
        """
        self.connection_options_dict = get_connection_options_from_secret(secret, table)
        url = self.connection_options_dict.get('url')
        db_type = url.split(':')[1]
        return self._read_from_jdbc(connection_type=db_type, transformation_ctx=transformation_ctx,
                                    push_down_predicate=push_down_predicate)
