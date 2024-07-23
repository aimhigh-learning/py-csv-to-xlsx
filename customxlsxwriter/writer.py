import os
import xlsxwriter;
import pandas as pd;
from pandas import DataFrame;

def _protectedWorkSheet(df: DataFrame, sheet : str): 
    with pd.ExcelWriter('output.xlsx', engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name=sheet, index=False)
        worksheet = writer.sheets[sheet]
        worksheet.set_column('A:XDF', 30) ## Lock the columns ... and width is 40
        worksheet.protect();

if __name__ == 'main':
    print('Inside Xlsx writer module ...');