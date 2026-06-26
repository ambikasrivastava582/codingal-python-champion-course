import tkinter as tk
import random

# Function to play the game
def play(user_choice):
    choices = ["Stone", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Stone" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Stone") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    user_label.config(text="Your Choice: " + user_choice)
    computer_label.config(text="Computer Choice: " + computer_choice)
    result_label.config(text=result)


# Create Main Window
root = tk.Tk()
root.title("Stone Paper Scissors Game")
root.geometry("450x350")
root.configure(bg="lightblue")

# Heading
heading = tk.Label(
    root,
    text="Stone Paper Scissors",
    font=("Arial", 18, "bold"),
    bg="lightblue"
)
heading.pack(pady=15)

# Instruction
instruction = tk.Label(
    root,
    text="Choose one option:",
    font=("Arial", 12),
    bg="lightblue"
)
instruction.pack()

# Buttons
frame = tk.Frame(root, bg="lightblue")
frame.pack(pady=15)

stone_btn = tk.Button(frame, text="Stone", width=10,
                      command=lambda: play("Stone"))
stone_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(frame, text="Paper", width=10,
                      command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(frame, text="Scissors", width=10,
                         command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

# Result Labels
user_label = tk.Label(root, text="Your Choice: ",
                      font=("Arial", 12), bg="lightblue")
user_label.pack(pady=5)

computer_label = tk.Label(root, text="Computer Choice: ",
                          font=("Arial", 12), bg="lightblue")
computer_label.pack(pady=5)

result_label = tk.Label(root,
                        text="",
                        font=("Arial", 14, "bold"),
                        fg="blue",
                        bg="lightblue")
result_label.pack(pady=15)

# Run Application
root.mainloop()