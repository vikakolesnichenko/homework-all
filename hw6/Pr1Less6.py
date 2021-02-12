# Создать словарь оценок предполагаемых студентов (Ключ - ФИ студента, значение - список оценок студентов).
# Найти самого успешного и самого отстающего по среднему баллу.
students = {}
s = []
a = {'Иванов Иван':(6,5,9), 'Петров Петр':(5,8,10), 'Андреев Андрей':(9,8,10), 'Борисов Борис':(6,5,3)}
for i in a.values():
    d = [float(sum(i)) / len(i)]
    s.append(d)
keys = a.keys()
for z in keys:
    dict1 = dict(zip(keys, s))

min_ball = min(dict1, key=dict1.get)
print(min_ball, 'has a minimum GPA')

max_ball = max(dict1, key=dict1.get)
print(max_ball, 'has a maximum GPA')