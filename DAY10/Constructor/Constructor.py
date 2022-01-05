# 생성자 ( constructor ) : 인스턴스 생성, 필드값을 초기화 하는 함수

# 생성자의 형식
# class 클래스명:
#     def __init__(self, *args):
        # 이 부분에 필드 초기화하는 코드를 입력

# self : 클래스에서 생성된 인스턴스에 접근하기 위한 목적으로 사용

# _ : 변수에 특별한 이름을 부여하지 않고 사용하려고 할 때
# ex. for _ in range(10)
#       print('Hello')

# __ : 특수한 예약함수, 변수에 사용
# ex. if __init__ == '__main__':


# 1. 기본 생성자 : 생성자에 self만 있고, 다른 매개변수가 없는 경우
# class Car:
#     def __init__(self):
#         self.color = 'red'
#         self.speed = 0
#
# car1 = Car()
# print(f'자동차의 색상은 {car1.color}')
# print(f'자동차의 속도는 {car1.speed}')


# 2. 매개변수가 있는 생성자
# class Car1:
#     def __init__(self,speed,color):
#         self.speed = speed      # 차변과 대변은 다른 값이지만 형식상 같은 이름으로 작성해줌
#         self.color = color
#
# myCar = Car1()      # speed와 color 라는 매개변수도 같이 넣어줘야함. 안넣으면 타입에러가 뜸
# myCar = Car1(10, 'white')
# print(isinstance(myCar, Car1))
# print(f'myCar의 색상은 {myCar.color}')
# print(myCar.speed)


# 3. 디폴트 매개변수를 사용하는 생성자
class Car1:
    def __init__(self,speed=0,color='red'):
        self.speed = speed
        self.color = color

myCar = Car1()
print(f'myCar의 색상은 {myCar.color}')
print(myCar.speed)

myCar = Car1(10, 'white')
print(f'myCar의 색상은 {myCar.color}')
print(myCar.speed)


# 3-1.
class Car3:
    def __init__(self,speed=0,color='red'):
        self.speed = speed
        self.color = color

    def drive(self):
        self.speed = 50

    def speedUp(self):
        self.speed += 10

myCar4 = Car3()
print('초기 속도',myCar4.speed)
myCar4.drive()
print('drive 이후 속도',myCar4.speed)
myCar4.speedUp()
print('speedUp 이후 속도',myCar4.speed)