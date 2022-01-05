# 필드 이용 메서드

class Car:
    model = ''

    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model

    # 필드값을 반환
    def getModel(self):
        return self.model

    # 필드값을 지정
    def setModel(self, model):
        self.model = model

    def getSpeed(self):
        return self.speed

    def setSpeed(self, speed):
        self.speed = speed

myCar = Car(0,'red','audi')
print(myCar.getSpeed())

myCar.setSpeed(50)
print(myCar.getSpeed())