from aws_cdk import (
    core as cdk,
    aws_s3 as s3,
    aws_cloudwatch as cloud_watch,
    aws_cloudwatch_actions as actions,
    aws_dynamodb as dynamo_db,
    aws_lambda as _lambda,
    aws_apigatewayv2 as api_gw,
)
from aws_cdk.aws_cloudwatch import TextWidget, SingleValueWidget, GraphWidget


class CdkStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

       






        #bucket = s3.Bucket(self, "MyFirstBucket",  versioned=True,)
        metric1 = cloud_watch.Metric(
                namespace="AWS/EC2",
                metric_name="CPUCreditUsage",
                dimensions_map={
                    "Name": "InstanceId",
                    "Value": "i-0c00ad8f568855a6e"
                }
            )
        metric2 = cloud_watch.Metric(
                namespace="AWS/EC2",
                metric_name="CPUCreditBalance",
                dimensions_map={
                    "Name": "InstanceId",
                    "Value": "i-0c00ad8f568855a6e"
                }
            )

        dashboard = cloud_watch.Dashboard(self,id= "CloudWatchDashBoard",)
        dashboard.add_widgets(cloud_watch.GraphWidget(
             title="CPUCreditBalance",

            left=[metric2],

           
            )
        )

 
