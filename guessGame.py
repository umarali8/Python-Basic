import random

jackpot = random.randint(1, 100)

print(" Welcome to the Guess Game!")
print("I have selected a number between 1 and 100.")

counter = 1


guess = int(input("Enter your guess: "))


while guess != jackpot:
    if guess < jackpot:
        print(" Guess Higher!")
    else:
        print(" Guess Lower!")

    guess = int(input("Try again: "))
    counter += 1

print("\n Congratulations!")
print(f"You guessed the correct number: {jackpot}")
print(f"You took {counter} attempts.")