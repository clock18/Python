class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        return self.name + '님 안녕하세요'

class Student(Person):
    def __init__(self, name, age, department, grade):
        super().__init__(name, age)
        self.department = department
        self.grade = grade

    def study(self):
        pass

person1 = Person('정진한', 27)
print(person1.greeting())