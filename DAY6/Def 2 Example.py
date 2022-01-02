# 사칙연산 함수 작성
# add() : 더하기
# sub() : 빼기
# mul() : 곱하기
# div() : 나누기
# mod() : 나머지

# a = 9, b = 3
# 두 개의 숫자를 전달받아서 연산 결과 반환

def add():
    a = int(input('숫자 1 입력 : '))
    b = int(input('숫자 2 입력 : '))
    return a + b

print('더한 값 : ',add())


def sub():
    a = int(input('숫자 1 입력 : '))
    b = int(input('숫자 2 입력 : '))
    return a - b

sub = sub()
print('뺀 값 : ',sub)

def mul():
    a = int(input('숫자 1 입력 : '))
    b = int(input('숫자 2 입력 : '))
    return a * b

mul = mul()
print('곱한 값 : ',mul)

def div():
    a = int(input('숫자 1 입력 : '))
    b = int(input('숫자 2 입력 : '))
    return a / b

div = div()
print('나눈 값 : ',div)

def mod():
    a = int(input('숫자 1 입력 : '))
    b = int(input('숫자 2 입력 : '))
    return a % b

mod = mod()
print('나머지 값 : ',mod)






