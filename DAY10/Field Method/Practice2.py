# 앞에서 작성한 car 클래스에서 다음의 두가지 메소드를 추가하시오.
# speedUp(증가할 속도량)
# speedDown(감소할 속도량)

class Car:
    model = ''

    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model

    def getModel(self):
        return self.model
    def setModel(self, model):
        self.model = model

    def getSpeed(self):
        return self.speed
    def setSpeed(self, speed):
        self.speed = speed

    def speedUp(self, speed):
        if self.speed >= 140:
            print('과속입니다. 속도를 줄이세요.')
        else:
            self.speed += speed
    def speedDown(self, speed):
        if self.speed > 0 :
            self.speed -= speed
        else:
            self.speed = 0
            print('정지했습니다.')