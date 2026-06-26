import tkinter as tk
from tkinter import messagebox

# Function to convert length
def convert():
    try:
        meters = float(entry.get())

        centimeters = meters * 100
        kilometers = meters / 1000
        inches = meters * 39.37

        result.config(
            text=f"Centimeters : {centimeters:.2f} cm\n"
                 f"Kilometers  : {kilometers:.3f} km\n"
                 f"Inches      : {inches:.2f} in"
        )

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")


# Create Window
root = tk.Tk()
root.title("Length Converter")
root.geometry("400x350")
root.configure(bg="lightyellow")

# Heading
heading = tk.Label(root,
                   text="Length Converter",
                   font=("Arial", 18, "bold"),
                   bg="lightyellow",
                   fg="blue")
heading.pack(pady=15)

# Label
label = tk.Label(root,
                 text="Enter Length in Meters:",
                 font=("Arial", 12),
                 bg="lightyellow")
label.pack()

# Entry
entry = tk.Entry(root, font=("Arial", 12), width=20)
entry.pack(pady=10)

# Button
button = tk.Button(root,
                   text="Convert",
                   font=("Arial", 12),
                   bg="green",
                   fg="white",
                   command=convert)
button.pack(pady=10)

# Result Label
result = tk.Label(root,
                  text="",
                  font=("Arial", 12),
                  bg="lightyellow",
                  fg="black",
                  justify="left")
result.pack(pady=20)

# Run Window
root.mainloop()