Flat_number = int(input())
if (1 > Flat_number > 4):
    print('it is first floor')
elif (5 > Flat_number > 8):
    print('it is second floor')
elif (9 > Flat_number > 12):
    print('it is third floor')
else:
    print('go to the next entrance')

a = int(input())
b = int(input())
c = int(input())

k = a
if k < b:
    k = b
if k < c:
    k = c

