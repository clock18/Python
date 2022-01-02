# 'stop' 문자 입력될 때 까지 숫자를 입력하고, 입력된 숫자의 개수를 출력

# num = input('숫자입력 : ')
# cnt = 0
# while num != 'stop':
#     num = int(num)
#     cnt += 1
#     num = input('숫자입력 : ')
#
# print('숫자 개수', cnt)



# 7을 입력할 때까지 계속 입력하기
# 7이 입력되면 프로그램 종료

num = int(input('숫자 입력 : '))

while num != 7:
    num = int(input('숫자 입력 : '))
else:
    print('7 입력 종료')
