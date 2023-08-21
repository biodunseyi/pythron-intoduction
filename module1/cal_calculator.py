from calculator import get_sum, get_diff, get_exponent, get_product, get_div

print("""This code does basic calculations like addition, subtraction, division, multiplication, and exponents.

It can only take two values for calculation

a = addition
m = multiplication
d = division
e = exponent
s = subtraction
""")


operations = True

while operations:
  calculation_input = input("What mode of calculation do you want to perform? ")
  
  first_val = float(input("Enter the first number: "))
  second_val = float(input("Enter the second number: "))

  if calculation_input.lower() == "a":
    total = get_sum(first_val, second_val)
    print(f"The total value is {total}")
    prompt = input("Do you want to continue this operation? y for yes and n for no: ")
    if prompt.lower() == "y":
      continue
    else:
      operations = False
  elif calculation_input.lower() == "m":
    total = get_product(first_val, second_val)
    print(f"The product is {total}")
    prompt = input("Do you want to continue this operation? y for yes and n for no: ")

    if prompt.lower() == "y":
      continue
    else:
      operations = False  
  elif calculation_input.lower() =="d":
    total = get_div(first_val, second_val)
    print(f"The diision is {total}")
    prompt = input("Do you want to continue this operation? y for yes and n for no: ")
    if prompt.lower() == "y":
      continue
    else:
      operations = False

  elif calculation_input.lower() =="e":
    total = get_exponent(first_val, second_val)
    print(f"The exponent of {first_val} raise to power {second_val} is {total}")
    prompt = input("Do you want to continue this operation? y for yes and n for no: ")

    if prompt.lower() == "y":
      continue
    else:
      operations = False

  elif calculation_input.lower() == "s":
    total = get_diff(first_val, second_val)
    print(f"The value is {total}")
    prompt = input("Do you want to continue this operation? y for yes and n for no: ")
    if prompt.lower() == "y":
      continue
    else:
      operations = False
  else:
    print("Invalid response...")
else:
  print("Thank you for using our calculator app. Have a nice day.")