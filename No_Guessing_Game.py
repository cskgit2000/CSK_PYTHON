import random

lower = int(input("Enter lower bound: "))
upper = int(input("Enter upper bound: "))
number = random.randint(lower, upper)
attempts = 0

while True:
    guess = int(input("Guess the number: "))
    attempts += 1
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break
