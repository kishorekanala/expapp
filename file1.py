import csv 

file_name="text.csv"

#reading file
def read_file(file_name):
    file=open(file_name,"r")
    csv_reader=csv.reader(file)
    return csv_reader

rows=read_file(file_name)

#printing contents
def print_contents(file_name):
    for rows in rows:
        print(rows)

print_contents(file_name)



