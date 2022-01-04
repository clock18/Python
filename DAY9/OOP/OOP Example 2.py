# 1. 클래스 생성
class Car:
    def speedUp(self):
        pass

    def speedDown(self):
        pass

# 2. 객체 생성
myCar = Car()
yourCar = Car()

# 3. 객체(인스턴스) 사용
myCar.speedUp()
# 인스턴스 생성 후 필드 추가
myCar.color = 'black'
myCar.speed = 0

print(myCar.color)