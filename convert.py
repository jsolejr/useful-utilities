# Opens a file named 'input_file_name.txt' in read mode.
# The 'with' statement ensures that the file is properly closed after it is used.
with open('input_file_name.txt', 'r') as file:
    
    # Reads all the lines in the file and stores them in a list named 'values'.
    # Each line in the file becomes an element in the list.
    values = file.readlines()

# Creates a new list named 'updated_values' that contains modified versions of the strings in the 'values' list.
# Each string is wrapped in single quotes and followed by a comma and a newline character.
updated_values = [f"'{value.strip()}',\n" for value in values]

# Opens a file named 'updated_file_name.txt' in write mode.
# The 'with' statement ensures that the file is properly closed after it is used.
with open('updated_file_name.txt', 'w') as file:
    
    # Writes the contents of the 'updated_values' list to the file.
    # Each element in the list is written as a separate line.
    file.writelines(updated_values)
