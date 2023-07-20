# Write a Python program that takes two numbers as input and determines if the first number is greater than, less than, or equal to the second number. Print the corresponding message based on the condition.
print(
  "This code check if the first number is the same, lesser than or greater than the first number"
)
dig1 = float(input("Enter Your First Number: "))
dig2 = float(input("Enter Your Second Number: "))

if dig1 > dig2:
  print(f'{dig1} is greater than {dig2}')

elif dig1 < dig2:
  print(f'{dig2} is greater than {dig1}')

elif dig1 == dig2:
  print(f' {dig1} and {dig2} are equal')

else:
  print("Invalid input...")