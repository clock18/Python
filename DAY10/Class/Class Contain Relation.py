# 상속관계와 포함관계(has-a)

class Person:
    def __init__(self,name):
        self.name = name
    def greeting(self):
        print('Hi')
    def getName(self):
        print(self.name)


class Student(Person):
    def study(self):
        print('Study')


class PersonList:
    def __init__(self):
        self.personList = []

    def appendPerson(self, person):
        self.personList.append(person)

personL = PersonList()
nameL = ['kim', 'Lee', 'Choi']

for i in range(3):
    p = personL.appendPerson(Person(nameL[i]))
    print(p)