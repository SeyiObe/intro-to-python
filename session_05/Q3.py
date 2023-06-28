from math import ceil

length = int(input("Enter length in cm\n"))
width = int(input("Enter width in cm\n"))

area = length*width
area_m = ceil(area/10000)

print("Area is " + str(area_m) + "m2")