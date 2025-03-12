# Loops

# for and while

# .pop()

# name is Famel
# name is seyi
# name is riky

namesPeople = ['Bola', 'Yemi', 'Riky', 'Seyi', 'Famel']
name_len = len(namesPeople)


while name_len > 0:
  last_name = namesPeople[-1]
  print(f'The last name on the names list is {last_name}')
  namesPeople.pop(-1)
  name_len = len(namesPeople)
  print(name_len)

