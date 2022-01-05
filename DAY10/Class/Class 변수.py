# 클래스 변수 : 여러 인스턴스가 공유하는 변수
class Car:
    color = ''
    speed = 10
    count = 0

    def __init__(self):
        self.speed = 0
        Car.count += 1        # self.count 였으면 지역변수라서 1이 출력되지만
                              # 클래스이름.count로 했기 때문에 공유하는 형태가 됨 (전역변수)

car1 = Car()
print(car1.count)
car2 = Car()
print(car2.count)