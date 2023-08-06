from easyglue.reader import EasyDynamicFrameReader
from easyglue.writer import EasyDynamicFrameWriter

from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame


@property
def read(self):  # Have to add self since this will become a method
    return EasyDynamicFrameReader(glue_context=self)


@property
def write(self):
    return EasyDynamicFrameWriter(glue_context=self.glue_ctx, dynamicframe=self)


setattr(GlueContext, 'read', read)
setattr(DynamicFrame, 'write', write)
