# 예제

def sub(x,y):
    global a        # global이 없다면 a는 전역변수가 됨
    a = 7           # global이 있다면 a는 지역변수가 됨
    x, y = y,x
    b = 3
    print('sub()------------')
    print(a,b,x,y)
    print('-------------')

a,b,x,y = 1,2,3,4
sub(x,y)
print(a,b,x,y)      # global이 없다면 1,2,3,4
                    # global이 있다면 7,2,3,4