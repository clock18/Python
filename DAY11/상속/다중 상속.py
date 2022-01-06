# 다중 상속 : 여러 클래스에서 상속을 받는 것

# class 클래스이름(base class1, base class 2, ...):  # base class = 부모 클래스 = super class
#     pass


class Person(object):
    def __init__(self,name='',age=0):
        self.name = name
        self.age = age

    def greeting(self):
        print(f'안녕하세요 {self.name}')

class University:
    def __init__(self,department='', grade=''):
        self.department = department
        self.grade = grade

    def manageScore(self):
        print('학점관리')

class Undergraduate(Person, University):
    def study(self):
        print('공부하기')

kim = Undergraduate()
kim.name = 'kim'
kim.age = 20
kim.greeting()
kim.manageScore()
kim.study()
