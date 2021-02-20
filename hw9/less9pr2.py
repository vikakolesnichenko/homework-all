numb = int(input("Please enter a number: "))
if numb < 0 or (numb % 2) == 0:
    print('Error')
    exit()

elem = numb - 1
i = 1
while i <= numb:
 if not (i % 2) == 0:
  print((' ' * elem) + (i * "*" ))
  elem -= 1
 i += 1


elem += 2
k = numb - 1
while k > 0:
 if not (k % 2) == 0:
  print((' ' * elem) + k * "*")
  elem += 1
 k -= 1