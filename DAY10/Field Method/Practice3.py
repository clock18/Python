# 앞에서 작성한 Dog 클래스에서
# 1. 객체간의 크기를 비교하는 메서드 작성
# 2. 객체간의 나이를 더하고, 빼고, 곱하고, 나누는 메서드 작성

class Dog:
    def __init__(self,Size='small',Age='1 year',Color='red'):
        self.Size = Size
        self.Age = Age
        self.Color = Color


    def setSize(self, Size):
        self.Size = Size
    def getSize(self):
        return self.Size

    def setAge(self, Age):
        self.Age = Age
    def getAge(self):
        return self.Age

    def __gt__(self, other):
        return self.Size >= other.Size
    def __add__(self, other):
        return self.Age + other.Age
    def __sub__(self, other):
        return self.Age - other.Age
    def __mul__(self, other):
        return self.Age * other.Age
    def __repr__(self):
        return '두 강아지의 나이를 더한 값은 ' + str(Dog1+Dog2)+ ' 입니다.'

Dog1 = Dog(10,15)
Dog2 = Dog(5,5)
plus = Dog1.getAge() + Dog2.getAge()
sub = Dog1.getAge() - Dog2.getAge()
mul = Dog1.getAge() * Dog2.getAge()


print(Dog1.getSize() > Dog2.getSize())
print(plus)
print(sub)
print(mul)
print(Dog1)
