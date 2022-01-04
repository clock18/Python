# 클래스 구현과정
# 1단계 : 클래스 정의(선언)
# class 클래스명:
#     def __init__(self):
#         self.필드명1 = 초기값
#         self.필드명2 = 초기값
#
#     def 메소드명1(self, 매개변수, ...):
#         pass
#         return

# 2단계 : 객체 생성(인스턴스 생성) => 변수선언과 비슷
# 객체변수명 = 클래스명()

# 3단계 : 객체 이용, 메소드, 필드값변경, 필드값 사용
# 변수나 함수와 다르게 구별하기 위해서
# 객체이름.변수명
# 객체이름.메소드명


# 자동차 클래스
# 기능(동작) => 메소드(함수) : speedUp(), speedDown()
# 속성(상태, 값) => 변수(필드) : color, speed

# 1. 클래스 선언
# 클래스이름 : 식별자 규칙에 따라서 정의 ( 숫자먼저나오면안됨. 영어숫자혼용가능. 특수문자는 밑줄만가능,
#                                   구분하기 위해 클래스이름의 첫글자는 무조건 대문자 )
class Car:
    def __init__(self):
        self.speed = 0
        self.color = 'red'

    def speedUp(self):
        pass

    def speedDown(self):
        pass

# 2. 객체 생성
myCar = Car()
yourCar = Car()

# 3. 객체(인스턴스) 사용
myCar.speedUp()
myCar.color = 'black'

# 특정한 클래스의 인스턴스인지 확인 : isinstance(인스턴스명, 클래스명)
print(isinstance(myCar,yourCar))

# 파이썬의 클래스
# ex. int, float, str, bool, list, dict, set, tuple


