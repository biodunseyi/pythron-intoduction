# lists, tuples, sets, dictionaries

# Attributes of a list

# lists are ordered
fruits = ['kiwi', 'gac', 'dragon fruit', 'coconut']
print("Fruit Game!")
print("This game takes user input and check if it is available in the list")
print("You get 1 point if you guessed right and a Boo if you guessed wrong")
guessFruit = input("Enter your guessed fruit: ")

rif guessFruit.lower() in fruits:
  print(
    f'Congrats! You got a point. Your guessed fruit is {guessFruit}. and is in the list of fruits'
  )
else:
  print("Boo! what a dummy, You guessed wrong.")
