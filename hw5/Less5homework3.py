#Разбираемся, что делает функция zip, и пробуем написать свой собственный zip.
l = ['a', 8, 9, 7, 12, 'lk']
z = [1, 54, 35, 2, 1, 6, 9]

def myzip(*param):
    minlen = min(len(S) for S in param)
    return [tuple(S[i] for S in param) for i in range(minlen)]

print(myzip(l, z))