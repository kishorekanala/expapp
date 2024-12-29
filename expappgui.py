import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json

from outflowdatabase import * 
from readcashflowdata import *

def load_config():
    with open('config.json', 'r') as file:
        return json.load(file)

def submit_outflow():
    
    df, rows = get_cashflowdata(file_path_entry.get())

    #for row in rows:
    #    print(row)
    print(df)

    # Ask for user confirmation
    if not messagebox.askyesno("Confirmation", "Do you want to display the DataFrame?"):
        return

    # Create a new frame to display the DataFrame
    df_frame = tk.LabelFrame(root_frame, text="DataFrame Display")
    df_frame.grid(row=0, column=2, rowspan=2, padx=10, pady=10, sticky="nsew")

    # Create a canvas and scrollbars
    canvas = tk.Canvas(df_frame)
    v_scrollbar = ttk.Scrollbar(df_frame, orient="vertical", command=canvas.yview)
    h_scrollbar = ttk.Scrollbar(df_frame, orient="horizontal", command=canvas.xview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

    # Place the canvas and scrollbars in the frame
    canvas.grid(row=0, column=0, sticky="nsew")
    v_scrollbar.grid(row=0, column=1, sticky="ns")
    h_scrollbar.grid(row=1, column=0, sticky="ew")

    df_frame.grid_rowconfigure(0, weight=1)
    df_frame.grid_columnconfigure(0, weight=1)

    # Display the DataFrame in the scrollable frame
    for i, (index, row) in enumerate(df.iterrows()):
        for j, value in enumerate(row):
            tk.Label(scrollable_frame, text=value).grid(row=i, column=j, padx=5, pady=5)

def submit_contribution():
    contribution_date = contribution_date_entry.get()
    contribution_source = contribution_source_combobox.get()
    amount = contribution_amount_entry.get()
    notes = contribution_notes_text.get("1.0", tk.END)
    
    data = {
        "Contribution Date": contribution_date,
        "Contribution Source": contribution_source,
        "Amount": amount,
        "Note": notes.strip()
    }
    
    # Placeholder for action to handle the data
    print(data)  # Replace this with actual action

def import_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        # Placeholder for action to handle the file import
        print(f"Importing file from: {file_path}")  # Replace this with actual action

# Define the bulk_entry function
def bulk_entry():
    file_path = filedialog.askopenfilename()
    if file_path:
        print(f"Selected file: {file_path}")

# Create the main window
root = tk.Tk()
root.title("Expense Application")

# Load configuration
config = load_config()

# Create the main frame
root_frame = ttk.Frame(root)
root_frame.grid(row=0, column=0, padx=10, pady=10)

# Create the outflow entry frame with border and heading
cashflow_entry_frame = tk.LabelFrame(root_frame, text="Cashflow Entry")
cashflow_entry_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# Create and place the labels and entry widgets in the outflow entry frame
tk.Label(cashflow_entry_frame, text="CashFlow Data \nFile Path:").grid(row=6, column=0, padx=5, pady=5)
file_path_entry = tk.Entry(cashflow_entry_frame)
file_path_entry.grid(row=6, column=1, padx=5, pady=5)

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_path_entry.delete(0, tk.END)
        file_path_entry.insert(0, file_path)

select_file_button = tk.Button(cashflow_entry_frame, text="Select File", command=select_file)
select_file_button.grid(row=6, column=2, padx=5, pady=5)

# Create the Submit button
submit_button = tk.Button(cashflow_entry_frame, text="Submit", command=submit_outflow)
submit_button.grid(row=6, column=3, padx=5, pady=5)

# Create the outflow summary frame below the cashflow entry frame
outflow_summary_frame = tk.LabelFrame(root_frame, text="Outflow Summary")
outflow_summary_frame.grid(row=1, column=0, padx=10, pady=10, sticky="n")

# Add more outflow heads as needed
# Dynamically create labels for each outflow head from the config
outflow_head_labels = {}
for i, head in enumerate(config["outflow_heads"], start=1):
    tk.Label(outflow_summary_frame, text=f"{head}:").grid(row=i, column=0, padx=10, pady=5)
    outflow_head_labels[head] = tk.Label(outflow_summary_frame, text="0.00")
    outflow_head_labels[head].grid(row=i, column=1, padx=10, pady=5)

# Create a label for the total outflow
tk.Label(outflow_summary_frame, text="Total Outflow:").grid(row=0, column=0, padx=10, pady=5)
total_outflow_label = tk.Label(outflow_summary_frame, text="0.00")
total_outflow_label.grid(row=0, column=1, padx=10, pady=5)

# Create the contributions summary frame to the right of the outflow summary frame
contributions_summary_frame = tk.LabelFrame(root_frame, text="Contributions Summary")
contributions_summary_frame.grid(row=1, column=1, padx=10, pady=10, sticky="n")

# Add more contribution heads as needed
# Dynamically create labels for each contribution head from the config
contribution_head_labels = {}
for i, head in enumerate(config["contribution_heads"], start=1):
    tk.Label(contributions_summary_frame, text=f"{head}:").grid(row=i, column=0, padx=10, pady=5)
    contribution_head_labels[head] = tk.Label(contributions_summary_frame, text="0.00")
    contribution_head_labels[head].grid(row=i, column=1, padx=10, pady=5)

# Create a label for the total contributions
tk.Label(contributions_summary_frame, text="Total Contributions:").grid(row=0, column=0, padx=10, pady=5)
total_contributions_label = tk.Label(contributions_summary_frame, text="0.00")
total_contributions_label.grid(row=0, column=1, padx=10, pady=5)

create_table()

# Run the application
root.mainloop()