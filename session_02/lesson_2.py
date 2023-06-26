width = 4
height = 3
area = width*height
print("Rectangle of width " + str(width) + " and height " + str(height) + " has an area of " + str(area))

string = "python"
print(len(string))

print(string[0])
print(string[2])

name = input("What's your name? ")
print("Hello " + name)

age = int(input("How old are you? "))
adjusted_age = age + 15
print("In 15 years, you will be " + str(adjusted_age))

print("Hello "+ name + ", you are currently " + str(age) + " years old. In 15 years time you will be " + str(adjusted_age) + ".")

hometown = input("What's your hometown? ")
print(hometown.upper())

fav_color = input("What's your favourite color? ")
print(len(fav_color))

month = input("What month is it? ")
weather = input("How hot is it today? ")
print("It is " + month + " and it is " + weather + "C today")

temp1 = int(input("What's the weather on Monday? "))
temp2 = int(input("What's the weather on Tuesday? "))
temp3 = int(input("What's the weather on Wednesday? "))
temp4 = int(input("What's the weather on Thursday? "))
temp5 = int(input("What's the weather on Friday? "))

average_temp = (temp1 + temp2 + temp3 + temp4 + temp5)/5
print("It is " + month + " and the average temperature is " + str(average_temp) + " degrees celsius")

print("It is " + month.upper() + " and the average temperature is " + str(average_temp) + " degrees celsius")

favourite_animals = "dog\n\tcat\n\tfish\n\tchicken\n\tgoat"
print(favourite_animals)

number = int(input("Pick a number between 0 and " + str(len(name) - 1) + "? "))
print(name[number].upper())

str = "WelcometoPython"
print(str[1:-1:2])

