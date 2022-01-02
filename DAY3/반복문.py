# 제어구조
# 1. 순차구조 : 명령들이 순차적으로 실행되는 구조
# 2. 선택구조 : 조건에 따라 명령을 선택하여 실행되는 구조
# 3. 반복구조 : 동일한 명령이 반복되면서 실행되는 구조

# 반복 : 동일한 문장을 여러 번 반복시키는 구조

# for (변수) in 리스트 또는 범위:
#   반복문장1
#   반복문장2

# []안에 여러개의 변수가 들어가있는 것을 리스트라고 함.
# ex. ['홍길동', '이몽룡', '성춘향'] = 리스트

# for (변수) in range(0,10):
#   pirnt(변수)
#   결과 : 0~9까지 출력
# range(출력시작값, 출력끝값+1)
# range(출력끝값+1) 이 경우에는 무조건 0부터 출력 시작
# range(출력시작값, 출력끝값+1, 간격)

# for name in ['apple', 'banana', 'melon']:
#     print(name)

# for number in range(10):
#     print(number)

# for number in range(0,10):
#     print(number)

# for number in range(1,10,2):  올라갈때는 +1
#     print(number)

# for number in range(9,0,-1):  내려갈때는 -1
#     print(number)


sumx = 0
for x in range(1,11):
    sumx += x
print(sumx)

# x=0
# for y in range(1,101,2):
#     x += y
# print(x)

# odd=0
# even=0
# for i in range(1,101):
#     if i%2==1:
#         odd+=i
#     else:
#         even+=i
# print('홀수의 합은 : ',odd)
# print('짝수의 합은 : ',even)

# three=0
# for i in range(3,101,3):
#     three += i
#     print(i)
# print('3의 배수의 합은 : ', three)


# for i in range(100):
#     if i%3 == 0:
#         three += i
#         print(i)
# print(three)


