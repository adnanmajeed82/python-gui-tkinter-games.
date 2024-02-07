import tkinter as tk
import random

class GuessingGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Guessing Game")
        self.geometry("300x150")
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(self, text="Guess a number between 1 and 100:")
        self.label.pack()

        self.entry = tk.Entry(self)
        self.entry.pack()

        self.button = tk.Button(self, text="Guess", command=self.check_guess)
        self.button.pack()

        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

    def check_guess(self):
        guess = int(self.entry.get())
        self.attempts += 1

        if guess < self.secret_number:
            self.result_label.config(text="Too low! Try again.")
        elif guess > self.secret_number:
            self.result_label.config(text="Too high! Try again.")
        else:
            self.result_label.config(text=f"Congratulations! You guessed the number in {self.attempts} attempts.")

if __name__ == "__main__":
    game = GuessingGame()
    game.mainloop()
