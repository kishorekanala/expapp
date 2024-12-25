import sqlite3
from datetime import datetime

# Connect to the database
def connect_db():
    conn = sqlite3.connect('outflow.db')
    return conn

# Create the table if it doesn't exist
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS outflow (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            outflow_date TEXT,
            outflow_head TEXT,
            beneficiary_name TEXT,
            amount REAL,
            notes TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Insert data into the table
def insert_data(outflow_date, outflow_head, beneficiary_name, amount, notes):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO outflow (outflow_date, outflow_head, beneficiary_name, amount, notes)
        VALUES (?, ?, ?, ?, ?)
    ''', (outflow_date, outflow_head, beneficiary_name, amount, notes))
    conn.commit()
    conn.close()

# Read data from the table
def read_data():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM outflow')
    rows = cursor.fetchall()
    conn.close()
    return rows

# Example usage
if __name__ == "__main__":
    create_table()
    insert_data(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'Rent', 'John Doe', 1200.00, 'Monthly rent payment')
    data = read_data()
    for row in data:
        print(row)