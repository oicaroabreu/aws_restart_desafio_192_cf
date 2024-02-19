import aws_cdk as core
import aws_cdk.assertions as assertions

from desafio_192_cf.desafio_192_cf_stack import Desafio192CfStack

# example tests. To run these tests, uncomment this file along with the example
# resource in desafio_192_cf/desafio_192_cf_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Desafio192CfStack(app, "desafio-192-cf")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
