#Банкомат выдает сумму максимально возможными купюрами
bankomat = [1000, 500, 200, 100, 50, 20, 10]
tmp = 1
r = []
while tmp % 10 != 0:
    tmp = int(input())
    if tmp % 10 != 0:
        print('enter another amount')
    while tmp < 0:
        tmp = int(input())
        if tmp < 0:
            print('enter another amount')
for i in bankomat:
    result = 0
    while tmp >= i:
        tmp -= i
        result +=1
        r.append(i)
print(r)