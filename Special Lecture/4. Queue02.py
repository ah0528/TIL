# 함수
def isQueueFull():
    global SIZE, queue, front, rear
    if (rear == SIZE-1):

        return True
    else:
        return False

def enQueue(data):
    global SIZE, queue, front, rear
    if (isQueueFull()):
        print("큐 꽉 차있음!")
        return
    rear += 1
    queue[rear] = data

def isQueueEmpty():
    global SIZE, queue, front, rear
    if(front == rear):
        return True
    else:
        return False

def deQueue():
    global SIZE, queue, front, rear
    if(isQueueEmpty()):
        print('큐 텅~!')
        return None
    front += 1
    data = queue[front]
    queue[front] = None     # 복사 했으니 초기화해줌
    return data

def peek():     # 다음에 나갈 것 확인만 하기
    global SIZE, queue, front, rear
    if(isQueueEmpty()):
        print("큐 텅~!")
        return None
    return queue[front+1]



# 전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1 # front와 rear 초기화

# 메인
enQueue('호랑이')
enQueue('멍멍이')
# enQueue('야옹이')
# enQueue('수달이')
# enQueue('토깽이')
# print('출구<--', queue, '<--입구')
# enQueue('어흥이')
# print('출구<--', queue, '<--입구')

print('출구<--', queue, '<--입구')
print('밥 손님 :',deQueue())
print('다음 입장 예정 손님 :', peek())
print('밥 손님 :',deQueue())
print('출구<--', queue, '<--입구')
print('밥 손님 :',deQueue())
