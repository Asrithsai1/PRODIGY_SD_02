import tkinter as tk
from tkinter import messagebox
import random

# Function to start a new game
def new_game():
    global random_number
    random_number = random.randint(1, 100)
    guess_button.config(state="normal")
    result_label.config(text="I have picked a number between 1 and 100. Try to guess!")
    entry_box.delete(0, 'end')

# Function to handle the user's guess
def check_guess():
    try:
        guess = int(entry_box.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        return

    if guess < 1 or guess > 100:
        result_label.config(text="Please guess a number between 1 and 100.")
    elif guess < random_number:
        result_label.config(text="Too low! Try again.")
    elif guess > random_number:
        result_label.config(text="Too high! Try again.")
    else:
        result_label.config(text=f"Congratulations! {guess} is correct.")
        guess_button.config(state="disabled")

# Creating the main window
window = tk.Tk()
window.title("Guessing Game")

# Setting up the layout and widgets
instructions_label = tk.Label(window, text="Welcome to the Guessing Game! Try to guess the number.", font=("Helvetica", 14))
instructions_label.pack(pady=10)

entry_label = tk.Label(window, text="Enter your guess:", font=("Helvetica", 12))
entry_label.pack()

entry_box = tk.Entry(window, font=("Helvetica", 12))
entry_box.pack(pady=10)

guess_button = tk.Button(window, text="Guess", font=("Helvetica", 12), command=check_guess)
guess_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

new_game_button = tk.Button(window, text="New Game", font=("Helvetica", 12), command=new_game)
new_game_button.pack(pady=10)

# Start a new game on load
new_game()

# Start the Tkinter event loop
window.mainloop()
