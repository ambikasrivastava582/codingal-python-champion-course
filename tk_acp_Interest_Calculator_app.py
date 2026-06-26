import tkinter as tk
from tkinter import messagebox

# Function to calculate simple interest
def calculate_interest():
    try:
        principal = float(principal_entry.get())
        rate = float(rate_entry.get())
        time = float(time_entry.get())

        interest = (principal * rate * time) / 100
        total_amount = principal + interest

        result_label.config(
            text=f"Simple Interest: ₹{interest:.2f}\n"
                 f"Total Amount: ₹{total_amount:.2f}"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")


# Create Window
root = tk.Tk()
root.title("Simple Interest Calculator")
root.geometry("400x350")
root.configure(bg="lightgreen")

# Heading
heading = tk.Label(
    root,
    text="Simple Interest Calculator",
    font=("Arial", 18, "bold"),
    bg="lightgreen"
)
heading.pack(pady=15)

# Principal Amount
tk.Label(
    root,
    text="Principal Amount (₹):",
    bg="lightgreen",
    font=("Arial", 12)
).pack()

principal_entry = tk.Entry(root, width=25)
principal_entry.pack(pady=5)

# Rate of Interest
tk.Label(
    root,
    text="Rate of Interest (%):",
    bg="lightgreen",
    font=("Arial", 12)
).pack()

rate_entry = tk.Entry(root, width=25)
rate_entry.pack(pady=5)

# Time
tk.Label(
    root,
    text="Time (Years):",
    bg="lightgreen",
    font=("Arial", 12)
).pack()

time_entry = tk.Entry(root, width=25)
time_entry.pack(pady=5)

# Calculate Button
calculate_btn = tk.Button(
    root,
    text="Calculate",
    command=calculate_interest,
    bg="blue",
    fg="white",
    font=("Arial", 12)
)
calculate_btn.pack(pady=15)

# Result Label
result_label = tk.Label(
    root,
    text="",
    bg="lightgreen",
    font=("Arial", 14, "bold"),
    fg="darkgreen"
)
result_label.pack(pady=10)

# Run Application
root.mainloop()