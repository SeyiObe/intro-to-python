import random

number = random.randint(1,10)
guess = None

while guess != number:
  guess = int(input("Choose a number.\n"))
print("You guessed the correct number!!")