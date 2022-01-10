[자료형, 연산자에 대한 연습문제]

1. 변수에 대한 설명으로 틀린 것을 모두 고르시오. 

① 파이썬은 변수의 선언을 생략해도 된다.

② 변수 종류에는 정수형, 실수형, 불형, 문자열 등이 있다.

③ a=b처럼 같이 변수에 변수를 대입할 수 없다.

<span style="color:green">④ type( ) 함수는 변수에 저장된 값을 출력한다.</span>


2. 코드를 실행하면 오류가 발생한다. 그 이유를 설명하시오. 

    a=b=10=c=d=20

<span style="color:green">중간에 변수가 아닌 숫자가 들어 있기 때문이다.</span>

3. 각 진수를 10진수로 변환하시오.

① 2진수 0011 <span style="color:green">3</span>

② 2진수 01010 <span style="color:green">10</span>

③ 16진수 11  <span style="color:green">17</span>

④ 8진수 17  <span style="color:green">15</span>


4. 오류가 발생하는 것을 모두 고르고, 그 이유를 간단히 설명하시오.

① int('1002', 2) <span style="color:green">2진수에 2를 사용할 수 없음</span>

② int('1008', 8) <span style="color:green">8진수에 8를 사용할 수 없음</span>

③ int('AAFG', 16) <span style="color:green">16진수에 G를 사용할 수 없음</span>


5. 코드의 출력값을 예측하시오.

   bin(12); hex(12); oct(12)
   
   <span style="color:green">0b1100; 0o14; 0xc</span>

6. 다음 계산식의 결과를 예측하시오. 

   a, b, c = 1, 2, 3
   
① a+b%c <span style="color:green">3</span>

② a*b-c <span style="color:green">-1</span>

③ a/b*c <span style="color:green">1.5</span>


7. 문자열을 숫자로 변환한 후, 계산하는 식이다. 오류가 발생하는 것을 고르고, 오류가 발생하지 않도록 수정하시오. 

   s1, s2, s3 = "111", "111.11", "99999999999999"
   

① int(s1) + 111.11

② int(s2) + 111.11  <span style="color:green">오류발생, float(s2) + 111.11로 수정해야함</span>

③ int(s3) + 111.11



8. 비트 연산자의 활용이다. 결과를 16진수로 예측하시오. 

0xFF00 & 0x00FF  <span style="color:green">0x0000</span>

0xFF00 | 0x00FF  <span style="color:green">0xFFFF</span>

0xFF00 ^ 0x00FF  <span style="color:green">0xFFFF</span>



9. 비트 시프트 연산자의 활용이다. 결과를 예측하시오. 

a=100; a=a<<100 ; a=a>>100; print(a)

<span style="color:green">100</span>

10. 다음 중첩 if문을 elif를 사용하는 코드로 변경하시오.

score=55
if score >= 60 :
    print("합격이다.")
else :
    if score >= 40 :
         print("불합격 이지만 과락은 아닙니다.")


```python
score = 55
if score>=60 :
    print('합격이다.')
elif score >=40 :
    print('불합격 이지만 과락은 아닙니다.')
else:
    print('불합격 이면서 과락입니다.')
```

    불합격 이지만 과락은 아닙니다.
    
