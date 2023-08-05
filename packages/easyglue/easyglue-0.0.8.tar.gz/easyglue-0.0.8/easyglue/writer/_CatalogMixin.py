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
        self._write_to_catalog(database=database, table=table, redshift_tmp_dir=redshift_tmp_dir,
                               transformation_ctx=transformation_ctx, catalog_id=catalog_id, kwargs=kwargs)

    def table(self, qualified_name: str, redshift_tmp_dir: str = "", transformation_ctx: str = "",
              catalog_id: int = None, **kwargs: Any):
        database_name, table_name = validate_qualified_name(qualified_name)
        self._write_to_catalog(database=database_name, table=table_name, redshift_tmp_dir=redshift_tmp_dir,
                               transformation_ctx=transformation_ctx, catalog_id=catalog_id, kwargs=kwargs)
