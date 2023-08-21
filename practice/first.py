from datetime import datetime

today = datetime.today()

print("""
This program takes different user inputs and stores their information in a dictionary
""")

statement = True
students_bio = {}
student_id = 1
def get_user_info():
  name = input("Enter Your full name Here: ")
  grade = input("What grade are you : ")
  year = int(input("Enter your year of birth: "))
  age = today.year - year
  school = input("Enter Your School name: ")
  students_bio[student_id] = {
    "name": name,
    "age": age,
    "school": school,
    "dob": year,
    "grade": grade
  }

while statement:
  get_user_info()
  student_id += 1
  response = input("Do you want to continue adding student information? y/n ")
  if response.lower() == "y":
    continue
  elif response.lower() == "n":
    break
  else:
    print("Invalid Input you are by default getting y")
    continue


def find_student_by_id(id_num):
  student = students_bio.get(id_num, "User not registered")
  print(f'Your name is {student["name"]}, and a {student["grade"]} student in the {student["school"]} university. \n You are {student["age"]} years old.')


query = input("Do you lot want to find a student from the database y/n: ")
if query.lower() == "y":
  id_num = int(input("Enter the student ID: "))
  find_student_by_id(id_num)