# 리터럴 : 정수 실수 문자 문자열 논리값 특수
# 고정된 값, 변수에 저장되는 값
# 정수 리터럴 : 소수점이 없는 정수 ex. 0 75 100
# 0b로 시작하면 2진수  0o로 시작하면 8진수
# 0~9로 시작되면 10진수
# 0x로 시작하면 16진수, 16진수에서 10=a, 11=b 12=c ...
# 실수 리터럴 : 소수점이 있는 실수. e를 포함하는 지수표현
# 문자 리터럴 : 따옴표로 묶은 하나의 문자 ex 'a' , 'b'
# 문자열 리터럴 : ex. '홍길동' , 'python'
# 논리값 리터럴 : True False 값
# 특수 리터럴 : None ( 값이 없음 )



# 정수 리터럴

a=49
b=0b110001
c=0o61
d=0x1f2c
e=0x31

print(a,b,c,d,e)


# 실수 리터럴

f1 = 3.14
f2 = -123.45
f3 = 1.234e5
    # e5 = 10의 5승을 의미

print(f1,f2,f3)



# 문자 리터럴

c1 = 'a'
c2 = 'b'

print(c1, c2)


# 문자열 리터럴

str1 = '정진한'
str2 = 'hello'
str3 = """안녕하세요
반갑습니다"""
str4 = '''여러 줄로 나누어
사용할 수 
있어요'''
print(str1,str2,str3,str4)


# 논리값 리터럴 : True, False

t= True
f = False

print(t,f)



# 특수 리터럴 : None

name = '정진한'
phone = ''
address = None

print(name, phone, address)