def get_user_bio():
  name = input("what is your name?")
  DOB = int(input("What year were you born:"))
  year = 2023
  age = year - DOB
  print(f'Your name is {name} and your are {age} years old')

get_user_bio()