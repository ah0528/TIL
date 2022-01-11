# 실습문제 : dictionary

1. 학생들의 이름과 성적을 딕셔너리로 저장하고 있다. 이 딕셔너리를 사용하여 각 학생의 성적에 대한 총점과 평균을 계산하여 코드를 작성하시오.

students = [
   {"name" : "홍길동", "korean" : 87, "math" : 98, "english" : 88, "science" : 95},
   {"name" : "이몽룡", "korean" : 92, "math" : 98, "english" : 96, "science" : 98},
   {"name" : "성춘향", "korean" : 76, "math" : 96, "english" : 94, "science" : 90},
   {"name" : "변학도", "korean" : 98, "math" : 92, "english" : 96, "science" : 92},
   {"name" : "박지성", "korean" : 95, "math" : 98, "english" : 98, "science" : 98},
   {"name" : "류현진", "korean" : 64, "math" : 88, "english" : 92, "science" : 92}
]


```python
students = [
   {"name" : "홍길동", "korean" : 87, "math" : 98, "english" : 88, "science" : 95},
   {"name" : "이몽룡", "korean" : 92, "math" : 98, "english" : 96, "science" : 98},
   {"name" : "성춘향", "korean" : 76, "math" : 96, "english" : 94, "science" : 90},
   {"name" : "변학도", "korean" : 98, "math" : 92, "english" : 96, "science" : 92},
   {"name" : "박지성", "korean" : 95, "math" : 98, "english" : 98, "science" : 98},
   {"name" : "류현진", "korean" : 64, "math" : 88, "english" : 92, "science" : 92}
]
print('이름   총점   평균')
title = ['korean', 'math', 'english', 'science']
for i in range(len(students)):
    total = 0
    for score in title:
        total += students[i][score]
    print(students[i]['name'],total,total/len(title))
```
2. 딕셔너리를 이용하여 사용자로부터 영어단어와 뜻을 입력받아 사전을 구성하고, 사용자가 입력한 단어를 검색하여 뜻을 출력하는 프로그램을 작성하시오.
voca = {}
while True:
    str_a = input('영어 단어 등록 (종료는 quit): ')
    if str_a == 'quit':
        break
        
    elif str_a in voca:
        print(f'{str_a}는 이미 등록된 단어 입니다.')
        
    else:
        str_b = input(f'{str_a}의 뜻입력 (종료는 quit):')
        if str_b != 'quit':
            voca[str_a] = str_b


while True:
    str_s_a = input('검색할 단어 등록 (종료는 quit): ')
    if str_s_a == 'quit':
        print('종료합니다')
        break
        
    elif str_s_a not in voca:
        print(f'{str_s_a}는 사전에 없는 단어 입니다.')
        
    else:
        print(f'{str_s_a}의 뜻은 {voca[str_s_a]}입니다.')