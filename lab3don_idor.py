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

    def __del__(self):
        pass

    def forWrite(self):
        res = f'{self.name},{self.dob.date()},' + ','.join(self.properties) + '\n'
        return res

    def iadd(self, days):
        self.dob += timedelta(days=int(days))
        return self

    def add_property(self, property):
        self.properties.append(property)


students = []

with open('ourText.txt', 'r', encoding="utf-8") as doc:
    for line in doc:
        lists = line.strip().split(',')
        student = Student(name=lists[0], dob=lists[1], properties=lists[2:])
        students.append(student)


count= int(input('Яку кількість студентів буде додано? \n'))

for student in range(count):
    name = input(f'Введіть ім\'я {student+1} студента: \n')
    dob = input(f'Введіть ДН {student+1} студента: \n')
    student = Student(name=name, dob=dob)
    count2 = int(input(f'Яку кількість властивостей для студента {name} буде додано? \n'))

    if count2 != 0:
        for property in range(count2):
            a = input(f'Введіть властивість {property+1} для студента {name}: \n')
            student.add_property(a)
    students.append(student)


with open('ourText.txt', 'w', encoding="utf8") as newDoc:
    for i in students:
        a = i.forWrite()
        newDoc.write(a)


for lineFromTxt in students:
    print(lineFromTxt)