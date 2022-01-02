# 내부 함수 : 함수 안에 있는 함수
# 함수가 정의된 범위 안에서만 사용 가능

def func1(x,y):
    def func2(a,b):
        return a+b
    return func2(x,y)

print(func1(10,20))
# print(func2(10,20))     # fun1 안에서 정의된 함수이므로 에러가뜸.
