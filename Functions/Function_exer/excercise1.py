# Exercise 1:
# Write a function called print_numbers that takes an integer n as input and prints all the numbers from 1 to n.

def print_numbers():
  n = int(input("Enter a number:"))
  for i in range(n+1):
    print(i)
#print_numbers()