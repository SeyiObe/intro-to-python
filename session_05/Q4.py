correct_password = "qwerty123"
password = input("Enter password\n")
counter = 0

while counter < 2:
  if password == correct_password:
    print("You have successfully logged in")
    break
  else:
    print("Password failure\n")
    password = input("Enter password again\n")
    counter += 1
if counter == 2:
  print("System locked")