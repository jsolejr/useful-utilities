import tkinter as tk
from tkinter import filedialog
from openpyxl import load_workbook

# Create root window and hide it
root = tk.Tk()
root.withdraw()

# Get input file path from user
input_file_path = filedialog.askopenfilename(title="Select the input file")
with open(input_file_path, 'r') as f:
    lines = f.read().splitlines()

# Get Excel file path from user
excel_file_path = filedialog.askopenfilename(title="Select the Excel file")

# Load the Excel workbook
wb = load_workbook(filename=excel_file_path, read_only=True)

# Create a list to store no match results
no_match_values = []

# Iterate over input values
for line in lines:
    # Assume no match until found
    match_found = False
    # Iterate over sheets and cells
    for sheet in wb:
        for row in sheet.iter_rows():
            for cell in row:
                # Check if cell value matches input value
                if cell.value is not None and str(cell.value).lower() == line.lower():
                    # Match found
                    match_found = True
                    # Skip to next line
                    break
            # Break nested loop if match found
            if match_found:
                break
        # Break loop over sheets if match found
        if match_found:
            break
    # If no match found after checking all cells, add to no match list
    if not match_found:
        no_match_values.append(line)

# Get output file path from user
output_file_path = filedialog.asksaveasfilename(title="Save the output file", defaultextension=".txt")

# Write no match values to output file
with open(output_file_path, 'w') as f:
    for value in no_match_values:
        f.write(f'{value}\n')

print(f"Completed. No match values have been saved to {output_file_path}.")
