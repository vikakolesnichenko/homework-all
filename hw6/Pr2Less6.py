#Создать структуру данных для студентов из имен и фамилий, можно случайных.
# Придумать структуру данных, чтобы указывать, в какой группе учится студент(Группы
# Python, FrontEnd, FullStack, Java).
# Студент может учиться в нескольких группах. Затем вывести:

all = {'ivanov ivan', 'kvach denis', 'bogdanov bogna', 'vika kotova', 'liza simpson', 'ira kaz', 'vasia pupkin', 'kris smit', 'sasha zaderey', 'lena kaptur', 'artem nikitin'}
Python = {'ivanov ivan', 'kvach denis', 'bogdanov bogna', 'vika kotova', 'liza simpson', 'ira kaz'}
FrontEnd = {'ivanov ivan', 'liza simpson', 'vasia pupkin'}
FullStack = {'kris smit', 'sasha zaderey', 'bogdanov bogna'}
Java = {'lena kaptur', 'artem nikitin', 'liza simpson'}

# студенты, которые учатся в двух и более группах
p1 = all & Python & FrontEnd
p2 = all & Python & FullStack
p3 = all & Python & Java
P = p1 | p2 | p3
fr1 = all & FrontEnd & FullStack
fr2 = all & FrontEnd & Java
FR = fr1 | fr2
fs1 = all & FullStack & Java
final = P | FR | fs1
print(final)

# студентов, которые не учатся на фронтенде
Fr = ((Python | FullStack) | Java) - FrontEnd
print(Fr)

# студентов, которые изучают Python или Java
PJ = (Python | Java)
print(PJ)