import csv
import datetime

filename = 'test.csv'


def storeoutflowdatainDB(date, head, amt, desc):
    print('Storing data in DB')
    print(date)
    print(head)
    print(amt)
    print(desc)
    print('-------------------')


def read_csv1(filename):
    file = open(filename, 'r')
    csv_reader = csv.reader(file)
    return csv_reader

def print_outflowdata(date, head, amt, desc):
    print(date)
    print(head)
    print(amt)
    print(desc)
    print('-------------------')
    
def validate_date(date):
    try:
        datetime.datetime.strptime(date, '%d/%m/%Y')
    except ValueError:
        return 'Invalid date format'
    return None

csvcontents = read_csv1(filename)

#print(type(csvcontents))
for row in csvcontents:
    if csvcontents.line_num == 1:
        continue
    #print(type(row))
    date = row[0]
    head = row[1]
    amt = row[2]
    desc = row[3]
    print_outflowdata(date, head, amt, desc)
    err = validate_date(date)
    if err:
        print(err)
        break
    
    storeoutflowdatainDB(date, head, amt, desc)


read_csv1(filename)


    