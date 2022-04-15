import random


class SecretNumber:
    def __init__(self, upper_limit):
        self.secret_number = random.randrange(1, upper_limit)
        self.guesses = 4
        self.correct = False

    def guess_number(self, guess):
        if self.guesses != 0:
            if guess > self.secret_number:
                print("Too high, guess lower")
                self.guess_counter()
            elif guess < self.secret_number:
                print("Too low, guess higher")
                self.guess_counter()
            else:
                print("Correct!")
                self.correct = True
        else:
            print(f"Sorry, no more guesses! The number was {self.secret_number}")
            self.correct = True

    def guess_counter(self):
        print(f"Guesses left: {self.guesses}")
        self.guesses -= 1
