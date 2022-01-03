from random import randint

com = int(randint(1, 3))


def gbb_game(you_n):

    if (com == 1 and you_n == 3) or (com == 2 and you_n == 1) or (com == 3 and you_n == 2):
        print('컴퓨터가 이겼습니다.')
        print('com : %d'%com)
    elif com == you_n:
        print('비겼습니다.')
        print('com : %d' % com)
    else:
        print('당신이 이겼습니다.')
        print('com : %d' % com)


def input_num():
    you = int(input('YOU 입력 (1:가위, 2:바위, 3:보) : '))
    gbb_game(you)



