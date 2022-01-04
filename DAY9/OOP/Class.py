# 객체와 클래스
# 함수처럼 어떤 기능을 함수 코드에 묶어 두는 것이 아니라, 객체라고 하는 코드에
# 그런 기능을 묶은 하나의 단일 프로그램을 넣어 다른 프로그래머가 재사용할 수 있도록 함
# 함수와 변수를 함께 가지고 있도록 구성

# 계산기 (객체) : 계산기가 여러개 필요한 경우 함수와 변수를 여러개 생성해야 함
result = 0

def adder(num):
    global result
    result += num
    return result

print(adder(3))
print(adder(7))
print(adder(9))


# 계산기 (클라스)

class Calculator:
    def __init__(self):
        self.result = 0         # result 라는 변수를 쓸 것이라는 의미

    def adder(self,num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()


# 클래스 구현하기
# 1. 클래스 선언
# 2. 인스턴스 생성
# 3. 필드나 메서스 사용