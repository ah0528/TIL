# 6. 문자열 찾기 : find() 메서드
# 형식 : str.find(search_str)
# 문자열에서 찾으려는 검색 문자열과 첫 번째로 일치하는 문자열의 위치를 반환하고 찾을 수 없다면 -1 반환
# 문자열의 위치는 0부터 시작

str_f = 'Python code.'
print(str_f.find('Python'))
print(str_f.find('code'))
print(str_f.find('o'))
print(str_f.find('easy'))

# 검색 범위 지정가능 :
# str.find(search_str, start, end)    start ~ end-1 범위에서 찾음
# str.find(search_str, start)         start부터 문자열 끝까지 찾음
str_f_se = 'Python is powerful. Python is easy to learn.'
print(str_f_se.find('Python', 15, 30))
print(str_f_se.find('Python', 35))

# 만약 찾은 문자열이 몇 번 나오는지 알고 싶다면 count() 메서드를 이용하면 됨
# 형식 : str.count(search_str)
#       str.count(search_str,start,end)
#       str.count(search_str,start)
# 문자열에서 찾고자 하는 문자열과 일치하는 횟수를 반환하고, 없으면 0을 반환

str_c = 'Python is powerful. Python is easy to learn. Python is open.'
print(str_c.count('is'))
print(str_c.count('welcome'))
print(str_c.count('Python', 10))

# 지정된 문자열으로 시작하는지/끝나는지 검사하는 메서드 : startswith(), endswith() 메서드
# 형식 : str.startswith(prefix[, start, end]), str.endswith(prefix[, start, end])
# 시작하거나 끝난다면 True를, 그렇지 않다면 False를 반환

str_se = 'Python is powerful. Python is easy to learn.'
print(str_se.startswith('Python'))
print(str_se.startswith('Python', 7))
print(str_se.endswith('learn.'))
print(str_se.endswith('.'))