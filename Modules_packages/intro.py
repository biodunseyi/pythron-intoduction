import time
import datetime
import math

number = int(input("Enter any number of your choice:"))

root_number = number ** 0.5

print(root_number)


def factorial():
  n = int(input("Enter a number:"))
  output = 1
  for i in range(1, n+1):
    output *= i
  print(output)

factorial()