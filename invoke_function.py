import json
import boto3

def lambda_handler(event, context):
    # Create an AWS Lambda client
    lambda_client = boto3.client('lambda')

    # Specify the name of the Lambda function you want to invoke
    target_lambda_function_name = 'childlambda'

    # Specify the payload (input) for the target Lambda function
    payload = {'key': 'value'}

    # Invoke the Lambda function
    response = lambda_client.invoke(
        FunctionName = 'arn:aws:lambda:ap-south-1:361489220352:function:childlambda',
        InvocationType = 'RequestResponse',  # Can be 'Event' for asynchronous invocation
        Payload = json.dumps(payload)
    )

    # Handle the response from the invoked Lambda function
    result = json.loads(response['Payload'].read().decode('utf-8'))
    
    # Process the result as needed
    print(result)
    
    # Your remaining code logic goes here