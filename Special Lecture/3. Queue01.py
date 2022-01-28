# 함수


# 전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1 # front와 rear 초기화


# 메인
# enQueue

rear += 1
queue[rear] = '멍멍이'

rear += 1
queue[rear] = '야옹이'

rear += 1
queue[rear] = '호랑이'

print('출구<--', queue, '<--입구 ')

# deQueue
front += 1
data = queue[front]
queue[front] = None
print('밥 손님:',data)

front += 1
data = queue[front]
queue[front] = None
print('밥 손님:',data)

front += 1
data = queue[front]
queue[front] = None
print('밥 손님:',data)

print('출구<--', queue, '<--입구 ')