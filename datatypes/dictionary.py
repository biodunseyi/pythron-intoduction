# dictionaries

student1_bio = {
  'name': "Bayo",
  'student_number': 1234,
  'SO': "Oyo",
  'Faculty': "Faculty of Computy Science"
}

student2_bio = {
  'name' : "Seyi",
  'student_number' : 901732,
  'So': "Lagos",
  'Faculty' : "Faculty of Animal Husbandry"
}

student3_bio = {
  'name' : "Yemi",
  'student_number' : 657573,
  'So': "Ogun",
  'Faculty' : "Faculty of Art" 
}

student4_bio = {
   'name' : "Khalid",
  'student_number' : 67892,
  'So': "Enugu",
  'Faculty' : "Faculty of Science"
}

students = [student1_bio, student2_bio, student3_bio, student4_bio]

names = []
id_numbers = []
faculties = []


for value in students:
  names.append(value['name'])
 
print(f'Names of students are {names}')


for number in students:
  id_numbers.append(number['student_number'])

print(f'Student numbers are {id_numbers}')

for department in students:
  faculties.append(department['Faculty'])

print(f'faculties are {faculties}')




# dictionaries

student1_bio = {
  'name': "Bayo",
  'student_number': 1234,
  'course': "Bayo",
  'Course':"Integrated mathematics and computer science",
  'SO': "Oyo",
  'Faculty': "Faculty of Computy Science"
}

print(f'The name of the student is {student1_bio["name"]}')
print(f'The student course is {student1_bio["course"]}')