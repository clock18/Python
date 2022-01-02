# 재귀 호출 : 자기함수 호출

# 문제1. 팩토리얼 계산
# 반복문 이용

# def factorial(n):
#     b = 1
#     for x in range(n,0,-1):
#         b *= x
#     return b
#
# n = int(input('숫자 입력 : '))
# print(factorial(n))


# 반복문 이용
def count(number):
    for x in range(number,0,-1):
        print(x)
count(5)


# 재귀함수 이용
def selfCount(number):
    if number == 1:
        return 1
    else:
        print(number)
        return count(number-1)
print(selfCount(5))