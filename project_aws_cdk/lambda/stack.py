from aws_cdk import core
from aws_cdk import (
    aws_iam as iam,
    aws_lambda as aws_lambda,
)

from project_aws_cdk.data_lake.base import BaseDataLakeBucket
from project_aws_cdk.active_environment import active_environment

class RawLambdaRole:
    def __init__(self, scope: core.Construct,data_lake_raw_bucket: BaseDataLakeBucket, **kwargs) -> None:


    def add_policy(self):


class LambdaStack(core.stack):
    