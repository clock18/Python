# 클래스 메서드 : 인스턴스를 통하지 않고 메서드를 클래스에서 바로 호출

# @classmethod를 메서드 위에 붙이면 됨
# 반드시 메서드내에 인수로 cls를 지정해야함

# 형식
# class 클래스이름:
#     @classmethod
#     def 메서드명(cls, 인수1,인수2...):
#         코드입력

# 호출 형식
# 클래스이름.메서드명(인수1, 인수2 ..)

# 클래스 변수 이용 ex
# class Person:
#     count = 0
#     def __init__(self,name):
#         self.name = name
#         Person.count += 1
#
#     def printCount(self):
#         print(f'{self.count}명이 태어났습니다.')
#
# man1 = Person('Kim')
# man2 = Person('Lee')
#
# man1.printCount()
# man2.printCount()


class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def printCount(cls):
        print(f'{cls.count}명이 태어났습니다.')


man1 = Person('Kim')
man2 = Person('Lee')

Person.printCount()