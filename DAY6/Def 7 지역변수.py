# 지역 변수 ( local variable ) : 함수 내에서 정의된 함수
# def 안에서 정의된 함수들은 def 밖에서 쓰는 함수와 다름
# 함수가 호출되면 생성되고, 함수가 종료되면 지역변수는 소멸

# def show():
#     a = 1
#     print('show() 함수')
#     print(a)
# show()
# print(a)            # def 안의 a와 print에 입력한 a는 다른 것임



# def show(a):
#     a += 1
#     print('show() 함수')
#     print(a)
# show(10)



# 전역변수 : 함수 밖에서 정의된 함수

a = 1
def show():
    print('show() 함수')
    print(a)           # def 함수 내에 a가 있는 지 찾고 없으면 밖에서 a값을 찾음
show()

b = 10
def add():
    print('add()함수')
    print(a)
    print(b)
    print('--------------------------------')
add()

# 전역 변수 a를 변경하려고 할 때
def add2():
    global a
    a += 1
    c = a + b
    print('add2()함수')
    print(a)
    print(b)
    print(c)
    print('--------------------------------')
add2()




# 전역 변수는 어디서든지 사용 가능 ( 함수 내부에서 사용 가능 )
# 함수내부의 지역 변수나 매개 변수는 함수 내에서만 사용가능
# 지역변수가 전역변수보다 우선순위가 높음
# 함수 내부에서 할당연산자 사용하는 식에서 변수는 지역변수로 인식
# 함수 내부에서 전역변수를 변경할 때는 global 키워드를 사용
