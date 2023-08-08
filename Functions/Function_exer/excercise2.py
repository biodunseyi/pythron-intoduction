# Exercise 2:
# Write a function called sum_even_numbers that takes an integer n as input and returns the sum of all even numbers from 1 to n.

def sum_even():
  n = int(input("Enter a number:"))
  sum = 0
  for i in range(1,n+1):
    if i % 2 == 0:
      sum = sum + i
  print(sum)
sum_even()