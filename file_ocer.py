import pytesseract
import PyPDF4
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import os.path

# Create a Tkinter root window
root = tk.Tk()
root.withdraw()

# Prompt the user to select an input file using a file dialog
input_file_path = filedialog.askopenfilename()

# Get the file extension
file_extension = os.path.splitext(input_file_path)[1].lower()

if file_extension in ['.jpg', '.jpeg', '.png', '.bmp', '.gif']:
    # Open the input image file
    input_image = Image.open(input_file_path)

    # Perform OCR using pytesseract
    extracted_text = pytesseract.image_to_string(input_image)

elif file_extension == '.pdf':
    # Open the input PDF file
    with open(input_file_path, mode='rb') as input_file:
        pdf_reader = PyPDF4.PdfFileReader(input_file)
        num_pages = pdf_reader.getNumPages()
        extracted_text = ''

        # Extract text from each page of the PDF file
        for i in range(num_pages):
            page = pdf_reader.getPage(i)
            extracted_text += page.extractText()

else:
    # Unsupported file type
    raise ValueError(f"Unsupported file type: {file_extension}")

# Get the output file path with the same name as the input file, but with a .txt extension
output_file_path = os.path.splitext(input_file_path)[0] + '.txt'

# Write the extracted text to the output file
with open(output_file_path, 'w') as output_file:
    output_file.write(extracted_text)
