# 클래스 상속 (Inheritance) - 코드의 재사용성이 좋아짐
# 상속하는 클래스 : 부모 클래스, 슈퍼 클래스, 상위 클래스
# 상속받는 클래스 : 자식 클래스, 서브 클래스, 하위 클래스
# 자식 클래스는 부모 클래스의 변수와 함수를 그대로 이용가능하고, 자식 클래스만 갖는 변수와 함수를 추가할 수 있음
# 부모 클래스가 미리 선언이 되어있어야 자식 클래스를 선언할 수 있음
# 부모 클래스과 자식 클래스에서 정의한 함수명이 같은 경우 부모 클래스의 함수를 호출하려면 명시적으로 부모클래스명.함수명()으로 호출하거나, super().함수명()을 사용해야함

class Bicycle:
    def __init__(self, wheel_size, color):
        self.wheel_size = wheel_size
        self.color = color

    def move(self,speed):
        print(f'자전거 : 시속 {speed}킬로미터로 전진')

    def turn(self, direction):
        print(f'자전거 {direction}방향으로 회전')

    def stop(self):
        print(f'자전거({self.wheel_size}인치, {self.color}) 정지')

class FoldingBicylce(Bicycle):
    def __init__(self, wheel_size, color, state):
        super().__init__(wheel_size, color)
        self.state = state

    def fold(self):
        self.state = 'folding'
        print(f'자전거 : 접기, {self.state}')

    def unfold(self):
        self.state = 'unfolding'
        print(f'자전거 : 펼침, {self.state}')

my_bicycle = FoldingBicylce(26,'yellow','folding')
my_bicycle.fold()
