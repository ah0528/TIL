# for문, while문 연습문제
1. for문을 이용하여 * 문자로 트리를 만드시오.


```python
for i in range(5,0,-1):
    print(i*'*')

for i in range(1,6):
    print(' '*(5-i)+'*'*i+'*'*(i-1)+' '*(5-i))
```

    *****
    ****
    ***
    **
    *
        *    
       ***   
      *****  
     ******* 
    *********
    

2. while문을 이용하여 7을 입력할 때까지 입력을 반복하고, 7이 입력되면 종료되는 코드를 작성하시오.


```python
k = int(input('숫자 입력 : '))

while True:
    if k == 7:
        print('7 입력! 종료')
        break
    else:
        k = int(input('다시 입력 : '))
```

    숫자 입력 : 10
    다시 입력 : 9
    다시 입력 : 8
    다시 입력 : 7
    7 입력! 종료
    

3. 노래방 기계에서 현재 잔액이 소진될 때까지 노래방을 이용하는 프로그램을 작성하시오.


```python
money = int(input('현재 잔액 : '))
song_price = int(input('1곡 가격 : '))
k = money // song_price

while k > 0:
    for i in range(1,k+1):
        print(f'노래를 {i}곡 불렀습니다.\n현재 {money - (song_price * i)}원 남았습니다.')
        if money - (song_price * i) < song_price :
            print('돈이 부족합니다. 종료합니다.')
    break
```

    현재 잔액 : 10000
    1곡 가격 : 3000
    노래를 1곡 불렀습니다.
    현재 7000원 남았습니다.
    노래를 2곡 불렀습니다.
    현재 4000원 남았습니다.
    노래를 3곡 불렀습니다.
    현재 1000원 남았습니다.
    돈이 부족합니다. 종료합니다.
    
