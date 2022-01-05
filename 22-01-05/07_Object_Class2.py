# 클래스 변수와 인스턴스 변수
# 클래스 변수 :
# 정의 : 변수명 = 데이터
# 접근 : 클래스명.변수명

# 인스턴스 변수:
# 정의 : self.변수명 = 데이터
# 접근 : self.변수명

class Car:
    instance_count = 0    # 클래스 변수
    def __init__(self, size, color):
        self.size = size  # 인스턴스 변수
        self.color = color # 인스턴스 변수
        Car.instance_count += 1 # 클래스 변수에 접근! 클래스명.변수명
        print(f'자동차 객체의 수 : {Car.instance_count}개')

    def move(self):
        print(f'크기가 {self.size}이고 색이 {self.color}인 자동차가 이동합니다.')

car1 = Car('big', 'red')
car2 = Car('small', 'black')
car2.move()

class Car2:
    count = 0
    def __init__(self, size, color, count):
        self.size = size  # 인스턴스 변수
        self.color = color # 인스턴스 변수
        self.count = count # 인스턴스 변수
        Car2.count += 1  # 클래스 변수에 접근! 클래스명.변수명
        print(f'자동차 객체의 수 : {Car2.count}개')
        print(f'자동차 크기는 {size}, 색은 {color}, 변수초기화 : self.count = {self.count}')

car2_1 = Car2('big', 'Yellow', 20)
car2_2 = Car2('medium', 'White', 30)
# ===> 알 수 있는 점 : 클래스 변수와 인스턴스 변수는 변수명이 같아도 다른 것이다.
