import os;
import csv;
import sys;

def _read(file: str):
    with open(file, newline='') as f:
        reader = csv.reader(f)
        try:
            for row in reader:
                print(row)
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(file, reader.line_num, e))
    


def _readWrite(file: str, worksheet):
    with open(file, newline='') as f:
        reader = csv.reader(f)
        try:
            for row_num,row in enumerate(reader):
                worksheet.write_row(row_num,0,row); ## Write a row
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(file, reader.line_num, e))

if __name__ == 'main':
    print('Inside reader module ...')
    _read();