import os
from customxlsxwriter.writer import _writeProtectedSheetToS3
import pandas as pd
from datetime import datetime
import boto3
from reader.reader import _readFromS3
import json

ACCESS_KEY = os.environ.get('ACCESS_KEY');
SECRET_KEY = os.environ.get('SECRET_KEY');
BUCKET = os.environ.get('BUCKET');


def handler(event, context):
    ## Read the event 
    inputFile = event['filePath']
    template = event['template']

    if(inputFile == '' or template == ''):
        raise Exception('Sorry , inputFile and template as a request body can not be null or empty')

    try:

        ## Create the s3 session
        session = boto3.Session(aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY)
        
        ## Create s3 client as we need this only
        s3 = session.client('s3')

        print(f"Before load into dataframe - {datetime.now()}")
        ## Read the file in frame..
        df = _readFromS3(bucket=BUCKET, key=inputFile, s3=s3)

        print(f"After loaded into dataframe - {datetime.now()}")
        
        ## Write back to s3 with protected and xlsx
        print(f"Before write into dataframe & s3 - {datetime.now()}")
        if template == 'analytics':
            _writeProtectedSheetToS3(df,BUCKET, inputFile,'Data',s3=s3);
        else :
            raise Exception(f"Sorry this {template} template type is not yet implemented")
        
        print(f"Successfully pushed into s3 - {datetime.now()}")

        return {
            'status': 200,
            'body': {
                'message': json.dumps('Successfully converted !'),
                'output': f"{inputFile}.xlsx"
            }
        }
    except Exception as e:
        return {
            'status': 500,
            'body': {
                'message': f"{e}"
            }
        }


## Enable this for dev testing
# if __name__ == "__main__":
#     handler({filePath:'hello.txt', template:}) # type: ignore
    