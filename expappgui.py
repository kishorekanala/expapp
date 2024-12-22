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

def submit_contribution():
    contribution_date = contribution_date_entry.get()
    contribution_source = contribution_source_entry.get()
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

# Create the main window
root = tk.Tk()
root.title("Expense Application")

# Load configuration
config = load_config()

# Create the main frame
root_frame = ttk.Frame(root)
root_frame.grid(row=0, column=0, padx=10, pady=10)

# Create the outflow entry frame with border and heading
outflow_entry_frame = tk.LabelFrame(root_frame, text="Outflow Entry")
outflow_entry_frame.grid(row=0, column=0, padx=10, pady=10, sticky="n")

# Create and place the labels and entry widgets in the outflow entry frame
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

# Create the inflow entry frame with border and heading
inflow_entry_frame = tk.LabelFrame(root_frame, text="Inflow Entry")
inflow_entry_frame.grid(row=1, column=0, padx=10, pady=10, sticky="n")

# Create and place the labels and entry widgets in the inflow entry frame
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
submit_inflow_button = tk.Button(inflow_entry_frame, text="Submit Inflow", command=submit_contribution)
submit_inflow_button.grid(row=4, column=0, columnspan=2, pady=10)

# Create the outflow summary frame on the right-hand side of the outflow entry frame
outflow_summary_frame = tk.LabelFrame(root_frame, text="Outflow Summary")
outflow_summary_frame.grid(row=0, column=1, padx=10, pady=10, sticky="n")

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

# Create the contributions summary frame on the right-hand side of the inflow entry frame
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

# Run the application
root.mainloop()