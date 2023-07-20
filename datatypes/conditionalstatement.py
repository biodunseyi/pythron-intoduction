# Condtional Statements

# if, elif and else

name = input("Enter Your Name: ")
gender = input("Choose Male/Female/Non Binary: ")

if gender.title() == "Male":
  print(f"Name is {name.title()} can be addressed as he")
elif gender.title() == "Female":
  print(f"Name is {name.title()} can be addressed as she")
elif gender.title() == "Non Binary":
  print(f"Name is {name.title()}. You are delusional.")
else:
  print(f"Invalid Input. Your input is {gender}")