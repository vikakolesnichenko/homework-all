from datetime import date, timedelta
# Создать класс  Employee.
# Хранить в нём данные о работнике (Имя, почту, ЗП за один рабочий день).
class Employee:
    def __init__(self, name, email, zp):
        self.name = name
        self.email = email
        self.zp = zp
    # Создать метод work(...) который возвращает строку “I come to the office.”
    def work(self):
        return f"I come to the office"
    #Создать метод check_salary(...)
    # - который позволит посчитать ЗП за указанное количество рабочих дней.
    def check_selary(self, zp):
        now = date.today()
        month_start = date(now.year, now.month, 1)
        diff = (now - month_start).days + 1
        count_sell = zp * diff
        return count_sell

    # Создать метод, который сравнивает сотрудников по уровню ЗП.

    def __gt__(self, other):
        return self.zp > other.zp

    def __ge__(self, other):
        return self.zp >= other.zp

    def __lt__(self, other):
        return self.zp < other.zp

    def __le__(self, other):
        return self.zp <= other.zp

    def __eq__(self, other):
        return self.zp == other.zp

    def __ne__(self, other):
        return self.zp != other.zp

#Создать классы Recruiter и Programmer, которые наследуются от Employee
class Recruiter(Employee):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
#Переопределить методы work() которые будут использовать метод родителя и возвращать:
#“I come to the office and start to coding.” - для Programmer
#“I come to the office and start to hiring.” - для Recruiter
    def work(self):
        parent_work1 = super().work()
        return f"I come to the office and start to hiring"

    # Переопределить методы __str__ для классов-наследников,
    # чтоб они возвращали строку: “Должность: Имя”

    def __str__(self):
        return (f'Recruter: {self.name}')

class Programmer(Employee):
    def __init__(self, name, email, zp, tech_stack):
        super().__init__(name, email, zp)
        self.tech_stack = tech_stack

    def work(self):
        parent_work2 = super().work()
        return f"I come to the office and start to coding"

    # Переопределить методы __str__ для классов-наследников,
    # чтоб они возвращали строку: “Должность: Имя”

    def __str__(self):
        return f'Programmer: {self.name}'

    def comp_tech(self, tech_another):
        if len(self.tech_stack) > len(tech_another.tech_stack):
            comp = '>'
        elif len(self.tech_stack) < len(tech_another.tech_stack):
            comp = '<'
        else:
            comp = '='

        return (f'Tech stack of {self.name} {comp} tech stack of {tech_another.name}')

    def alfa_pr(self, *args):
        tech_stack_for_alfa = set()
        for i in args:
            tech_stack_for_alfa = tech_stack_for_alfa.union((set(i.tech_stack)))

            alfa_pr = Programmer('Proframer 3', 'pr3@gamail.com', 100, list(tech_stack_for_alfa))
            return alfa_pr

emp_1 = Recruiter('Vika', 'viktoria@gmail.com', 24)
emp_2 = Programmer('Sophia', 'Soph@gmail.com', 30,  ['Python', 'SQL', 'CSS', 'PostgreSQL'])
emp_3 = Programmer('Vlad', 'Vlad@gmail.com', 500,  ['Python', 'GitHub', 'Java'])

print(emp_1 > emp_2)
print(emp_1 >= emp_2)
print(emp_1 < emp_2)
print(emp_1 <= emp_2)
print(emp_1 == emp_2)
print(emp_1 != emp_2)

Programmer3 = Programmer.alfa_pr(emp_2, emp_3)
print(Programmer3.tech_stack)

if __name__ == '__main__':
    den = Recruiter('Vasia', 'Vasia1', 22)
    print(den.work())

