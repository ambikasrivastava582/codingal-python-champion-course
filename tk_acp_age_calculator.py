import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Function to calculate age
def calculate_age():
    try:
        birth_year = int(entry.get())
        current_year = datetime.now().year

        if birth_year > current_year:
            messagebox.showerror("Error", "Birth year cannot be in the future!")
            return

        age = current_year - birth_year
        result_label.config(text=f"Your Age is: {age} years")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid birth year.")

# Create Window
root = tk.Tk()
root.title("Age Calculator")
root.geometry("350x250")
root.configure(bg="lightblue")

# Heading
heading = tk.Label(
    root,
    text="Age Calculator",
    font=("Arial", 18, "bold"),
    bg="lightblue"
)
heading.pack(pady=15)

# Birth Year Label
label = tk.Label(
    root,
    text="Enter Your Birth Year:",
    font=("Arial", 12),
    bg="lightblue"
)
label.pack()

# Entry Box
entry = tk.Entry(root, font=("Arial", 12), width=20)
entry.pack(pady=10)

# Calculate Button
button = tk.Button(
    root,
    text="Calculate Age",
    command=calculate_age,
    bg="green",
    fg="white",
    font=("Arial", 12)
)
button.pack(pady=10)

# Result Label
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="lightblue",
    fg="blue"
)
result_label.pack(pady=10)

# Run Application
root.mainloop()