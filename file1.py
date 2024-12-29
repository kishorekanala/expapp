import csv 
import datetime
import pandas as pd

file_name="aa.csv"

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
    total_sum=0
    df=read_file(file_name)
    
    if amount in df.columns:
        print(f"Elements under '{amount}':")
        print(df[amount].to_string(index=False))
        print("------------")
        print("Number of amount enteries:",len(df))
    else:
        print(f"Column '{amount}' not found in the file.")

def print_amount_sum(amount):
    total_sum=0
    df=read_file(file_name)
    for row in range(len(df)):
        total_sum+=row
    print("-------------")
    print("The total amount spent:", float(total_sum))
    print("-------------")

def average_amount(amount):
    total_sum=0
    df=read_file(file_name)
    for row in range(len(df)):
        total_sum+=row
    average_amount=total_sum/(len(df))
    print("Average amount spent:",float(average_amount))




#print(storeoutflowdata(file_name))
#print_contents(file_name)
#print(read_file(file_name))
#print(print_table(file_name))
average_amount("Amount")
print_amount_sum("Amount")

    





