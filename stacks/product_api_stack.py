from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
    CfnOutput
)
from constructs import Construct
import os

class ProductApiStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Lambda function for get_product
        lambda_fn = _lambda.Function(
            self, "GetProductFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="get_product.handler",
            code=_lambda.Code.from_asset(os.path.join(os.path.dirname(__file__), '../lambda_code')),
            environment={}
        )

        # API Gateway REST API
        api = apigateway.LambdaRestApi(
            self, "ProductsApi",
            handler=lambda_fn,
            proxy=False
        )

        # /products/{id} endpoint
        products = api.root.add_resource("products")
        product_id = products.add_resource("{id}")
        product_id.add_method("GET")

        # Output the API URL
        CfnOutput(
            self, "ProductsApiUrl",
            value=api.url,
            description="URL of the Products API"
        )
