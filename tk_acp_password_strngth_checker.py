import tkinter as tk
from tkinter import messagebox
import re

# Function to check password strength
def check_password():
    password = entry.get()

    if len(password) < 6:
        result.config(text="Weak Password", fg="red")

    elif (len(password) >= 8 and
          re.search("[A-Z]", password) and
          re.search("[a-z]", password) and
          re.search("[0-9]", password) and
          re.search("[@#$%^&*!]", password)):
        result.config(text="Strong Password", fg="green")

    else:
        result.config(text="Medium Password", fg="orange")


# Create Window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")
root.configure(bg="lightblue")

# Heading
heading = tk.Label(root,
                   text="Password Strength Checker",
                   font=("Arial", 16, "bold"),
                   bg="lightblue")
heading.pack(pady=15)

# Password Label
label = tk.Label(root,
                 text="Enter Password:",
                 font=("Arial", 12),
                 bg="lightblue")
label.pack()

# Password Entry
entry = tk.Entry(root, show="*", font=("Arial", 12), width=25)
entry.pack(pady=10)

# Check Button
button = tk.Button(root,
                   text="Check Strength",
                   command=check_password,
                   bg="green",
                   fg="white",
                   font=("Arial", 12))
button.pack(pady=10)

# Result Label
result = tk.Label(root,
                  text="",
                  font=("Arial", 14, "bold"),
                  bg="lightblue")
result.pack(pady=10)

# Run Application
root.mainloop()