import json

import wikipedia


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    
    if "body" in event:
        event = json.loads(event["body"])
    entity = event["entity"]

    data = wikipedia.summary(entity,  sentences=1)
    
    print(f"Response from Wikipedia API: {data}")
    
    response = {
        "statusCode": "200",
        "headers": {
            "Contenet-type": "application/json"
            },
        "body": json.dumps(
            {
            "message": data
            }
        )
        }

    return response
