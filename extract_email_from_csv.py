import re
import csv
import os
import chardet

# Function to check if a given cell_value is an email address
def is_email(cell_value):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    trimmed_cell_value = cell_value.strip()
    return re.match(email_regex, trimmed_cell_value)

# Function to detect the encoding of a file using chardet library
def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

# Function to extract emails from a CSV file
def extract_emails_from_csv(file_path):
    emails = []
    encoding = detect_encoding(file_path)

    # Read the CSV file with the detected encoding and split rows using whitespace as the delimiter
    with open(file_path, 'r', newline='', encoding=encoding) as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', skipinitialspace=True)
        for row in reader:
            for cell in row:
                if is_email(cell):
                    emails.append(cell.strip())

    return emails

# Function to write the extracted emails to a text file
def write_emails_to_file(emails, output_file):
    with open(output_file, 'w') as f:
        for email in emails:
            f.write(f'{email}\n')

# Function to process all CSV files in a given directory
def process_csv_files_in_directory(directory, output_file):
    all_emails = []
    total_files = 0
    for file in os.listdir(directory):
        if file.endswith('.csv'):
            total_files += 1
            file_path = os.path.join(directory, file)
            print(f'Processing file: {file_path}')
            emails = extract_emails_from_csv(file_path)
            print(f'Found {len(emails)} emails in {file_path}')
            all_emails.extend(emails)

    write_emails_to_file(all_emails, output_file)
    return all_emails, total_files

if __name__ == '__main__':
    input_directory = r'\Input path here'  #'C:\Users\XXXXXXX\Auto-GPT\autogpt\auto_gpt_workspace\WFO_users'
    output_file = '\outputpath\here'    #'output_emails.txt'

    # Process all CSV files in the input_directory and save the extracted emails to the output_file
    all_emails, total_files = process_csv_files_in_directory(input_directory, output_file)
    print(f'Processed {total_files} files')
    print(f'Extracted {len(all_emails)} emails and saved them to {output_file}')
