import pandas as pd
import datetime

def validate_date(date):
    try:
        datetime.datetime.strptime(date, '%d/%m/%Y')
    except ValueError:
        return 'Invalid date format'
    return None


df = pd.read_csv("aa.csv")
print(df.describe)

def print_contents(df):
    for _, row in df.iterrows():
        print("\nRow Data:")
        for col_name in df.columns:
            print(f"{col_name}:{row[col_name]}")
        #print(tabulate(df, headers='keys', tablefmt='grid'))
        err= validate_date(row["Date"])
        if err:
            print("Error.")
        else:
            print("No error.")