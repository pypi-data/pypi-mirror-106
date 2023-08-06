from typing import Any

from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame

from easyglue.utils import writer_method


class JDBCMixin:
    glue: GlueContext
    dyf: DynamicFrame

    connection_options_dict: dict

    @writer_method
    def jdbc(self, connection_options: dict = None, transformation_ctx: str = "", **kwargs: Any):
        """
        Writes a dataset to a JDBC source by calling write_from_options with the right configuration
        :param connection_options: Connection options dictionary specifying JDBC parameters
        :param transformation_ctx: Glue transformation context
        :param kwargs: Keyword arguments
        :return: None
        """
        if connection_options:
            self.connection_options_dict = connection_options
        url = self.connection_options_dict.get('url')
        db_type = url.split(':')[1]
        self.glue.write_from_options(frame_or_dfc=self.dyf,
                                     connection_type=db_type,
                                     connection_options=self.connection_options_dict,
                                     transformation_ctx=transformation_ctx,
                                     kwargs=kwargs)
