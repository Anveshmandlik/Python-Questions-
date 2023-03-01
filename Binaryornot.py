stringA = input()

b = '10'
count = 0
for char in stringA:
   if char not in b:
      count = 1
      break
   else:
      pass
if count:
   print("StringA is not a binary string")
else:
   print("StringA is a binary string")
