#!/usr/bin/env python3
import os
from aws_cdk import core

from project_aws_cdk.data_lake.stack import DataLakeStack

app = core.App()
data_lake = DataLakeStack(app)

app.synth()
