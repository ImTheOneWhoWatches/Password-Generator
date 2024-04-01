import random
import colorama
from colorama import Fore, Style
import time
import pyperclip
import tkinter as tk
from tkinter import ttk
import string
import os

default_length = 20  # default number of characters

def reset_script():
    global all, length, amount, default_length
    length = 20
    amount = 1

    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    digits = "123456789"
    symbols = "!@#$%^&*()_+-=~`:;{[}]:;>.<,?/"

    upper, lower, nums, syms = True, True, True, True

    all = ""

    if upper:
        all += uppercase_letters
    if lower:
        all += lowercase_letters
    if nums:
        all += digits
    if syms:
        all += symbols

def print_banner():
    print(Fore.BLUE + """
     ______ __           ____               _       __  __          _       __          __           __
    /_  __// /_   ___   / __ \  ____   ___ | |     / / / /_   ____ | |     / / ____ _  / /_  _____  / /_   ___    _____
     / /  / __ \ / _ \ / / / / / __ \ / _ \| | /| / / / __ \ / __ \| | /| / / / __ `/ / __/ / ___/ / __ \ / _ \  / ___/
    / /  / / / //  __// /_/ / / / / //  __/| |/ |/ / / / / // /_/ /| |/ |/ / / /_/ / / /_  / /__  / / / //  __/ (__  )
   /_/  /_/ /_/ \___/ \____/ /_/ /_/ \___/ |__/|__/ /_/ /_/ \____/ |__/|__/  \__,_/  \__/  \___/ /_/ /_/ \___/ /____/
""" + Style.RESET_ALL)

def print_separator():
    print(Fore.GREEN + "========================================================================================================================" + Style.RESET_ALL)

def generate_password():
    global all, length, amount
    passwords = []  # Temporary list to store generated passwords
    length = length_var.get()
    characters = characters_var.get()
    
    if not length:
        password_text.delete(1.0, tk.END)
        password_text.insert(tk.END, "Please enter a password length.")
        return
    
    try:
        length = int(length)
        if length <= 0:
            password_text.delete(1.0, tk.END)
            password_text.insert(tk.END, "Password length must be a positive integer.")
            return
    except ValueError:
        password_text.delete(1.0, tk.END)
        password_text.insert(tk.END, "Invalid password length.")
        return
    
    if not characters:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = characters.replace(" ", "")  # Remove any spaces
        
    password = ''.join(random.choice(characters) for _ in range(length))
    
    password_text.delete(1.0, tk.END)
    password_text.insert(tk.END, password)
    
    with open("assets/passwords.txt", "a") as f:
        f.write(password + "\n")  # Write the generated password to the file

def remove_passwords():
    try:
        open("assets/passwords.txt", "w").close()  # Open in write mode to truncate the file
        password_listbox.delete(0, tk.END)  # Clear the listbox
        print("All saved passwords have been removed.")
    except FileNotFoundError:
        print("No passwords found to remove.")

# Function to load saved passwords from passwords.txt
def load_passwords():
    try:
        with open("assets/passwords.txt", "r") as f:
            passwords = f.readlines()
            for password in passwords:
                password_listbox.insert(tk.END, password.strip())
    except FileNotFoundError:
        print("Passwords file not found.")

def copy_password():
    password = password_text.get(1.0, tk.END).strip()
    pyperclip.copy(password)
    print("Password copied to clipboard:", password)

# Create the main window
root = tk.Tk()
root.title("TheOne's Client")

# Set background image
bg_image = tk.PhotoImage(file="assets/BackgroundImage.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Prevent the fucking resizment of the window this took a long time to learn for 0 reason
root.resizable(False, False)

#input fields and labels
length_label = ttk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=5, pady=5)
length_var = tk.StringVar()
length_entry = ttk.Entry(root, textvariable=length_var, width=10)
length_entry.grid(row=0, column=1, padx=5, pady=5)

characters_label = ttk.Label(root, text="Custom Characters (optional):")
characters_label.grid(row=1, column=0, padx=5, pady=5)
characters_var = tk.StringVar()
characters_entry = ttk.Entry(root, textvariable=characters_var)
characters_entry.grid(row=1, column=1, padx=5, pady=5)

# Create the generate button
generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Create the copy button
copy_button = ttk.Button(root, text="Copy Password", command=copy_password)
copy_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Create the text area to display the generated passwords
password_text = tk.Text(root, height=5, width=50)
password_text.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Create the listbox to display saved passwords
password_listbox = tk.Listbox(root, height=10, width=30)
password_listbox.grid(row=0, column=2, rowspan=5, padx=5, pady=5)

# Create the load passwords button
load_button = ttk.Button(root, text="Load Passwords", command=load_passwords)
load_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Create the clear button
clear_button = ttk.Button(root, text="Clear", command=remove_passwords)
clear_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
