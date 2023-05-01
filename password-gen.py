# Import the random and tkinter modules
import random
import tkinter as tk
from tkinter import messagebox

# Define a function to generate the password
def generate_password(length):
    # Define the character sets to be used in the password
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>/?\\"

    # Combine the character sets into a single string
    all_characters = lowercase_letters + uppercase_letters + numbers + special_characters

    # Generate a random password and return it
    password = "".join(random.sample(all_characters, length))
    return password

# Prompt the user to input the desired length of the password
length = tk.simpledialog.askinteger("Password Generator", "How many characters do you want in your password?", minvalue=1)

# Generate the password and display it in a message box
password = generate_password(length)
messagebox.showinfo("Password Generator", f"Your new password is: {password}")

# End of program
