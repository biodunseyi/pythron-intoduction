items = ['fish','yam','salt','rice','garri']

using breaks on for loop
for i in items:
   if i.lower() == 'salt':
     break
   else:
     print(i)


 using continue on for loop
 for i in items:
   if i.lower() == 'salt':
     continue
   else:
     print(i)

for j in items:
  print(j)
else:
  print("You are at the end of the train...")