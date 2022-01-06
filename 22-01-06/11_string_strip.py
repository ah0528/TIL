# 2. 필요없는 문자열 삭제하기 : strip() 메서드
# 형식 : str.strip()
# 문자열(str)의 앞과 뒤에서 시작해서 지정한 문자 외의 다른 문자를 만날 때까지 지정한 문자를 모두 삭제한 문자열을 반환
# 만약 지정한 문자와 일치하는 것이 없으면 문자열을 그대로 반환
# 지정한 문자가 여러 개일 경우 순서는 상관없음
# 지정한 문자 없이 str.strip()으로 사용할 경우, 공백과 개행문자를 삭제함

str = 'Python    '
print(str.strip())

str1 = 'aaaaPythonaaaa'
# str1에서 a 제거하기
print(str1.strip('a'))

str2 = 'aaabbPythonbbbba'
# str2에서 a와 b 삭제하기
# 방법 1.
str_strip = str2.strip('a')
print(str_strip.strip('b'))
# 방법 2. 한 번에 제거
print(str2.strip('ab'))    # 'ba'여도 같은 결과가 반환됨

test_str_multi = '##**#!!...    Python is powerful.!##!%%'
print(test_str_multi.strip('#*!.% '))

print('aaaaBallaa'.strip('a'))  # 질문) Ball의 a는 삭제되지 않는 이유

# 문자열의 앞이나 뒤 중에서 한쪽만 삭제하고 싶으면 lstrip()나 rstrip() 메서드를 사용
str_lr = '0000Python is easy to learn.000'
print(str_lr.lstrip('0'))    # 왼쪽만 삭제
print(str_lr.rstrip('0'))    # 오른쪽만 삭제
print(str_lr.strip('0'))     # 양쪽 삭제

coffee_menu = '    에스프레소, 아메리카노,    카페라떼    , 카푸치노    '
coffee_menu_list = coffee_menu.split(',')

coffee_list = []
for i in coffee_menu_list:
    coffee = i.strip()
    coffee_list.append(coffee)
print(coffee_list)