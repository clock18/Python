# 1. 클래스 선언
# 클래스 선언 시 필드 추가

class Car:
    color = ''
    speed = 0

    def speedUp(self):
        self.speed += 10

    def speedDown(self):
        pass

# 2. 객체 생성
myCar = Car()
yourCar = Car()

# 3. 객체(인스턴스) 사용
myCar.speedUp()
print(myCar.speed)
myCar.color = 'black'
print(myCar.color)

myCar.speedUp()
print(myCar.speed)
myCar.speedUp()
print(myCar.speed)