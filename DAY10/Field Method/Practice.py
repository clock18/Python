# 앞에서 작성한 Dog 클래스에서
# 1. 디폴트 매개변수를 갖는 생성자를 정의
# 2. 필드의 값을 가져오고, 변경하는 메서드를 정의
# 3. sleep(), sit(), run(), eat() 메소드의 내용을 정의
#    잠자기,   앉다,   뛰다,   먹다 등의 내용이 출력되도록 정의
# 4. 필드 중 breed는 비공개필드로 정의

# 인스턴스를 생성하되, 인수의 수를 다양하게 입력하여 생성하는 코드 작성

class Dog:
    def __init__(self,Breed='Maltese', Size='small',Age='1 year',Color='red'):
        self.__Breed = Breed
        self.Size = Size
        self.Age = Age
        self.Color = Color

    def setBreed(self, Breed):
        self.__Breed = Breed
    def getBreed(self):
        return self.__Breed

    def setSize(self, Size):
        self.Size = Size
    def getSize(self):
        return self.Size

    def setAge(self, Age):
        self.Age = Age
    def getAge(self):
        return self.Age

    def setColor(self, Color):
        self.Color = Color
    def getColor(self):
        return self.Color


    def sleep(self):
        self.sleep = print('잠자기')

    def sit(self):
        self.sit = print('앉기')

    def run(self):
        self.run = print('뛰기')

    def eat(self):
        self.eat = print('먹기')

mydog = Dog()
