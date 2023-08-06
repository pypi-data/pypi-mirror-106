import unittest

from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame

import easyglue
from test.test_utils import ddb_client
from test.writer import WriterTest

DDB_TABLE_NAME = "easyglue-test"


def create_sample_ddb_table():
    delete_sample_ddb_table()
    _create_ddb_table(DDB_TABLE_NAME)


def delete_sample_ddb_table():
    if _ddb_table_exists(DDB_TABLE_NAME):
        _delete_ddb_table(DDB_TABLE_NAME)


def _ddb_table_exists(table_name: str):
    return table_name in ddb_client.list_tables().get('TableNames', [])


def _create_ddb_table(table_name: str):
    key_schema = [{'AttributeName': 'id', 'KeyType': 'HASH'}]
    attribute_definitions = [{'AttributeName': 'id', 'AttributeType': 'S'}]
    provisioned_throughput = {'ReadCapacityUnits': 50, 'WriteCapacityUnits': 50}

    ddb_client.create_table(TableName=table_name, KeySchema=key_schema, AttributeDefinitions=attribute_definitions,
                            ProvisionedThroughput=provisioned_throughput)
    waiter = ddb_client.get_waiter('table_exists')
    waiter.wait(TableName=table_name)


def _delete_ddb_table(table_name: str):
    """
    Deletes a DDB table by the given name, then waits until it's deleted
    :param table_name: Name of the table to delete
    :return: None
    """
    ddb_client.delete_table(TableName=table_name)
    waiter = ddb_client.get_waiter('table_not_exists')
    waiter.wait(TableName=table_name)


class TestOthers(WriterTest):
    _glue: GlueContext
    dataset: DynamicFrame

    @classmethod
    def setUpClass(cls) -> None:
        super(TestOthers, cls).setUpClass()
        create_sample_ddb_table()

    @classmethod
    def tearDownClass(cls) -> None:
        delete_sample_ddb_table()

    @unittest.skip("DDB tests take very long to complete, only enable when necessary")
    def test_dynamodb(self):
        self.dataset.write.dynamodb(table_name=DDB_TABLE_NAME)
        data = self.glue.create_dynamic_frame. \
            from_options(connection_type="dynamodb", connection_options={"dynamodb.input.tableName": DDB_TABLE_NAME})
        self.assertEqual(1000, data.count())

    @unittest.skip("DDB tests take very long to complete, only enable when necessary")
    def test_ddb(self):
        self.dataset.write.ddb(table_name=DDB_TABLE_NAME)
        data = self.glue.create_dynamic_frame. \
            from_options(connection_type="dynamodb", connection_options={"dynamodb.input.tableName": DDB_TABLE_NAME})
        self.assertEqual(1000, data.count())
