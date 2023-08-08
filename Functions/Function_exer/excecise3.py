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
      