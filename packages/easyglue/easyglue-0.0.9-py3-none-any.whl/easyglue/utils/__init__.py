import json
import re
import requests

import boto3

AWS_METADATA_ENDPOINT = 'http://169.254.169.254/latest/dynamic/instance-identity/document'


def get_current_region() -> str:
    response = requests.get(AWS_METADATA_ENDPOINT)
    return response.json().get('region')


secrets_client = boto3.client('secretsmanager', region_name=get_current_region())


def reader_method(func):
    """
    Decorator method, designed to be used in all methods that read a dataset and return it as a DynamicFrame. The
    decorator will call the wrapped method, then will clear all the options dictionaries so that options from a read
    don't reappear in the next read.
    :param func: Reader function
    :return: Result of the reader function
    """

    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        self.connection_options_dict.clear()
        self.format_options_dict.clear()
        self.additional_options_dict.clear()
        return result

    return wrapper


def writer_method(func):
    """
    Decorator method, designed to be used in all methods that write a dataset. The decorator will call the wrapped
    method, then will clear all the options dictionaries so that options from a write don't reappear in the next write.
    :param func: Writer function
    :return: Result of the writer function
    """
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        self.connection_options_dict.clear()
        self.format_options_dict.clear()
        self.additional_options_dict.clear()
        return result

    return wrapper


QUALIFIED_NAME_MATCH_REGEX = "[a-zA-Z0-9_]+\\.[a-zA-Z0-9_]+"
QUALIFIED_NAME_MATCH_CAPTURE = "[a-zA-Z0-9_]+"


def validate_qualified_name(qualified_name: str) -> tuple:
    """
    Validates that the provided qualified name is in the form of "database.table" and if so, returns each part
    :param qualified_name: Qualified name of the table
    :return: Database name, table name
    """
    if not re.match(QUALIFIED_NAME_MATCH_REGEX, qualified_name):
        raise ValueError('Provided table name is not in the form of "database.table"')
    else:
        matches = re.findall(QUALIFIED_NAME_MATCH_CAPTURE, qualified_name)
        return matches[0], matches[1]


SUPPORTED_JDBC_ENGINES = ["mysql", "aurora", "redshift", "oracle", "postgresql"]
SUPPORTED_MONGO_ENGINES = ["mongo"]


def get_connection_options_from_secret(secret_id: str, table_name: str = None) -> dict:
    """
    Reads and parses the arguments of an AWS Secrets Manager secret into the connection options needed by Glue to
    connect to a JDBC or MongoDB/DocumentDB source.
    :param secret_id: Name or ARN of the AWS Secrets Manager secret to get the connection parameters from
    :param table_name: (Optional) Name of the table to read from
    :return: Dictionary of connection options
    """
    value = secrets_client.get_secret_value(SecretId=secret_id)
    secret = json.loads(value.get('SecretString', {}))
    engine = secret.get('engine')
    if engine in SUPPORTED_JDBC_ENGINES:
        return _generate_conn_opts_jdbc(secret, table_name)
    elif engine in SUPPORTED_MONGO_ENGINES:
        return _generate_conn_opts_mongo(secret)
    else:
        raise ValueError(f"The engine parameter of the specified Secrets Manager secret either does not exist or is "
                         f"not supported. Supported values are "
                         f"{', '.join(SUPPORTED_JDBC_ENGINES + SUPPORTED_MONGO_ENGINES)}")


def _generate_conn_opts_jdbc(secret: dict, table_name: str = None) -> dict:
    """
    Parses the provided secret's parameters into the ones expected by JDBC Glue connection options
    :param secret: AWS Secrets Manager secret values in dictionary form
    :param table_name: (Optional) Name of the table to read from
    :return: Dictionary of connection options
    """
    return {
        "url": f"jdbc:{secret.get('engine')}://{secret.get('host')}:{secret.get('port')}/{secret.get('dbname')}",
        "dbtable": table_name,
        "user": secret.get('username'),
        "password": secret.get('password')
    }


def _generate_conn_opts_mongo(secret: dict) -> dict:
    """
    Parses the provided secret's parameters into the ones expected by MongoDB/DocumentDB Glue connection options
    :param secret: AWS Secrets Manager secret values in dictionary form
    :return: Dictionary of connection options
    """
    return {
        "uri": f"mongodb://{secret.get('host')}:{secret.get('port')}",
        "username": secret.get('username'),
        "password": secret.get('password')
    }
