with open('input_file_name.txt', 'r') as file:
    values = file.readlines()

updated_values = [f"'{value.strip()}',\n" for value in values]

with open('updated_file_name.txt', 'w') as file:
    file.writelines(updated_values)
