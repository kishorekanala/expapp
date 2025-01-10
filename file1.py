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


# Donot print the total within the function. return the total, 
# call the function and print it outside function 
def amount_sum(amount):
    df=read_file(file_name)
    
    if amount in df.columns:
        print(f"Elements under '{amount}':")
        print(df[amount].to_string(index=False))
        print("------------")
        print("Number of amount enteries:",len(df))
    else:
        print(f"Column '{amount}' not found in the file.")

# Donot print the total within the function. return the total, 
# call the function and print it outside function
def print_amount_sum(amount):
    total_sum=0
    df=read_file(file_name)
    total_sum=df["Amount"].sum()
    print("-------------")
    print("The total amount spent:", float(total_sum))
    print("-------------")


# Donot print the average amount within the function. return the average amount, 
# call the function and print it outside function
def total_average_amount(head):
    total_sum=0
    df=read_file(file_name)
    for i in head:
        for j in head[i]:
            total_sum=df[i][j].sum()
    average_amount=total_sum/(len(df))
    print("Average amount spent:",float(average_amount))


# Donot print the total amount per head within the function. return the total amount per head, 
# call the function and print it outside function
def print_only_headandamount(head,amount):
    df=read_file(file_name)
    selected_columns=df[["Head","Amount"]]
    print("Selected Columns:")
    print(selected_columns)
    head_list=list(df["Head"])
    amount_list=list(df["Amount"])
    together=dict(zip(head_list,amount_list))
    #print("Head List:\n",head_list)
    #print("Amount List:\n", amount_list)
    print(together)


# Donot print the total amount per head within the function. return the total amount per head, 
# call the function and print it outside function
def sum_of_headandamount(head,amount):
    df=read_file(file_name)
    category_totals=df.groupby("Head")["Amount"].sum()
    print("The total amount for each category:")
    print(category_totals)


# Donot print the avg amount per head within the function. return the avg amount per head, 
# call the function and print it outside function
def avg_of_headandamount(head,amount):
    df=read_file(file_name)
    category_totals=df.groupby("Head")["Amount"].mean()
    print("The average for each category:")
    print(category_totals)
    

#print(storeoutflowdata(file_name))
#print_contents(file_name)
#print(read_file(file_name))
#print(print_table(file_name))

#amount_sum("Amount")
#average_amount("Amount")
#print_amount_sum("Amount")
#print_only_headandamount("Head","Amount")
#sum_of_headandamount("Head","Amount")
avg_of_headandamount("Head","Amount")


    





