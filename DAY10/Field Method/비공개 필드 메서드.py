# 비공개 필드와 메소드 생성

# 비공개 필드 : 필드를 외부에서 직접 사용하지 못하도록 하는 방법
#             클래스 내부에서만 사용가능
# ex. __필드명

class Car:
    def __init__(self, speed=0, color='white'):
        self.speed = speed
        self.__color = color        # 클래스 내에서만 사용하는 비공개필드

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

car1 = Car()
print(car1.getColor())
car1.setColor('red')
print(car1.getColor())
# print(car1.color)       # 사용 불가