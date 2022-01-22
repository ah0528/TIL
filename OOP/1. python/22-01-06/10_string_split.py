# 문자열 다루기
# 1. 문자열 분리하기 : split() 메서드
# 형식 : str.split([sep])
# 구분자인 sep을 기준으로 문자열을 분리해 리스트로 반환
# 구분자를 입력하지 않고 수행하면 문자열 사이의 모든 공백과 개행문자(\n)를 없애고 분리된 문자열을 항목으로 담은 리스트를 반환

str = '에스프레소 바닐라라떼 아메리카노 카푸치노'
print(str.split())

coffee_menu_str = '에스프레소, 바닐라라떼, 아메리카노, 카푸치노'
print(coffee_menu_str.split(','))

print('에스프레소, 바닐라라떼, 아메리카노, 카푸치노'.split(','))    # 문자열을 변수에 할당하지 않고 직접 split() 메서드를 사용할 수 있음

# 인자 maxsplit을 추가하면 앞에서부터 원하는 횟수만큼만 문자열을 분리 : str.split([sep,] maxsplit=숫자)
print('바나나 사과 멜론 토마토 배'.split(maxsplit=2))    # 앞에서부터 2번만 문자열을 분리하여라.

# 문제 : 국가 번호까지 있는 전화번호에서 국가 번호를 뺀 나머지 번호를 구하는 코드를 작성하시오.
phone_number = '+82-01-2345-6789'
tel = phone_number.split('-',maxsplit=2)
print(tel)
first = tel[1] + '0-'
print(f'국가 번호를 뺀 전화번호 : {first+tel[2]}')

#    교재 답안---------
phone_number = '+82-01-9876-5432'
split_num = phone_number.split('-',1)

print(f'국내전화번호 : {split_num[1]}')