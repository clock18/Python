# 함수(function) 정의

# def show_info():
#     print('이름 : 정진한')
#     print('나이 : 27')
#
# show_info()
#
#
# def welcome(n):
#     for x in range(n):
#         print('welcome!')
#
# welcome(5)


# 두 개의 숫자를 입력받아서 합을 구하여 출력하는 함수 작성

def sumAB():
    a = 0
    for x in range(1,3):
        b = int(input('숫자 %d 입력 : '%x))
        a += b
    print('합 :',a)

sumAB()