fizz = int(input())
buzz = int(input())
numb = int(input())
l = []
st = 0
while st < numb:
    st += 1
    if (not st % fizz) and (not st % buzz):
        l.append('FB')
    if (not st % fizz) and st % buzz:
        l.append('F')
    if not (st % buzz) and st % fizz:
        l.append('B')
    if (st % fizz) and (st % buzz):
        l.append(str(st))
s = ' '.join(str(i) for i in l)
print(s)