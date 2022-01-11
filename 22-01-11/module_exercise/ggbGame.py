# gbbGame.py
import random
com_n = random.randint(1,3)

def gbb_game(you_n):
    if (com_n - you_n == -2) or (com_n - you_n == 1):
        print('컴퓨터가 이겼습니다.')
    elif com_n == you_n :
        print('비겼습니다.')
    else:
        print('당신이 이겼습니다.')
    print(f'COM:{com_n}')

def input_num():
    you_n = int(input('YOU 입력 (1:가위, 2:바위, 3:보) : '))
    gbb_game(you_n)

