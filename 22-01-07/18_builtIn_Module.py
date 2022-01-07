# 내장모듈

# random 모듈 예시
import random

print(random.random())
print(random.randint(50,60))
print(random.randrange(1,10,2))
print(random.choice([1,2,3,4,5]))
print(random.sample(('사과','수박','배','바나나'),2))

# datetime 모듈 예시
import datetime

# 객체를 생성해 이용하기
date_obj = datetime.date(2022,1,7)
print(date_obj)
time_obj = datetime.time(13,20,55)
print(time_obj)
datetime_obj = datetime.datetime(2030,5,28,15,30,13)
print(datetime_obj)

# 클래스 메서드를 이용하기
# date_var = datetime.date.date_classmethod()
# time_var = datetime.time.time_classmethod()
# datetime_var = datetime.datetime.datetime_classmethod()

# calendar 모듈
import calendar

print(calendar.calendar(2021))
print(calendar.month(2021, 1))
print(calendar.monthrange(2020,5))
calendar.setfirstweekday(6)  # 주의 첫 번째 요일을 일요일로 지정
print(calendar.month(1997,5))
print(calendar.weekday(1997,5,28))
print(calendar.isleap(1997))
