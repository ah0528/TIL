# 함수
def isStackFull():      # 스택이 꽉 찼는지 확인하는 함수 정의(True/False를 반환)
    global SIZE, stack, top
    if (top >= SIZE-1):  # top이 스택의 크기 -1 보다 크거나 같으면(스택이 꽉 찬 상태면)
        return True
    else:
        return False


def push(data):
    global SIZE, stack, top
    if (isStackFull()):
        print('스택 꽉!')
        return                   # 스택이 꽉 차 있으면 push를 못하니까 아무것도 넣지 않고 return하면 됨
    top += 1
    stack[top] = data

def isStackEmpty():     # 스택이 비어있는지 확인하는 함수 정의
    global SIZE, stack, top
    if (top <= -1):
        return True
    else:
        return False

def pop():
    global SIZE, stack, top
    if (isStackEmpty()):
        print("스택이 텅~")
        return None
    
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek():         # 다음에 나올 아이 확인만 하는 함수 peek() 정의
    global SIZE, stack, top
    if (isStackEmpty()):
        print("스택 텅~")
        return None
    
    return stack[top]


# 전역
SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1

# 메인

push('커피1')
push('커피2')
# push('커피3')
# push('커피4')
# push('커피5')
print(stack)
# push('커피6')

print('다음 예정-->',peek())

retData = pop()  # pop은 data를 return하니까 변수로 받아줘야 함
print("pop한 데이터->", retData)
retData = pop()
print("pop한 데이터->", retData)
retData = pop()
print("pop한 데이터->", retData)
print(stack)