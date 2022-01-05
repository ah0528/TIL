# 클래스에서 사용하는 함수
# 1. 인스턴스 메서드:
# 각 객체에서 개별적으로 동작하는 함수를 만들고자 할 때 사용하는 함수
# 함수를 정의할 때 첫 인자로 self가 필요(self: 클래스의 인스턴스 자신을 가르킴)
# 인스턴스 메서드에서는 self를 이용해 인스턴스 변수를 만듦 - self.변수명 = 인자
# 인스턴스 메서드 안에서는 self.메서드명() 형식으로 클래스 내의 다른 함수 호출가능
class Car:
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

# 2. 정적 메서드:
# 클래스 안에 있지만, 클래스나 클래스의 인스턴스와는 무관하게 독립적으로 동작하는 함수
# 함수를 정의할 때 인자로 self를 사용하지 않음
# 정적 메서드 안에서는 인스턴스 메서드나 인스턴스 변수에 접근할 수 없음
# 함수 정의 전에 데코레이터인 @staticmethod를 선언해 정적 메서드임을 표시해야함
'''class Car2:
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

    @staticmethod    # 정적 메서드임을 표시함
    def check_type(model_code):
        if model_code >= 20:
            print('이 자동차는 전기차입니다.')
        elif model_code >= 10:
            print('이 자동차는 가솔린차입니다.')
        else:
            print('이 자동차는 디젤차입니다.')

Car.check_type(25)
'''
# 3.클래스 메서드 :
# 클래스 변수를 사용하기 위한 함수
# 클래스 메서드는 함수를 정의할 때 첫 번째 인자로 클래스를 넘겨받는 cls가 필요함
# 클래스 메서드를 사용하기 위해서는 함수 앞에 데코레이터인 @classmethod를 지정해야함
# 정적 메서드와 같이 객체를 생성하지 않고 클래스명을 이용해 바로 호출가능

class Car3:
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

    @classmethod
    def count_instance(cls):
        print(f'자동차 객체의 개수 : {cls.instance_count}')

Car3.count_instance()
car5 = Car3('small', 'pink')
Car3.count_instance()
