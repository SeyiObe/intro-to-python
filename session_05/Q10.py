import random

list = []

name = None
while name != "":
  name = input("Add your name to the prize draw.\n")
  if name != "":
    list.append(name)

print("Congratulations " + random.choice(list) + " you are the winner of the prize draw!")

