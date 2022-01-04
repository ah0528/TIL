# 인자를 받아서 처리한 후 값을 반환하는 함수 만들기
# 사각형의 넓이를 구하는 함수 만드시오
'''
def area(x,y):
    return x*y

print(area(2,4))


def student_Info(studentInfo):
    print('----------')
    print(f'이름 : {studentInfo[0]}')
    print(f'학번 : {studentInfo[1]}')
    print(f'전화번호 : {studentInfo[2]}')

student_Info(['김현아', 456, '010-1234-1234'])


# 변수의 유효범위 - 전역변수, 지역변수

a = 5

def func1():
    a = 4
    print('func1의 a :', a)

def func2():
    global a
    a = 3
    print('func2의 a :', a)

func1()
func2()
print('전역변수 a의 값은 ?',a)
'''

# lambda함수
#1.(lambda 인자:인자 활용수행 코드)(인자)
print((lambda x,y:x**y)(3,2))

#2. lambda 함수를 변수에 할당하여 사용
lambda_func = lambda x,y:x**y
print(lambda_func(5,2))
