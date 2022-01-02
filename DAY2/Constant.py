# 상수 ( CONSTANT )
# 값이 변하지 않음
# 변수와 구분하기 위해 대문자로 사용
# 나중에 값 변경 가능 : 오류 없음

PI=3.141592

# 원의 둘레와 면적 계산

radius = 10
area = radius * radius * PI

print(area)

# 이자 계산 예제
RATE = 0.03

deposit = 100000
interest = deposit * RATE
balance = deposit + interest

print(format(balance,','))
# 위와 같이 , 를쓰면 천단위로 구분하는 구분자역할을 함
