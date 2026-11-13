# Guess the Number

[![CI](https://github.com/Logesh2097/Game_guessingnos/actions/workflows/ci.yml/badge.svg)](https://github.com/Logesh2097/Game_guessingnos/actions/workflows/ci.yml)

A small desktop number-guessing game written in Python with Tkinter.

## Overview

The game picks a secret number between 1 and 100. Type a guess and it answers
"Too low!", "Too high!" or "You win!" with the number of tries it took. Written
as a learning project for Tkinter and event-driven code.

## Features

- Guess with the Submit button or the Enter key.
- Counts your tries and reports them when you win.
- Text that is not a whole number, or is out of range, gets a message and is not counted as a try.
- A "New game" button starts another round without restarting the program.
- The game rules are separate from the window, so they are tested without a display.
- No third-party dependencies.

## Architecture

One file, two parts:

| Part | Responsibility |
|---|---|
| `GuessingGame` | The rules: holds the secret number, validates a guess, counts tries, returns the message |
| `build_window()` | The Tkinter window: reads the entry box, calls `GuessingGame.guess()`, shows the message |

## Technology stack

Python 3.10+ and Tkinter (both in the standard library). ruff and GitHub Actions for checks.

## Project structure

```
.
├── guess_the_number.py
└── tests/
    └── test_game.py
```

## Installation and running

Tkinter ships with the python.org installers for Windows and macOS. On
Debian or Ubuntu, install it with `sudo apt install python3-tk`.

```bash
git clone https://github.com/Logesh2097/Game_guessingnos.git
cd Game_guessingnos
python guess_the_number.py
```

There are no environment variables.

## Testing

```bash
python -m unittest discover -s tests -v
ruff check .        # pip install ruff
```

The rule tests run anywhere. The three window tests need Tkinter and a
display and are skipped without them; in GitHub Actions they run under a
virtual display (`xvfb-run`).

## Future improvements

- Difficulty levels with different ranges.
- A limit on the number of tries.
- A best-score record kept between runs.
