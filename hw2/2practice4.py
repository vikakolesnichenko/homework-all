n = int(input())
num = len(str(n)) #узнали кол-во разрядов
ii = 1
r = []
finish = []
while (num - ii) >= 0:
    k = 10**(num - ii) #возводим 10 в нужную стень
    ii += 1
    r.append(k) #добавляем полученное значение в список, пока не закончится цикл
l = list(str(n)) #переводим введенное число в список
for i in range(0, len(r)):
    factor = (r[i], '*', l[i]) #соединяем значение списка с составляющими числа и 10, возведенными в степень
    finish.append(factor)
print(finish)