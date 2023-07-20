sentence = "A gunshot is probably the most terrifying sound a person can hear. It is characterized by discomfort and, consequently, destruction; This is very conversant among people in the United States. "

print(len(sentence))
print(len(sentence.strip()))
a_count = sentence.count("a", 12, 20)

print(a_count)

tence = sentence.replace("g", "a", 7)
print(tence)

wordCheck = sentence.startswith('s')
endCheck = sentence.endswith('y')
finder = sentence.find("the",30)
print(finder)
