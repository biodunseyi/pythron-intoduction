name1 = "paul olamide"
name2 = "bayo bello"

#variable swapping for all data
name1, name2 = name2, name1

print(name1.capitalize(), name2.title())

# upper, lower, title methods

# varaible naming

firstname = "ola"
first_name = "ola"
firstName = "ola"
name3 = "oooo"
# name-2 = "aaa" # not valid

# count method
word = "Do not outsmart your master"

o_count = word.count("o", 2, 10)

start_checker = word.startswith('D')
end_checker = word.endswith('r')

print(end_checker)

finder = word.find("zeus") # -1 represents values that are not in the target
indexer = word.index("zeus") # raises an ValueError for values that are not in target
print(finder)
print(indexer)