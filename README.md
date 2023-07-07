# Useful-Utilities
A hodge podge of utilities to do different things I've come across while working.






# Email Extractor from CSV Files
Create extract_email_from_csv.py
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



# Webpage Metadata Extractor

This Python script fetches and extracts metadata from a specified URL using the `requests` and `BeautifulSoup` libraries. It returns a list of dictionaries containing the metadata properties and their corresponding values.

## Usage

1. Ensure you have Python 3.x installed on your system.
2. Install the required libraries using the following commands:

```bash
pip install requests
pip install beautifulsoup4
```

3. Place the `metadata_extractor.py` script in a directory of your choice.
4. Import the `get_metadata` function from the script in your Python project:

```python
from metadata_extractor import get_metadata
```

5. Call the `get_metadata` function with the URL you want to extract metadata from:

```python
url = "https://example.com"
metadata_list = get_metadata(url)
```

The `metadata_list` variable will contain a list of dictionaries with metadata properties and their corresponding values.

## Requirements

- Python 3.x
- `requests` library (install using `pip install requests`)
- `beautifulsoup4` library (install using `pip install beautifulsoup4`)

## Functions

- `get_metadata(url)`: Fetches the specified URL, extracts metadata from the webpage, and returns a list of dictionaries containing metadata properties and their corresponding values.

## Limitations

This script extracts metadata properties that have either the `property` or `name` attribute in their corresponding `meta` tags. If a webpage contains metadata in a different format, you may need to modify the script accordingly.


Sure, here's an example README.md file for this Python script:

# OCR Text Extractor

This is a Python script that can be used to extract text from image or PDF files using OCR (optical character recognition).

## Requirements

- Python 3.x
- `pytesseract` module
- `PyPDF4` module
- `Pillow` module
- `tkinter` module (included with Python)

You can install the required Python modules using `pip`, the package manager for Python. For example, to install `pytesseract`, you can run the following command in your terminal or command prompt:

```
pip install pytesseract
```

## Usage

1. Open a terminal or command prompt and navigate to the directory containing the `ocr_text_extractor.py` file.
2. Run the following command:

   ```
   python ocr_text_extractor.py
   ```

3. The script will prompt you to select an input file using a file dialog. You can select an image or PDF file.
4. The script will extract the text from the input file using OCR and save it to a .txt file with the same name as the input file, in the same directory.

## Limitations

- The OCR accuracy depends on the quality of the input file and the fonts used in the text.
- The script currently only supports the following image file types: .jpg, .jpeg, .png, .bmp, .gif. If you try to use an unsupported file type, the script will raise a ValueError.
- The script currently only supports the PyPDF4 module for extracting text from PDF files. If you have a PDF file that uses a different PDF library or format, you may need to modify the script to support it.

Certainly! Here's an example of a README.md file for your program:

```markdown



# Excel Search Program

This Python program allows you to search for values in an Excel workbook based on a list of study descriptions. It provides a user-friendly interface where you can select the input file, search the workbook, and generate a list of values that were not found.

## Requirements

- Python 3.x
- openpyxl library

## Installation

1. Clone or download the repository.
2. Install the required dependencies using pip:

   ```shell
   pip install openpyxl
   ```

## Usage

1. Run the program by executing the `SearchExcelForMissingValues.py` file.
2. Select the input file when prompted. This file should contain a list of study descriptions, with each description on a separate line.
3. Select the Excel workbook file when prompted. The program will search for the study descriptions in column K of each sheet in the workbook.
4. After the search is complete, a dialog box will display the results. If any values were not found in the workbook, they will be listed.
5. Click the "Save" button to select a save location and save the list of not found values to a text file. Alternatively, click the "Close" button to exit the program.

## Example

Suppose you have an input file named `study_descriptions.txt` containing the following study descriptions:

```
Study A
Study B
Study C
```

And you have an Excel workbook named `data.xlsx` with multiple sheets. The program will search for these study descriptions in column K of each sheet in the workbook and generate a list of any descriptions that were not found.

## License

This program is licensed under the [MIT License](LICENSE).
```

Feel free to customize the README.md file as per your specific requirements and add any additional sections or information you deem necessary.

Let me know if you need further assistance!
