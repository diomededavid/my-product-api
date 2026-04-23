from aws_cdk import App, Environment
from stacks.product_api_stack import ProductApiStack

app = App()

# Get region and account from context variables or use defaults
region = app.node.try_get_context("region") or "us-east-1"
account = app.node.try_get_context("account") or "123456789012"

ProductApiStack(
    app,
    "ProductApiStack",
    env=Environment(account=account, region=region)
)
app.synth()
