"""Guess the Number: a small Tkinter game.

The game rules live in ``GuessingGame`` and know nothing about the window,
so they can be tested without a display.
"""

from __future__ import annotations

import random

LOWEST = 1
HIGHEST = 100


class InvalidGuess(ValueError):
    """The text entered is not a whole number in range."""


class GuessingGame:
    """One round: a secret number and the guesses made so far."""

    def __init__(self, lowest: int = LOWEST, highest: int = HIGHEST, secret: int | None = None):
        if lowest > highest:
            raise ValueError("lowest must not be greater than highest")
        self.lowest = lowest
        self.highest = highest
        self.attempts = 0
        self.won = False
        self._secret = random.randint(lowest, highest) if secret is None else secret  # noqa: S311

    def parse(self, text: str) -> int:
        """Turn what the player typed into a number, or raise ``InvalidGuess``."""
        try:
            guess = int(text.strip())
        except ValueError:
            raise InvalidGuess("Enter a whole number.") from None
        if not self.lowest <= guess <= self.highest:
            raise InvalidGuess(f"Enter a number between {self.lowest} and {self.highest}.")
        return guess

    def guess(self, text: str) -> str:
        """Count a guess and return the message to show the player."""
        number = self.parse(text)
        self.attempts += 1
        if number < self._secret:
            return "Too low!"
        if number > self._secret:
            return "Too high!"
        self.won = True
        tries = "try" if self.attempts == 1 else "tries"
        return f"You win! It took you {self.attempts} {tries}."


def build_window(game: GuessingGame | None = None):
    """Create the game window and return it. Call ``mainloop()`` on it to play."""
    import tkinter as tk

    window = tk.Tk()
    window.title("Guess the Number")
    window.geometry("320x190")
    window.game = game or GuessingGame()

    def check_guess(_event=None):
        if window.game.won:
            return
        try:
            message = window.game.guess(guess_entry.get())
        except InvalidGuess as problem:
            message = str(problem)
        result_label.config(text=message)
        guess_entry.delete(0, tk.END)
        if window.game.won:
            submit_button.config(state=tk.DISABLED)

    def new_game():
        window.game = GuessingGame()
        result_label.config(text="")
        submit_button.config(state=tk.NORMAL)
        guess_entry.delete(0, tk.END)
        guess_entry.focus_set()

    tk.Label(window, text=f"Guess a number between {LOWEST} and {HIGHEST}:").pack(pady=10)

    guess_entry = tk.Entry(window)
    guess_entry.pack()
    guess_entry.bind("<Return>", check_guess)
    guess_entry.focus_set()

    submit_button = tk.Button(window, text="Submit", command=check_guess)
    submit_button.pack(pady=10)

    result_label = tk.Label(window, text="")
    result_label.pack()

    tk.Button(window, text="New game", command=new_game).pack(pady=5)

    # Exposed so a test can drive the window.
    window.guess_entry = guess_entry
    window.submit_button = submit_button
    window.result_label = result_label
    return window


def main() -> None:
    build_window().mainloop()


if __name__ == "__main__":
    main()
