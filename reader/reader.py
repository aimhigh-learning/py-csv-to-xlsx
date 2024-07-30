import pandas as pd;

def _readFromS3(bucket: str , key : str , s3):
    response = s3.get_object(Bucket=bucket, Key=key)
    status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")
    if status == 200:
         print(f"Successful S3 get_object response. Status - {status} for key - {key}")
         books_df = pd.read_csv(response.get("Body"))
         return books_df
    else :
        print(f"Unsuccessful S3 get_object response. Status - {status}")
        raise Exception(f"Sorry some issue while fetching the object from s3 : -{status}")
    


if __name__ == 'main':
    print('Inside reader module ...')
    