def funkc1(a1):
    result = a1.upper()
    return result

def funkc2(a2):
    result = a2.lower()
    return result

l = ['Yy', 'Oo', 'Pp', 'GHJghj']
l2 = list(map(funkc1, l))
l3 = list(map(funkc2, l))
print(l2)
print(l3)