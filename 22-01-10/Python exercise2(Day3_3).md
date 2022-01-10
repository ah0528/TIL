# 연산자, if문을 이용한 프로그램 작성 문제

1. 16진수 글자 하나를 입력하면 16진수인지 아닌지를 구분하는 코드를 작성하시오.


```python
inp_letter = input('16진수 한 글자 입력 : ')
if inp_letter in ['A', 'B', 'C', 'D', 'E', 'F']:
    if inp_letter == 'A':
        print('10진수 ==> 10')
    elif inp_letter == 'B':
        print('10진수 ==> 11')
    elif inp_letter == 'C':
        print('10진수 ==> 12')
    elif inp_letter == 'D':
        print('10진수 ==> 13')
    elif inp_letter == 'E':
        print('10진수 ==> 14')
    elif inp_letter == 'F':
        print('10진수 ==> 15')
else:
    print('16진수가 아닙니다')
```

    16진수 한 글자 입력 : D
    10진수 ==> 13
    

2. 입력한 금액을 5만원, 1만원, 5천원, 1천원, 500원, 100원, 50원, 10원 동전으로 교환하는 프로그램을 작성하시오.


```python
cash = int(input('교환할 돈 입력 : '))

if cash // 50000 > 0 :
    a = cash // 50000
else :
    a = 0
cash -= 50000 * a

if cash // 10000 > 0 :
    b = cash // 10000
else:
    b = 0
cash -= 10000 * b

if cash // 5000 > 0 :
    c = cash // 5000
else:
    c = 0
cash -= 5000 * c

if cash // 1000 > 0 :
    d = cash // 1000
else:
    d = 0
cash -= 1000 * d

if cash // 500 > 0 :
    e = cash // 500
else:
    e = 0
cash -= 500 * e

if cash // 100 > 0 :
    f = cash // 100
else:
    f = 0
cash -= 100 * f

if cash // 50 > 0 :
    g = cash // 50
else:
    g = 0
cash -= 50 * g

if cash // 10 > 0 :
    h = cash // 10
else:
    h = 0
cash -= 10 * h

print('50000원 {}장, 10000원 {}장, 5000원 {}장, 1000원 {}장\n500원 {}개, 100원 {}개, 50원 {}개, 10원 {}개\n바꾸지 못한 돈 ==> {}원'.format(a,b,c,d,e,f,g,h,cash))

```

    교환할 돈 입력 : 98760
    50000원 1장, 10000원 4장, 5000원 1장, 1000원 3장
    500원 1개, 100원 2개, 50원 1개, 10원 1개
    바꾸지 못한 돈 ==> 0원
    

3. 두 사람이 주사위를 던져 높은 숫자가 나오면 이기는 게임을 작성해보시오.


```python
import random
A = random.randint(1,6)
B = random.randint(1,6)
print(f'A의 주사위 숫자는 {A}이다.\nB의 주사위 숫자는 {B}이다.')
if A > B:
    print('A가 이겼다.')
elif A < B:
    print('B가 이겼다.')
else:
    print('비겼다.')
```

    A의 주사위 숫자는 5이다.
    B의 주사위 숫자는 4이다.
    A가 이겼다.
    
