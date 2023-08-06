from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame

from easyglue.writer._S3Mixin import S3Mixin
from easyglue.writer._CatalogMixin import CatalogMixin
from easyglue.writer._OthersMixin import OthersMixin
from easyglue.writer._JDBCMixin import JDBCMixin


class EasyDynamicFrameWriter(S3Mixin, CatalogMixin, OthersMixin, JDBCMixin):
    data_format = ""  # TODO implement this, with a save() method
    connection_options_dict = {}
    format_options_dict = {}
    additional_options_dict = {}

    def __init__(self, glue_context: GlueContext, dynamicframe: DynamicFrame):
        self.glue = glue_context
        self.dyf = dynamicframe

    def format_option(self, key: str, value: str):
        """
        Stores a format option for later use when reading
        :param key: Format option key
        :param value: Format option value
        :return: None
        """
        self.format_options_dict.update({key: value})
        return self

    def format_options(self, options: dict):
        """
        Stores a dictionary of format options for later use when reading
        :param options: Format options dictionary
        :return: None
        """
        self.format_options_dict = options
        return self

    def connection_option(self, key: str, value: str):
        """
        Stores a connection option for later use when reading
        :param key: Connection option key
        :param value: Connection option value
        :return: None
        """
        self.connection_options_dict.update({key: value})
        return self

    def connection_options(self, options: dict):
        """
        Stores a dictionary of connection options for later use when reading
        :param options: Connection options dictionary
        :return: None
        """
        self.connection_options_dict = options
        return self

    def additional_option(self, key: str, value: str):
        """
        Stores an additional option for later use when reading
        :param key: Additional option key
        :param value: Additional option value
        :return: None
        """
        self.additional_options_dict.update({key: value})
        return self

    def additional_options(self, options: dict):
        """
        Stores a dictionary of additional options for later use when reading
        :param options: Additional options dictionary
        :return: None
        """
        self.additional_options_dict = options
        return self

    def option(self, key: str, value: str):
        """
        Method added to comply with Spark's DataframeReader 'option' method. Routes the option as a connection option
        :param key: Connection option key
        :param value: Connection option value
        :return: None
        """
        return self.connection_option(key, value)

    def options(self, options: dict):
        """
        Method added to comply with Spark's DataframeReader 'options' method. Routes the options as connection options
        :param options: Connection options dictionary
        :return: None
        """
        return self.connection_options(options)
