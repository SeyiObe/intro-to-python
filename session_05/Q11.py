import random

print("Let's play rock, paper, scissors")

user_score = 0
computer_score = 0
turns = 0
options = ["rock", "paper", "scissors"]

while turns < 3:
  user_choice = input("Choose rock, paper or scissors\n")
  computer_choice = random.choice(options)
  print("You picked " + user_choice)
  print("The computer picked " + computer_choice)
  turns += 1
  print("This is turn " + str(turns))
  if user_choice == "rock":
    if computer_choice == "scissors":
      print("You win")
      user_score += 1
    elif computer_choice == "paper":
      print("You lose")
      computer_score += 1
    else:
      print("It's a draw")
  elif user_choice == "paper":
    if computer_choice == "rock":
      print("You win")
      user_score += 1
    elif computer_choice == "scissors":
      print("You lose")
      computer_score += 1
    else:
      print("It's a draw")
  elif user_choice == "scissors":
    if computer_choice == "paper":
      print("You win")
      user_score += 1
    elif computer_choice == "rock":
      print("You lose")
      computer_score += 1
    else:
      print("It's a draw")  

print("Game Over! Final Score: You: " + str(user_score) + "\n Computer: " + str(computer_score))