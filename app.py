#!/usr/bin/env python3
import os
from aws_cdk import core

from project_aws_cdk.data_lake.stack import DataLakeStack
from project_aws_cdk.kinesis.stack  import KinesisStack
from project_aws_cdk.dms.stack import DmsStack
from project_aws_cdk.common_stack import CommonStack

app = core.App()
data_lake = DataLakeStack(app)
common_stack = CommonStack(app)
kinesis_stack = KinesisStack(
    app, data_lake_raw_bucket=data_lake.data_lake_raw_bucket
)
dms_stack = DmsStack(
    app,
    common_stack=common_stack,
    data_lake_raw_bucket=data_lake.data_lake_raw_bucket,
)

app.synth()
