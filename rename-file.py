import os

def rename_file(filename):
    # Open file and read the first three lines
    with open(filename, 'r') as f:
        first_lines = f.readlines()[:3]

    # Construct new filename using first three lines
    # Strip newline characters from each line and join with underscores
    new_filename = '_'.join([line.strip() for line in first_lines]) + '.txt'

    # Rename file to new filename
    os.rename(filename, new_filename)

    # Return new filename
    return new_filename
