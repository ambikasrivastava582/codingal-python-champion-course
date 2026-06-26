import tkinter as tk

# Function to open a new window
def open_window():
    top = tk.Toplevel(root)
    top.title("Second Window")
    top.geometry("300x200")
    top.configure(bg="lightyellow")

    label = tk.Label(
        top,
        text="Welcome to the Top-Level Window!",
        font=("Arial", 12),
        bg="lightyellow"
    )
    label.pack(pady=30)

    close_button = tk.Button(
        top,
        text="Close",
        command=top.destroy,
        bg="red",
        fg="white"
    )
    close_button.pack(pady=10)


# Main Window
root = tk.Tk()
root.title("Main Window")
root.geometry("400x300")
root.configure(bg="lightblue")

heading = tk.Label(
    root,
    text="Main Window",
    font=("Arial", 18, "bold"),
    bg="lightblue"
)
heading.pack(pady=20)

button = tk.Button(
    root,
    text="Open New Window",
    command=open_window,
    bg="green",
    fg="white",
    font=("Arial", 12)
)
button.pack(pady=20)

root.mainloop()