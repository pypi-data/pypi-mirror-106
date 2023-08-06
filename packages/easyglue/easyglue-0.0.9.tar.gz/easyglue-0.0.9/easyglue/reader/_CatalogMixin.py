from typing import Any

from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame

from easyglue.utils import reader_method, validate_qualified_name


class CatalogMixin:
    glue_context: GlueContext
    additional_options_dict: dict

    @reader_method
    def catalog(self, database_name: str, table_name: str, redshift_tmp_dir: str = "", transformation_ctx: str = "",
                push_down_predicate: str = "", catalog_id: int = None, **kwargs: Any) -> DynamicFrame:
        """
        Reads a dataset from Catalog by calling create_dynamic_frame.from_catalog with the right configuration
        :param self: Self reference to the EasyDynamicFrameReader class
        :param database_name: Name of the Data Catalog database containing the table
        :param table_name: Name of the Data Catalog table
        :param redshift_tmp_dir: Temporary path to be used when reading/writing from/to Redshift
        :param transformation_ctx: Glue transformation context
        :param push_down_predicate: S3 push down predicate to be applied
        :param catalog_id: Data Catalog ID containing the referenced database and table names
        :param kwargs: Keyword arguments
        :return: DynamicFrame representing the Data Catalog table
        """
        return self.glue_context.create_dynamic_frame_from_catalog(database=database_name,
                                                                   table_name=table_name,
                                                                   redshift_tmp_dir=redshift_tmp_dir,
                                                                   transformation_ctx=transformation_ctx,
                                                                   push_down_predicate=push_down_predicate,
                                                                   additional_options=self.additional_options_dict,
                                                                   catalog_id=catalog_id,
                                                                   kwargs=kwargs)

    @reader_method
    def table(self, qualified_name: str, redshift_tmp_dir: str = "", transformation_ctx: str = "",
              push_down_predicate: str = "", catalog_id: int = None, **kwargs: Any) -> DynamicFrame:
        """
        Reads a dataset from a Data Catalog qualified table name with the right configuration
        :param self: Self reference to the EasyDynamicFrameReader class
        :param qualified_name: Qualified name (database.table) of the table to read from
        :param redshift_tmp_dir: Temporary path to be used when reading/writing from/to Redshift
        :param transformation_ctx: Glue transformation context
        :param push_down_predicate: S3 push down predicate to be applied
        :param catalog_id: Data Catalog ID containing the referenced database and table names
        :param kwargs: Keyword arguments
        :return: DynamicFrame representing the Data Catalog table
        """
        database_name, table_name = validate_qualified_name(qualified_name)
        return self.glue_context.create_dynamic_frame_from_catalog(database=database_name,
                                                                   table_name=table_name,
                                                                   redshift_tmp_dir=redshift_tmp_dir,
                                                                   transformation_ctx=transformation_ctx,
                                                                   push_down_predicate=push_down_predicate,
                                                                   additional_options=self.additional_options_dict,
                                                                   catalog_id=catalog_id,
                                                                   kwargs=kwargs)
