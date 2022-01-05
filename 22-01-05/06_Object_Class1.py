# 객체와 클래스
# 클래스명이 Bicycle인 자전거 클래스를 만들어보자. (교재 p.137)

# 객체 생성한 후 객체의 속성을 설정해 클래스 정의하기
class Bicycle:
    def move(self,speed):
        print(f'자전거 : 시속 {speed}킬로미터로 전진')

    def turn(self, direction):
        print(f'자전거 {direction}방향으로 회전')

    def stop(self):
        print(f'자전거({self.wheel_size}인치, {self.color}) 정지')

my_bicycle = Bicycle()

my_bicycle.wheel_size = 26
my_bicycle.color = 'black'
my_bicycle.stop()

# 객체 초기화(생성자)를 이용해 클래스 정의하기
class Bicycle2:
    # a방법
    # def __init__(self):
    #     self.wheel_size = 25
    #     self.color = 'red'
    # b방법
    def __init__(self, wheel_size, color):
        self.wheel_size = wheel_size
        self.color = color

    def move(self,speed):
        print(f'자전거 : 시속 {speed}킬로미터로 전진')

    def turn(self, direction):
        print(f'자전거 {direction}방향으로 회전')

    def stop(self):
        print(f'자전거({self.wheel_size}인치, {self.color}) 정지')


# a방법
# my_bicycle2.wheel_size = 21
# my_bicycle2.color = 'Yellow'
# b방법
my_bicycle2 = Bicycle2(30,'purple')

my_bicycle2.turn('우')
my_bicycle2.stop()