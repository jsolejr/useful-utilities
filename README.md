# useful-utilities
A hodge podge of utilities to do different things I've come across while working.



Create extract_email_from_csv.py
# Email Extractor from CSV Files

This Python script extracts email addresses from CSV files located in a specified directory and saves the extracted emails to a text file.

## Usage

1. Ensure you have Python 3.x installed on your system.
2. Place the `get_email.py` script in the directory containing the CSV files you want to extract email addresses from.
3. Update the `input_directory` variable in the script with the path to your directory containing the CSV files. By default, it is set to:

```python
input_directory = r'Input\path\here'
```

4. Update the 'output\path\here` variable in the script with the desired name for the output text file. By default, it is set to:

```python
output_file = 'output_emails.txt'
```

5. Open a terminal or command prompt, navigate to the directory containing the `get_email.py` script, and run the script using the following command:

```bash
python get_email.py
```

The script will process all CSV files in the specified directory, extract email addresses, and save them to the output text file. You will see a summary of the processed files and the number of extracted emails in the terminal or command prompt.

## Requirements

- Python 3.x
- `chardet` library for detecting file encoding (install using `pip install chardet`)

## Functions

- `is_email(cell_value)`: Checks if a given cell value is an email address.
- `detect_encoding(file_path)`: Detects the encoding of a file using the `chardet` library.
- `extract_emails_from_csv(file_path)`: Extracts emails from a CSV file with the specified file path.
- `write_emails_to_file(emails, output_file)`: Writes the extracted emails to a text file.
- `process_csv_files_in_directory(directory, output_file)`: Processes all CSV files in a given directory, extracts emails, and saves them to the output file.

## Limitations

This script assumes that the CSV files use any whitespace character as a delimiter. If your CSV files use a different delimiter, you may need to modify the script accordingly.
