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
def print_contents(file_name):
    df=read_file(file_name )
    if df is not None:
        for _, row in df.iterrows():
            print("\nRow Data:")
            for col_name in df.columns:
                print(f"{col_name}")
                print(f"{row[col_name]}")
    
           
    err= validate_date(row["Date"])
    if err:
        print("Error.")

def print_table(file_name):
    df=read_file(file_name)
    print(df.to_string(index=False, justify="center"))
        
def amount_sum(amount):
    df=read_file(file_name)

    
#print(storeoutflowdata(file_name))
#print_contents(file_name)
#print(read_file(file_name))
print(print_table(file_name))
    





