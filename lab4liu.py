from datetime import datetime, timedelta


class Student:
    def __init__(self, name, dob, properties=None):
        if properties is None:
            properties = []
        self.name = name
        self.dob = datetime.strptime(dob, '%Y-%m-%d')
        self.properties = properties

    def __str__(self):
        return f'Ім\'я: {self.name}, ДН: {self.dob.strftime("%Y-%m-%d")}, Властивості: {", ".join(self.properties)}'

    def str_save(self):
        res = f'{self.name},{self.dob.date()},' + ','.join(self.properties) + '\n'
        return res

    def iadd(self, other):
        self.dob += timedelta(days=int(other))
        return self

    def add_property(self, property):
        self.properties.append(property)


students = []
try:
    with open('text.txt', 'r', encoding="utf-8") as old:
        for line in old:
            lists = line.strip().split(',')
            student = Student(name=lists[0], dob=lists[1], properties=lists[2:])
            students.append(student)
except:
    pass


count_st= int(input('Суільки студентів будете додавати? '))
for student in range(count_st):
    name = input(f'Введіть ім\'я {student+1} студента: ')
    dob = input(f'Введіть ДН {student+1} студента: ')
    student = Student(name=name, dob=dob)
    count_p = int(input(f'Яку кількість властивостей для студента {name} буде додано? '))
    if count_p != 0:
        for property in range(count_p):
            a = input(f'Введіть властивість {property+1} для студента {name}: ')
            student.add_property(a)
    students.append(student)


with open('text.txt', 'w', encoding="utf8") as new:
    for i in students:
        a = i.str_save()
        new.write(a)

for i in students:
    print(i)