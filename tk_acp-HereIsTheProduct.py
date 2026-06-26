import tkinter as tk
from tkinter import ttk, messagebox

# Function to display product details
def show_details():
    details = f"""
Product Name : {name_entry.get()}
Category : {category.get()}
Price : ₹{price_entry.get()}
Quantity : {quantity.get()}
Payment Mode : {payment.get()}
Gift Wrap : {"Yes" if gift.get() else "No"}
"""

    messagebox.showinfo("Product Details", details)


# Create Window
root = tk.Tk()
root.title("Product Form")
root.geometry("400x450")
root.configure(bg="lightblue")

# Heading
heading = tk.Label(root, text="Product Order Form",
                   font=("Arial", 18, "bold"),
                   bg="lightblue")
heading.pack(pady=10)

# Product Name
tk.Label(root, text="Product Name:", bg="lightblue").pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack()

# Category
tk.Label(root, text="Category:", bg="lightblue").pack()

category = ttk.Combobox(root,
                        values=["Electronics", "Clothing", "Books", "Toys"])
category.pack()
category.current(0)

# Price
tk.Label(root, text="Price:", bg="lightblue").pack()
price_entry = tk.Entry(root, width=30)
price_entry.pack()

# Quantity
tk.Label(root, text="Quantity:", bg="lightblue").pack()

quantity = tk.Spinbox(root, from_=1, to=20, width=10)
quantity.pack()

# Payment Method
tk.Label(root, text="Payment Method:", bg="lightblue").pack()

payment = tk.StringVar()
payment.set("Cash")

tk.Radiobutton(root, text="Cash",
               variable=payment,
               value="Cash",
               bg="lightblue").pack()

tk.Radiobutton(root, text="Card",
               variable=payment,
               value="Card",
               bg="lightblue").pack()

# Gift Wrap
gift = tk.BooleanVar()

tk.Checkbutton(root,
               text="Gift Wrap",
               variable=gift,
               bg="lightblue").pack()

# Submit Button
submit = tk.Button(root,
                   text="Submit",
                   command=show_details,
                   bg="green",
                   fg="white")
submit.pack(pady=15)

root.mainloop()