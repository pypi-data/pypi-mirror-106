from typing import Any

from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame

from easyglue.utils import writer_method, validate_qualified_name


class CatalogMixin:
    glue: GlueContext
    dyf: DynamicFrame

    additional_options_dict: dict

    @writer_method
    def _write_to_catalog(self, database: str, table: str, redshift_tmp_dir: str = "", transformation_ctx: str = "",
                          catalog_id: int = None, **kwargs: Any):
        """
        Writes the DynamicFrame to catalog by invoking write_dynamic_frame.from_catalog with the right options
        :param database: Data catalog database to write to
        :param table: Data catalog table to write to
        :param redshift_tmp_dir: Redshift temporary path
        :param transformation_ctx: Glue transformation context
        :param catalog_id: Glue Data Catalog ID
        :param kwargs: Keyword arguments
        :return: None
        """
        self.glue.write_dynamic_frame.from_catalog(frame=self.dyf,
                                                   database=database,
                                                   table_name=table,
                                                   redshift_tmp_dir=redshift_tmp_dir,
                                                   transformation_ctx=transformation_ctx,
                                                   additional_options=self.additional_options_dict,
                                                   catalog_id=catalog_id,
                                                   kwargs=kwargs)

    def catalog(self, database: str, table: str, redshift_tmp_dir: str = "", transformation_ctx: str = "",
                catalog_id: int = None, **kwargs: Any):
        """
        Writes the DynamicFrame to catalog by invoking _write_to_catalog
        :param database: Data catalog database to write to
        :param table: Data catalog table to write to
        :param redshift_tmp_dir: Redshift temporary path
        :param transformation_ctx: Glue transformation context
        :param catalog_id: Glue Data Catalog ID
        :param kwargs: Keyword arguments
        :return: None
        """
        self._write_to_catalog(database=database, table=table, redshift_tmp_dir=redshift_tmp_dir,
                               transformation_ctx=transformation_ctx, catalog_id=catalog_id, kwargs=kwargs)

    def table(self, qualified_name: str, redshift_tmp_dir: str = "", transformation_ctx: str = "",
              catalog_id: int = None, **kwargs: Any):
        """
        Writes the DynamicFrame to catalog by invoking _write_to_catalog
        :param qualified_name: Qualified name (database.table) of the Data Catalog table to write to
        :param redshift_tmp_dir: Redshift temporary path
        :param transformation_ctx: Glue transformation context
        :param catalog_id: Glue Data Catalog ID
        :param kwargs: Keyword arguments
        :return: None
        """
        database_name, table_name = validate_qualified_name(qualified_name)
        self._write_to_catalog(database=database_name, table=table_name, redshift_tmp_dir=redshift_tmp_dir,
                               transformation_ctx=transformation_ctx, catalog_id=catalog_id, kwargs=kwargs)
