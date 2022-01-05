# 클래스 상속과 메소스 재정의 연습

# Animal 클래스 정의
# talk(), eat(), sleep()  => 메소드
# age, leg, color, breed  => 필드

# 서브클래스 Dog 클래스 정의
# 메소드 다 받아들이고 talk() 재정의 => '멍멍'

# 서브클래스 Cat 클래스 정의
# 메소드 다 받아들이고 talk() 재정의 => '야옹'

class Animal():
    age = 0
    leg = 4
    color = 'black'
    breed = ''

    def __init__(self,age,leg,color,breed):
        self.age = age
        self.leg = leg
        self.color = color
        self.breed = breed

    def setAge(self, age):
        self.age = age
    def getAge(self):
        return self.age

    def setLeg(self, leg):
        self.leg = leg
    def getleg(self):
        return self.leg

    def setColor(self, color):
        self.age = color
    def getColor(self):
        return self.color

    def setBreed(self, breed):
        self.age = breed
    def getBreed(self):
        return self.breed

    def setEat(self,eat):
        self.eat = eat

    def setSleep(self,sleep):
        self.sleep = sleep


class Dog(Animal):
    def __init__(self,age,leg,color,breed):
        super().__init__(age, leg, color, breed)

    def dogTalk(self):
        print('멍멍')


class Cat(Animal):
    def __init__(self, age, leg, color, breed):
        super().__init__(age, leg, color, breed)

    def catTalk(self):
        print('야옹')

animal1 = Cat(4,4,'white','munchicken')
animal1.catTalk()
print(animal1.getBreed())


# 다형성 : 같은 이름의 메서드가 다른 기능을 할 수 있도록 한 것
# animals = [(cat1),(cat2),(cat3)]
# for animal in animals