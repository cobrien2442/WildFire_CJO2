import boto3
from datetime import datetime, timedelta

def lambda_handler(event, context):
    # steps ==> waiting for first email from firms
    # once format of initial data is found out ==> if csv, see how dynmo handles csv files. May need to break csv data up into 
    #json format -20240117
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
