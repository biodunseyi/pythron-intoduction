#Write a function called reverse_string that takes a string as a parameter and returns the reverse of the input string.

def reverse_string(sentence):
  rev_sentence = sentence[::-1]
  print(rev_sentence[::])

reverse_string(sentence=[20, 34])

sentence = "name"
sentence = 32
sentence = True

#Write a function called count_vowels that takes a string as a parameter and returns the count of vowels (a, e, i, o, u) in the string.

name =input("Enter a name:")
def count_vowels(name):
  # name =input("Enter a name: ") #local
  total_vowel = 0
  for i in name:
    if i in "aeiouAEIOU":
      print(f"{i} is a vowel")
      total_vowel += 1
  print(f'There are {total_vowel} vowel in {name} ')

count_vowels(name)
  


#Write a function called is_palindrome that takes a string as a parameter and returns True if the string is a palindrome (reads the same forwards and backwards), and False otherwise.

def is_palindrome(value):
  rev_value = value[::-1]
  if rev_value == value:
    print(True)
    return "I am a palindrome"
  else:
    print(False)
    return "Not a Palindrome"

chars = input("Enter your desired value: ")

is_palindrome(chars)

print(f"your name is {name}")