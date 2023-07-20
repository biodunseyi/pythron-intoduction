# Write a Python program that takes a year as input and determines if it is a leap year or not. A leap year is divisible by 4 but not divisible by 100, except if it is also divisible by 400. Print "Leap year" if it is a leap year, and "Not a leap year" otherwise.

print("This code determines if your input is a leap year or not./n")

year = int(input("Enter Year: "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not a leap year")
  else:
    print("Leap year")
else:
  print("Not a leap year")
