import pandas as pd
from datetime import datetime
from pandas import DataFrame
import io

def _writeProtectedSheetToS3(df: DataFrame,bucket: str, key: str, sheetName : str, s3): 
    with io.BytesIO() as output:
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, sheet_name=sheetName, index=False)
            worksheet = writer.sheets[sheetName]
            worksheet.set_column('A:XDF', 30) ## Lock the columns ... and width is 40
            worksheet.protect();
        data = output.getvalue()
        s3.put_object(Bucket=bucket, Key=f"{key}.xlsx", Body=data)
    

if __name__ == 'main':
    print('Inside Xlsx writer module ...');