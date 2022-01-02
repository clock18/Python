# 파이썬이 처리하는 자료형 ( Data Type )
# 정수(int), 실수(float), 문자열(str), 불(bool)

# 정수 : 2진수, 10진수, 8진수, 16진수
# 실수 : 3.14   1.2e3
# 문자열 : ''  ""
# 불(논리) : True False



a=100
b=3.14
c='name'
d=True

print(type(a))
print(type(b))
print(type(c))
print(type(d))


# 형변환 ( 자료 유형 변환 ) : int float str
# str() : 문자열로 변환
print(type(str(100)))

# int(문자열) : 문자열을 정수형으로 변환

# float(문자열) : 문자열을 실수형으로 변환

# int (문자열, 진수)
print(int('1010',2))
print(int('1010',8))