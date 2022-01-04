# if문
x = 100
if x>=90:
    if x == 100:
        print('Perfect')
    else:
        print('Very good')
elif x>=80 and x<90:
    print('Good')
else:
    print('Bad')

# 반복문 1. for문 - 지정된 범위만큼 반복
names = ['James','Robert','Lisa','Mary']
scores = [95,96,97,94]

for i in range(len(names)):
    print(names[i], scores[i])

##문제 반복문 1의 예제를 zip()함수를 이용해 풀어보시오.

# 반복문 2. while문 - 조건에 따라 반복
##문제 자연수 1부터 순차적으로 더해서 출력하다가 합이 20보다 크면 멈추는 while문을 작성하시오.

i = 0

while True:
    i += 1
    print(i)
    if i>3:
        break
    print(i)

# 리스트 컴프리헨션
## 문제1. 1~5까지 숫자가 들어있는 리스트에서 각 항목의 숫자를 제곱하는 반복문을 작성하시오

## 문제2. 문제1을 컴프리헨션을 사용하여 작성하시오

## 문제3. 3이상의 숫자만 제곱하도록 하는 반복문을 작성하시오
num = [1,2,3,4,5]
result = []
for k in num:
    if k>=3:
        result.append(k**2)
print(result)

result2 = [k**2 for k in num if k>=3]
print(result2)

name = 'faru'
print('이름은 %s' % name)

a = 0.1234567890123456789
print('{0:.2f},{0:.8f}'.format(a))

