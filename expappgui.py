import tkinter as tk
from tkinter import ttk
import json

def load_config():
    with open('config.json', 'r') as file:
        return json.load(file)

def submit_outflow():
    outflow_date = outflow_date_entry.get()
    outflow_head = outflow_head_combobox.get()
    beneficiary_name = outflow_name_entry.get()
    amount = outflow_amount_entry.get()
    notes = outflow_notes_text.get("1.0", tk.END)
    
    data = {
        "OutFlow Date": outflow_date,
        "OutFlow Head": outflow_head,
        "Name": beneficiary_name,
        "Amount": amount,
        "Note": notes.strip()
    }
    
    # Placeholder for action to handle the data
    print(data)  # Replace this with actual action

def submit_inflow():
    inflow_date = inflow_date_entry.get()
    inflow_source = inflow_source_entry.get()
    amount = inflow_amount_entry.get()
    notes = inflow_notes_text.get("1.0", tk.END)
    
    data = {
        "InFlow Date": inflow_date,
        "InFlow Source": inflow_source,
        "Amount": amount,
        "Note": notes.strip()
    }
    
    # Placeholder for action to handle the data
    print(data)  # Replace this with actual action

# Load configuration
config = load_config()

# Create the main window
root = tk.Tk()
root.title("Financial Entry Form")

# Create the root frame
root_frame = tk.Frame(root)
root_frame.pack(padx=10, pady=10)

# Create the outflow entry sub-frame
outflow_entry_frame = tk.LabelFrame(root_frame, text="Outflow Entry")
outflow_entry_frame.grid(row=0, column=0, padx=10, pady=10)

# Create and place the labels and entry widgets in the outflow entry sub-frame
tk.Label(outflow_entry_frame, text="Outflow Date (dd/mm/yyyy):").grid(row=0, column=0, padx=10, pady=5)
outflow_date_entry = tk.Entry(outflow_entry_frame)
outflow_date_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(outflow_entry_frame, text="Outflow Head:").grid(row=1, column=0, padx=10, pady=5)
outflow_head_combobox = ttk.Combobox(outflow_entry_frame, values=config["outflow_heads"])
outflow_head_combobox.grid(row=1, column=1, padx=10, pady=5)

tk.Label(outflow_entry_frame, text="Beneficiary Name:").grid(row=2, column=0, padx=10, pady=5)
outflow_name_entry = tk.Entry(outflow_entry_frame)
outflow_name_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(outflow_entry_frame, text="Amount:").grid(row=3, column=0, padx=10, pady=5)
outflow_amount_entry = tk.Entry(outflow_entry_frame)
outflow_amount_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(outflow_entry_frame, text="Notes:").grid(row=4, column=0, padx=10, pady=5)
outflow_notes_text = tk.Text(outflow_entry_frame, height=5, width=30)
outflow_notes_text.grid(row=4, column=1, padx=10, pady=5)

# Create and place the submit button for outflow entry
submit_outflow_button = tk.Button(outflow_entry_frame, text="Submit Outflow", command=submit_outflow)
submit_outflow_button.grid(row=5, column=0, columnspan=2, pady=10)

# Create the inflow entry sub-frame
inflow_entry_frame = tk.LabelFrame(root_frame, text="Inflow Entry")
inflow_entry_frame.grid(row=1, column=0, padx=10, pady=10)

# Create and place the labels and entry widgets in the inflow entry sub-frame
tk.Label(inflow_entry_frame, text="Inflow Date (dd/mm/yyyy):").grid(row=0, column=0, padx=10, pady=5)
inflow_date_entry = tk.Entry(inflow_entry_frame)
inflow_date_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(inflow_entry_frame, text="Inflow Source:").grid(row=1, column=0, padx=10, pady=5)
inflow_source_entry = tk.Entry(inflow_entry_frame)
inflow_source_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(inflow_entry_frame, text="Amount:").grid(row=2, column=0, padx=10, pady=5)
inflow_amount_entry = tk.Entry(inflow_entry_frame)
inflow_amount_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(inflow_entry_frame, text="Notes:").grid(row=3, column=0, padx=10, pady=5)
inflow_notes_text = tk.Text(inflow_entry_frame, height=5, width=30)
inflow_notes_text.grid(row=3, column=1, padx=10, pady=5)

# Create and place the submit button for inflow entry
submit_inflow_button = tk.Button(inflow_entry_frame, text="Submit Inflow", command=submit_inflow)
submit_inflow_button.grid(row=4, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()