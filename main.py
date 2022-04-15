from secret_number import SecretNumber

print("Welcome to Guess the Number!")
secret_number = SecretNumber(int(input("Enter the upper limit of the secret number: ")))
while not secret_number.correct:
    secret_number.guess_number(int(input("Guess the secret number: ")))
