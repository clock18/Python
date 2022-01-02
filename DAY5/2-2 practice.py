# 입력한 문자가 16진수인지 판별

# num = input('16진수 한 글자 입력 : ')
# if '0' <= num <= '9' or 'A' <= num <= 'F':  # a = 10 , a = 11 ...
#     print('10진수 > ',int(num, 16))
# else:
#     print('16진수가 아닙니다.')



# 지폐나 동전 교환

# cash, c50000, c10000, c5000, c1000, c500 = 0,0,0,0,0,0
# c100, c50, c10 = 0,0,0
#
# cash = int(input('교환할 돈은 얼마? '))
#
# c50000 = cash//50000
# cash = cash%50000
# c10000 = cash//10000
# cash = cash%10000
# c5000 = cash//5000
# cash = cash%5000
# c1000 = cash//1000
# cash = cash%1000
# c500 = cash//500
# cash = cash%500
# c100 = cash//100
# cash = cash%100
# c50 = cash//50
# cash = cash%50
# c10 = cash//10
# cash = cash%10
#
# print('50000원 %d장'%c50000)
# print('10000원 %d장'%c10000)
# print('5000원 %d장'%c5000)
# print('1000원 %d장'%c1000)
# print('500원 %d장'%c500)
# print('100원 %d장'%c100)
# print('50원 %d장'%c50)
# print('10원 %d장'%10)
# print('바꾸지 못한 돈 → %d원'%cash)



# 주사위 게임 ( 가위바위보 게임 )

from random import randint

DiceA = randint(1,6)
DiceB = randint(1,6)

if DiceA > DiceB:
    print('A의 주사위 숫자는 %d 입니다.'%DiceA)
    print('B의 주사위 숫자는 %d 입니다.'%DiceB)
    print('A가 이겼다.')
elif DiceA < DiceB:
    print('A의 주사위 숫자는 %d 입니다.' % DiceA)
    print('B의 주사위 숫자는 %d 입니다.' % DiceB)
    print('B가 이겼다.')
else:
    print('A의 주사위 숫자는 %d 입니다.' % DiceA)
    print('B의 주사위 숫자는 %d 입니다.' % DiceB)
    print('둘이 비겼다.')
