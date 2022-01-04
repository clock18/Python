# Error
# 문법적 오류, 실행 시간에 잘못된 메모리 접근 오류, 논리 오류, 사용자의 잘못된 입력 오류 등

# 예외
# 오류에 대처하기 위한 오류
# 예외는 주로 실행 중에 발생
# 오류 발생 시 프로그램이 중단되고 에러 메시지가 출력되지 않도록 예외를 발생시켜
# 예외 처리를 통해 정상 실행되도록 하기 위한 방법

# 예외 처리 방법
# try ... except
# try:
#       (예외 발생 가능) 문장
# except 예외 유형:
#        예외 처리 문장
# else:
#       예외 없을 떄 수행 문장
# finally:
#       예외 유뮤 상관없이 실행될 문장


# 0으로 나눈 경우
# ZeroDivisionError: division by zero 발생
# print(10/0)

# TypeError: can only concatenate str (not "int") to str
# print('나이 : '+23+'살')

# NameError: name 'b' is not defined
# print(b)

# ValueError: incomplete format
b=10
# print('%d%'%b)

# SyntaxError: expected ':'
# if b>10
#     print('합격')

# IndexError: list index out of range
# a = [1,2,3,4]
# print(a[4])

# UnboundLocalError
# def add():
#     a = a+1

# ModuleNotFoundError: No module named 'mymodule'
# import mymodule

# FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'
# f = open('test.txt', 'r')
# data = f.read()
# f.close()

# OSError: [Errno 22] Invalid argument: 'c:\test.txt'  => 경로명 에러
# f = open('c:\test.txt','r')
# f.close()

# try:
#     f = open('test22.txt','r')
# except FileExistsError:
#     pass
# else:
#     data = f.read()
#     print(data)
#     f.close()

try:
    f = open('test2.txt','r')
except FileNotFoundError as e:
    print(e)
else:
    data = f.read()
    print(data)
    f.close()