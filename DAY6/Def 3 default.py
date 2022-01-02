# 디폴트 매개변수
# 매개변수의 기본값을 지정

def greet(name, msg='안녕^^'):     # 디폴트 매개변수는 무조건 맨 뒤에 위치해야함
    print(name + '!'+ msg)        # 하지만 모두 매개변수라면 상관없음

greet('홍길동','반가워')
greet('강감찬')



def showInfo(name, year=1, age=20):
    print(name, year, age)

showInfo('홍길동', '4', '27')
showInfo('홍길동',3)
showInfo('홍길동')



print('hi', end='#')        # end의 디폴트값은 \n

