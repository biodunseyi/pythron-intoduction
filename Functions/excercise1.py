# Write a function called calculate_sum that takes two parameters, a and b, and returns the sum of a and b.


def calculate_sum(a, b):
  print(a + b)


calculate_sum(b=10, a=15)
calculate_sum(10, 20)

# Write a function called is_even that takes an integer parameter n and returns True if the number is even, and False otherwise.


def called_is_even(n):
  if n % 2 == 0:
    print(True)
  else:
    print(False)


called_is_even(5)
# Write a function called find_max that takes a list of numbers as a parameter and returns the largest number in the list.


def find_max(n):
  highest_number = max(n)
  print(f'The highest number is {highest_number}')


n = []
i = 0
while i < 5:
  inputs = float(input("Enter the numbers: "))
  if inputs < 0:
    print("Invalid Inputs")
    continue
  else:
    n.append(inputs)
    i += 1
else:
  find_max(n)
