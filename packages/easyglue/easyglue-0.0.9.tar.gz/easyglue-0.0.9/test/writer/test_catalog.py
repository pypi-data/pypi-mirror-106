from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame

import easyglue
from test.writer import WriterTest
from test.test_utils import delete_all_s3_objects, glue_client
from test.test_utils.resources import DATABASE_NAME, TABLE_NAME, TABLE_BUCKET, TABLE_PREFIX, table_def


def create_sample_table():
    delete_sample_table()
    _create_table(DATABASE_NAME, table_def)


def delete_sample_table():
    if _table_exists(DATABASE_NAME, TABLE_NAME):
        _delete_table(DATABASE_NAME, TABLE_NAME)


def _table_exists(database_name: str, table_name: str):
    tables = glue_client.get_tables(DatabaseName=database_name).get('TableList', [])
    table_names = list(map(lambda t: t['Name'], tables))
    return table_name in table_names


def _create_table(database_name: str, table_input: dict):
    glue_client.create_table(DatabaseName=database_name, TableInput=table_input)


def _delete_table(database_name: str, table_name: str):
    glue_client.delete_table(DatabaseName=database_name, Name=table_name)


class TestCatalog(WriterTest):
    _glue: GlueContext
    dataset: DynamicFrame

    @classmethod
    def tearDown(cls) -> None:
        delete_all_s3_objects(TABLE_BUCKET, TABLE_PREFIX)

    @classmethod
    def setUpClass(cls) -> None:
        super(TestCatalog, cls).setUpClass()
        create_sample_table()

    @classmethod
    def tearDownClass(cls) -> None:
        delete_sample_table()

    def test_catalog(self):
        self.dataset.write.catalog(database=DATABASE_NAME, table=TABLE_NAME)
        data = self.glue.create_dynamic_frame. \
            from_catalog(database=DATABASE_NAME,
                         table_name=TABLE_NAME)
        self.assertEqual(1000, data.count())

    def test_table(self):
        self.dataset.write.table(f"{DATABASE_NAME}.{TABLE_NAME}")
        data = self.glue.create_dynamic_frame. \
            from_catalog(database=DATABASE_NAME,
                         table_name=TABLE_NAME)
        self.assertEqual(1000, data.count())
