from datetime import datetime

def get_birthday(age):
  year = datetime.today().year
  return year - int(age)


# Write a program to calculate the area of a rectangle given its length and width.
def get_area(length, breath):
  return length * breath

# Create a program that converts temperature from Fahrenheit to Celsius.
def convert_fahrenheit_to_celcius(value):
  celsius = (value- 32) * 5/9
  return celsius


# Implement a simple calculator that can perform basic arithmetic operations.

# Implement a guessing game where the user needs to guess a random number.
import random


def check_guesses(guessed_number):
  random_number = random.randint(1, 9)
  if guessed_number == random_number:
    print("You guessed right")
  else:
    print("You guessed wrong")

# Write a function that calculates the factorial of a given number.

from math import factorial
def get_factorial(num):
  return factorial(num)

# Implement a function that returns the sum of all numbers in a list.
