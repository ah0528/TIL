# 파일 입력과 출력

with open('test.txt','w') as f:
    for i in range(1,10):
        f.write(f'2 * {i} = {2*i}\n')

with open('test.txt','r') as f:
    line1 = f.readline()
    line2 = f.readline()
    print('첫번째 줄', line1,end='')
    print('두번째 줄', line2)


with open('test.txt', 'r') as f:
    while True:
        data = f.readline()
        if data != '':
            print(data, end='')
        else:
            break

with open('test.txt', 'r') as f:
    data = f.readlines()
    print(type(data))
    print(data)

#
with open('test.txt', 'r') as f:
    for data in f.readlines():
        print(data, end='')


with open('test.txt', 'r') as f:
    for data in f:                # for문에서는 f.readlines()와 f가 같음
        print(data, end='')

#
with open('test2.txt','w') as f:
    for num in range(1,10):
        f.write(f'3 * {num} = {3*num}\n')

with open('test2.txt', 'r') as f:
    for line in f:
        print(line, end='')

