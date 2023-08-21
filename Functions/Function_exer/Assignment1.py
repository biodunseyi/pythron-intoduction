# Exercise 1:
# Write a function called print_numbers that takes an integer n as input and prints all the numbers from 1 to n.

def print_numbers():
  n = int(input("Enter a number:"))
  for i in range(n+1):
    print(i)
#print_numbers()
  
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

# Exercise 3:
# Write a function called count_vowels that takes a string as input and returns the count of vowels (a, e, i, o, u) in the string.

def count_vowels():
  input_strings = input("What word would you like to check its vowel:")
  vowels = "aeiouAEIOU"
  count = 0
  for char in input_strings:
    if char in vowels:
      count += 1
  print(f'There are {count} vowels in {input_strings}')

count_vowels()
      
      
# Exercise 4:
# Write a function called factorial that takes an integer n as input and returns the factorial of n (i.e., the product of all positive integers from 1 to n).

def factorial():
  n = int(input("Enter a number:"))
  output = 1
  for i in range(1, n+1):
    output *= i
  print(output)


# Exercise 5:
# Write a function called reverse_string that takes a string as input and returns the reverse of the input string.

def reverse_string():
  input_string = input("Enter what is in your mind:")
  print(input_string[::-1])
reverse_string()  

# Exercise 6:
# Write a function called is_prime that takes an integer n as input and returns True if n is a prime number, and False otherwise.

def is_prime(n):
    if n <= 1:
        print(f"{n} is not a prime number.")
    elif n <= 3:
        print(f"{n} is a prime number.")
    elif n % 2 == 0 or n % 3 == 0:
        print(f"{n} is not a prime number.")
    else:
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                print(f"{n} is not a prime number.")
                break
            i += 6
        else:
            print(f"{n} is a prime number.")

number = int(input("Enter a number you would like to check it prime: "))
is_prime(number)

# Exercise 7:
# Write a function called find_max that takes a list of numbers as input and returns the maximum value in the list.

def find_max(numbers):
    if not numbers:
        print("The list is empty.")
    else:
        max_value = numbers.pop(0)
        for num in numbers:
            if num > max_value:
                max_value = num
        print(f"The maximum value is: {max_value}")


find_max(5)


# Exercise 8:
# Write a function called print_pattern that takes an integer n as input and prints the following pattern:

# markdown
# Copy code
# *
# **
# ***
# ****
# where the number of asterisks in each row corresponds to the row number.

# Exercise 9:
# Write a function called calculate_grade that takes a float score as input and returns the corresponding letter grade according to the following scale:

# 90 or above: 'A'
# 80-89: 'B'
# 70-79: 'C'
# 60-69: 'D'
# Below 60: 'F'

def calculate_grade(score):
    if score >= 90:
        print('A')
    elif score >= 80:
        print('B')
    elif score >= 70:
        print('C')
    elif score >= 60:
        print('D')
    else:
        print('F')

score = float(input("Enter the score: "))
calculate_grade(score)

# Exercise 10:
# Write a function called is_palindrome that takes a string as input and returns True if the string is a palindrome (reads the same forwards and backwards), and False otherwise.

def is_palindrome(value):
    rev_value = value[::-1]
    if rev_value == value:
        print(True)
        print("I am a palindrome")
    else:
        print(False)
        print("Not a Palindrome")

chars = input("Enter your desired value: ")

is_palindrome(chars)

print(f"your value is {chars}")

