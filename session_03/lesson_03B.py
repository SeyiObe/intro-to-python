name = input("What's your name? ")

if name == "Alice":
  print("Hello Alice")
elif name == "Bob":
  print("Hello Bob")
else:
  print("You must be Charlie")

age = int(input("How old are you? "))
if age == 0:
  print("You're not born yet!")
elif age < 11:
  print("You're too young to go to this school")
elif age < 16:
  print("You can come to this school")
else:
  print("You're too old for school")

month = input("Enter a month of the year. ")
if month == "January" or month == "February" or month == "December":
  print(month + " is in winter.")
elif month == "March" or month == "April" or month == "May":
  print(month + " is in spring.")
elif month == "June" or month == "July" or month == "August":
  print(month + " is in summer.")
elif month == "September" or month == "October" or month == "November":
  print(month + " is in autumn.")
else:
  print("I don't know.")

number1 = int(input("Enter a number "))
number2 = int(input("Enter another number "))

if number1 % 2 == 0 and number2 % 2 == 0:
  print("Even")
if number1 % 2 != 0 and number2 % 2 != 0:
  print("Odd")
else:
  print(number1*number2)

if number1 > number2:
  print(number1)
else:
  print(number2)

current_salary = int(input("Enter your current salary "))
years_of_service = int(input("How many years have you been working here? "))

if years_of_service > 7:
  print("Current salary:\n" + str(current_salary) + "\nBonus:\n" + str(current_salary*0.2) + ".")
elif years_of_service > 5:
  print("Current salary:\n" + str(current_salary) + "\nBonus:\n" + str(current_salary*0.15) + ".")
elif years_of_service >= 3:
  print("Current salary:\n" + str(current_salary) + "\nBonus:\n" + str(current_salary*0.1) + ".")
else:
  print("Current salary:\n" + str(current_salary) + "\nBonus:\nNo Bonus")

name1 = input("What's your name? ")
age1 = int(input("What's your age? "))

name2 = input("What's your name? ")
age2 = int(input("What's your age? "))

name3 = input("What's your name? ")
age3 = int(input("What's your age? "))

if age1 > age2 and age1 > age3:
  print(name1 + " is the oldest and they are " + str(age1))
elif age2 > age1 and age2 > age3:
  print(name2 + " is the oldest and they are " + str(age2))
elif age3 > age1 and age3 > age2:
  print(name3 + " is the oldest and they are " + str(age3))
else:
  print("You're all the same age")

if age1 < age2 and age1 < age3:
  print(name1 + " is the youngest and they are " + str(age1))
elif age2 < age1 and age2 < age3:
  print(name2 + " is the youngest and they are " + str(age2))
elif age3 < age1 and age3 < age2:
  print(name3 + " is the youngest and they are " + str(age3))
else:
  print("You're all the same age")

mark1 = int(input("Enter your mark for lesson 1. "))

mark2 = int(input("Enter your mark for lesson 2. "))

mark3 = int(input("Enter your marks for lesson 3. "))



