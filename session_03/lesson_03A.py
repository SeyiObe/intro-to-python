name = input("What's your name? ")

if name == "Bob":
    print("Welcome Bob!")

if name != "Alice":
    print("You're not Alice")

password = input("Please enter the password ")

correct_password = "qwerty123"

if password == correct_password:
  print("You have successfully logged in")
else:
  print("Password failure")

number = int(input("Enter a number "))

if number % 2 == 0:
  print("even")
else: 
  print("odd")

number1 = int(input("Enter a number "))
number2 = int(input("Enter another number "))

if (number1 + number2) > 21:
  print("Bust")
else: 
  print("Safe")

length = int(input("Enter the length "))
width = int(input("Enter the width "))

if length == width:
  print("This is a square")
else:
  print("This is not a square")

current_salary = int(input("Enter your current salary "))
years_of_service = int(input("How many years have you been working here? "))

if years_of_service >= 3:
  print("Current salary:\n" + str(current_salary) + "\nBonus:\n" + str(current_salary*0.1) + ".")
else:
  print("Current salary:\n" + str(current_salary) + "\nBonus:\nNo Bonus")

value = int(input("Enter a number. "))
if value > 0:
  print(value ** 3)
else:
  print(value/2)
