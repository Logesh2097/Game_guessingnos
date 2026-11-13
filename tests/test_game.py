import os
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from guess_the_number import GuessingGame, InvalidGuess, build_window  # noqa: E402


class GuessingGameTests(unittest.TestCase):
    def test_a_low_guess_is_called_too_low(self):
        self.assertEqual(GuessingGame(secret=50).guess("10"), "Too low!")

    def test_a_high_guess_is_called_too_high(self):
        self.assertEqual(GuessingGame(secret=50).guess("90"), "Too high!")

    def test_the_right_guess_wins_and_reports_the_attempts(self):
        game = GuessingGame(secret=50)
        game.guess("10")
        game.guess("90")

        message = game.guess("50")

        self.assertTrue(game.won)
        self.assertEqual(message, "You win! It took you 3 tries.")

    def test_winning_first_time_says_one_try(self):
        self.assertEqual(GuessingGame(secret=7).guess("7"), "You win! It took you 1 try.")

    def test_text_that_is_not_a_number_is_rejected_and_not_counted(self):
        game = GuessingGame(secret=50)

        for text in ("", "abc", "4.5", "ten"):
            with self.subTest(text=text), self.assertRaises(InvalidGuess):
                game.guess(text)

        self.assertEqual(game.attempts, 0)

    def test_a_number_out_of_range_is_rejected(self):
        game = GuessingGame(secret=50)

        for text in ("0", "101", "-5"):
            with self.subTest(text=text), self.assertRaises(InvalidGuess):
                game.guess(text)

    def test_spaces_around_the_number_are_allowed(self):
        self.assertEqual(GuessingGame(secret=50).guess(" 50 ")[:8], "You win!")

    def test_the_secret_is_always_inside_the_range(self):
        for _ in range(200):
            game = GuessingGame(lowest=3, highest=5)
            self.assertIn(game._secret, (3, 4, 5))


def display_available():
    try:
        import tkinter  # noqa: F401
    except ImportError:
        return False
    return sys.platform == "win32" or bool(os.environ.get("DISPLAY"))


@unittest.skipUnless(display_available(), "needs Tkinter and a display")
class WindowTests(unittest.TestCase):
    def setUp(self):
        self.window = build_window(GuessingGame(secret=42))
        self.addCleanup(self.window.destroy)

    def submit(self, text):
        self.window.guess_entry.insert(0, text)
        self.window.submit_button.invoke()
        return self.window.result_label.cget("text")

    def test_a_guess_shows_its_result_and_clears_the_box(self):
        self.assertEqual(self.submit("10"), "Too low!")
        self.assertEqual(self.window.guess_entry.get(), "")

    def test_bad_input_shows_a_message_instead_of_an_error(self):
        self.assertEqual(self.submit("abc"), "Enter a whole number.")

    def test_winning_disables_the_submit_button(self):
        self.assertIn("You win!", self.submit("42"))
        self.assertEqual(str(self.window.submit_button.cget("state")), "disabled")


if __name__ == "__main__":
    unittest.main()
