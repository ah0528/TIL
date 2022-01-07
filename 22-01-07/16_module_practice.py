# # 형식 1 예시
# import my_first_module
# my_first_module.my_function()
#
# import my_area
# print(my_area.square_area(5))
#
# # 형식 2 예시
# from my_area import circle_area
# print(circle_area(10))
#
# from my_area import PI, circle_area, square_area  # 콤마로 구분해서 여러 개를 선언할 수 있음
# print(PI)

# 형식 3 예시
import my_area as area
print(area.circle_area(20))

from my_area import square_area as s_area
print(s_area(7))

# print(dir(my_area))    # 불러온 모듈에서 사용할 수 있는 변수, 함수, 클래스를 알 수 있음
