from random import randint
DiceA = int(randint(1,6))
DiceB = int(randint(1,6))

Ainput = input('%d'%DiceA)
Binput = input('%d'%DiceB)

if DiceA == Ainput and DiceB == Binput:
    print('A의 주사위 숫자는 %d 입니다.'%Ainput)
    print('B의 주사위 숫자는 %d 입니다.'%Binput)
    if DiceA>DiceB:
        print('A가 이겼다')
    else:
        print('B가 이겼다')






