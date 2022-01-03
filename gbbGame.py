#gbbGame.py
import random
com = random.randint(1,3)

def gbb_game(you_n):
    if com - you_n == -2 or com - you_n == 1:
        print('컴퓨터가 이겼습니다.')
    elif com - you_n == 0:
        print('비겼습니다.')
    else:
        print('당신이 이겼습니다.')
    print(f'COM:{com}')

def input_num():
    you = int(input('YOU 입력 (1:가위, 2:바위, 3:보) : '))
    gbb_game(you)