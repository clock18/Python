# 상송 ( inheritance )
# 부모클래스 (super class) : 상속을 해주는 클래스
# 자식클래스(sub class)


# 자동차 클래스
class Car:
    speed =0
    color = ''

    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

    def drive(self):
        print(f'{self.speed}로 주행합니다')      # return 값이 없으면 결과창에 None이 뜸



class Truck(Car):
    def __init__(self, speed, color, load):
        super().__init__(speed, color)      # super클래스의 speed,color를 Truck함수
        self.load = load                    # 안에서 다시 초기화 시켜줌.

truck1 = Truck(10, 'red', 1000)
truck1.drive()


# 승용차 클래스
class Vehicle(Car):
    def __init__(self, speed, color, seat):
        super().__init__(speed, color)
        self.seat = seat

    def person(self):
        print(f'{self.seat}명의 사람이 앉을 수 있습니다.')

vehicle1 = Vehicle(10,'red',4)
vehicle1.person()