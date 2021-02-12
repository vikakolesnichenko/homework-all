#Переделать вторую задачу так, чтобы результат писался в другой файл.
f = open('For_fizzBuzz.txt', 'r')
lo = f.readlines()
l2 =[]
for i, lin in enumerate(lo):
    l1 = lin.split()
    fizz = int(l1[0])
    buzz = int(l1[1])
    numb = int(l1[2])
    st = 0
    l = []
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
    l2.append(s + '\n')
f.close()
f1 = open('writeFizzBuzz.txt', 'w')
f1.writelines(l2)
f1.close()