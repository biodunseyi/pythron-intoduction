def get_user_bio():
  name = input("what is your name?")
  DOB = int(input("What year were you born:"))
  year = 2023
  age = year - DOB
  print(f'Your name is {name} and your are {age} years old')

get_user_bio()



def get_user_bio(year,name,DOB):
  # name = input("what is your name?")
  # DOB = int(input("What year were you born:"))
  
  age = year - DOB  
  print(f'Your name is {name} and your are {age} years old')
name = input("What is your name:")
year = int(input("What year is this:"))
DOB = int(input("What year were you born:"))
get_user_bio(year,name,DOB)

def get_date_of_birth(date):
  year = 2023
  age = year - date

  print(f'You are {age} years old')

date = int(input("Enter your birth year:"))

#get_date_of_birth(date)