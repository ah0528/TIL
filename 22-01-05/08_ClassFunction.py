# 클래스에서 사용하는 함수
# 1. 인스턴스 메서드:
#     각 객체에서 개별적으로 동작하는 함수를 만들고자 할 때 사용하는 함수
#     함수를 정의할 때 첫 인자로 self가 필요(self: 클래스의 인스턴스 자신을 가르킴)
#     인스턴스 메서드에서는 self를 이용해 인스턴스 변수를 만듦 - self.변수명 = 인자
#     인스턴스 메서드 안에서는 self.메서드명() 형식으로 클래스 내의 다른 함수 호출가능
class Car():
    instance_count = 0  # 클래스 변수 생성

    def __init__(self, size, color):  # 인스턴스 메서드인 _init__()
        self.size = size
        self.color = color
        Car.instance_count += 1
        print(f'자동차 객체의 수는 {Car.instance_count}개 입니다.')

    def move(self, speed):  # 인스턴스 메서드인 move()
        self.speed = speed
        print(f'크기가 {self.size}이고 색이 {self.color}인 자동차가 {self.speed}의 속도로 움직인다.')

    def auto_cruise(self):
        print('자율주행모드입니다.')
        self.move(self.speed)


car1 = Car('Big', 'Red')
car1.move(30)
car1.auto_cruise()       # auto_cruise() 함수를 호출하려면 move()함수가 호출되어있어야한다.