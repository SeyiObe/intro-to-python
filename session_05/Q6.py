numbers = [];

i = 0

while i < 10:
  entry = int(input("Please enter a number. One number should be 99.\n"))
  numbers.append(entry)
  i += 1

for i in range(len(numbers)):
  if numbers[i] == 99:
    print("Number 99 is at index " + str(i))
  i += 1