import csv 
import datetime
import pandas as pd

file_name="test.csv"

#reading file
def read_file(file_name):
    try:
        df=pd.read_csv(file_name)
        return df
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
    

def validate_date(date):
    try:
        datetime.datetime.strptime(date, '%d/%m/%Y')
    except ValueError:
        return 'Invalid date format'
    return None

#printing contents
def get_cashflowdata(file_name):
    df=read_file(file_name)
    if df is not None:
        rows = []
        for _, row in df.iterrows():
            row_data = {}
            for col_name in df.columns:
                row_data[col_name] = row[col_name]
            rows.append(row_data)
        return df, rows
    return None

    
df, rows = get_cashflowdata(file_name)
print(df)
#print(type(rows))
#for row in rows:
#    print(row)

#if rows:
#    for col_name in rows[0].keys():
#        print(f"{col_name}:")
#        for row in rows:
#            print(f"  {row[col_name]}")





