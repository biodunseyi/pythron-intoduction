# lists, tuples, sets, dictionaries
"""
  lists are orderable
  lists can take any data type including self
  list can be modified
"""
item = ['garri', 'groundnut', 'sugar', 'Milk']

# item[:3] = ["Golden Morn", 'Straw Berry', 'chocolate'] ## modifying an item
# appending, removing from the list
item[1:3] = ['kulikuli', 'salt']
#print(item)

groceries = ['cookie', 'corn flakes', 'golden morn']
foodStuff = ['Yam', 'Yice', 'Yauce']

# appending/adding to a list

# item = item + groceries
# item += groceries
item.append(groceries)
#print(item)

random_ages = [23, 32, 13, 44, 25, 19]

groceries += foodStuff
# print(len(groceries)) # prints out the length of a list

print(max(foodStuff))  
# min() and max() methods are used to get the lower and higher value in our list


# lists, tuples, sets, dictionaries
"""
  lists are orderable
  lists can take any data type including self
  list can be modified
"""
item = ['garri', 'groundnut', 'sugar', 'Milk']
fruits = ['banana', 'mango', 'pawapaw']

groceries = []
groceries.extend(item)
groceries.extend(fruits)


# groceries.append(item)
# groceries.append(fruits)

groceries.append("Honey")


groceries.pop(-1)

groceries[:4] = [f"Garri Smoothie = {groceries[:4]}"]
print(groceries)
print(len(groceries))