## 함수


## 전역
# stack=[None, None, None, None, None]  
SIZE = 5
stack = [None for _ in range(SIZE)]    #스택을 빈리스트로 정의
top = -1            # 스택이 비어있음을 의미(스택의 초기화)

## 메인
# PUSH
top += 1
stack[top] ='커피'

top += 1
stack[top] = '녹차'

top += 1
stack[top] = '꿀물'

print(stack)

# POP
data = stack[top]
stack[top] = None # data에 뺀 스택의 값이 들어있으니, 빈 곳은 깨끗하게 None으로 지정.
top -= 1
print('팝-->', data)

data = stack[top]
stack[top] = None
top -= 1
print('팝-->', data)

data = stack[top]
stack[top] = None
top -= 1
print('팝-->', data)

print(stack)