import tkinter as tk
import random

# Set up the game window
window = tk.Tk()
window.title("Guess the Number")
window.geometry("300x150")

# Generate a random number for the user to guess
secret_number = random.randint(1, 100)

# Define the game logic
def check_guess():
    guess = int(guess_entry.get())
    if guess == secret_number:
        result_label.config(text="You win!")
    elif guess < secret_number:
        result_label.config(text="Too low!")
    else:
        result_label.config(text="Too high!")

# Create the user interface
guess_label = tk.Label(window, text="Guess a number between 1 and 100:")
guess_label.pack(pady=10)

guess_entry = tk.Entry(window)
guess_entry.pack()

submit_button = tk.Button(window, text="Submit", command=check_guess)
submit_button.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack()

# Start the game
window.mainloop()
