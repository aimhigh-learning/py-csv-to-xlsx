import os;
import sys;
# from reader.reader import *
# from reader.reader import _read, _readWrite
from customxlsxwriter.writer import _protectedWorkSheet
import pandas as pd
from datetime import datetime


def handler(event, context):
    ## Read the event 
    inputFile = event['filePath']
    template = event['template']

    if(inputFile == '' or template == ''):
        raise Exception('Sorry , inputFile and template as a request body can not be null or empty')

    print('Current timestamp before read_csv: ', datetime.now())
    new_dataFrame = pd.read_csv(inputFile)
    print('Current timestamp after read_csv: ', datetime.now())
    
    print('Current timestamp before to_excel: ', datetime.now())
    _protectedWorkSheet(new_dataFrame,'Data');
    print('Current timestamp after to_excel: ', datetime.now())



if __name__ == 'main':
    handler()