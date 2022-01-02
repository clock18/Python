#print('hello')
#print('정진한')

# 변수 설정
#   c언어 기반이기 때문에 대소문자를 구분한다.
#   영문자, 숫자, 밑줄 모두 사용 가능하다. ( 특수문자 불가.
#    영문자보다 숫자가 먼저 나오거나 숫자만 쓰는 것 불가)
#   중간에 공백 사용x
#   ex. std_name(snake형)
#       stdName(camel형)
# 예약어는 변수명으로 사용불가
#   ex. if, def, while, return 등

a=100
b=50
temp=a
a=b
b=temp
print(a)
print(b)

# 변수 삭제 = del z ( 띄워써야함 )
# height = 키, weight = 몸무게. width = 폭, 너비
# %d=정수, %f=실수, %s=문자열, %% = %, %c = 문자1개
# \n = 1줄 띄어쓰는 효과
#   ex. print('성명:%s\n학번:%d'%(name,no)
#       결과 = 성명 : 정진한
#             학번 : 21410462
# format(변수,형식)
#   ex. format(ctemp,'.2f')
# f=90
# c=(f-32)*5/9
# print('%.2f'%c)
# print(format(c,'.2f'))
# 변수 선언 : int x, float y, char z