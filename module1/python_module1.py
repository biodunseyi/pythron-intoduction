# args and kwargs
[12, 3, 99]
# ()


def get_sum(*args):
  i = 0
  # total = 0
  args = list(args)
  while i < len(args):
    print(args)
    number = args.pop(0)
    print(number)
  #   total += number
  # return total


# total = get_sum(12, 13, 19, 25)

num_list = []
n = True
while n:
  number = float(input("Enter a number now: "))
  num_list.append(number)
  prompt = input("Do you want to add another number? y/n:  ")
  if prompt.lower() == "y":
    continue
  else:
    total = get_sum(num_list)

print(total)




def get_average(*args):
  total = sum(args) / len(args)
  return total
n = True
num_list = []

while n:
  number_input = int(input("Enter a number:"))
  num_list.append(number_input)
  prompt = input("Do you wish to continue? y/n: ")
  if prompt.lower() == "y":
    continue
  else:
    avg_val = get_average(*num_list)
    n = False
print(avg_val)
  
