items = []

# max_val = 3

# while max_val > 0:
#   goods = input("Enter an item of your choice: ")
#   items.append(goods)
#   max_val -= 1
#   print(f"{goods} has been added. You have {max_val} extra inputs..")

# print(sorted(items))

number_list = []

max_num_val = 4
while max_num_val > 0:
  number = input("Enter a random Number: ")
  if number.lower() == "stop":
    break
  elif not number.isdigit():
    print("Number is not whole number")
    continue
  else:
    number_list.append(number)
    max_num_val -= 1

print(number_list)