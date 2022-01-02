# 1-1

# for i in range(5,0,-1):
#     print('*'*i)



# 1-2

# for i in range(1,10,2):
#     print(' '*(10-i//2),'*' * i)

# for y in range(1, 10, 2):
#     string = '*'*y
#     print(string.center(10))



# 2

# cnt = int(input('숫자 입력 : '))
#
# while cnt != 7:
#     cnt = int(input('다시 입력 : '))
#
# print('7 입력! 종료')



# 3

money = 11000
value = 2000
i = 1

while i <= money // value:
    print('노래를 {}곡 불렀습니다'.format(i))
    balance = money - (i*value)
    print('현재 {}원 남았습니다.'.format(balance))
    i += 1
    if balance < 2000:
        print('잔액이 충분하지 않습니다. 종료합니다.')
        break
