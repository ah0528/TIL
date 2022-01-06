# 3. 문자열 연결하기 : join() 메서드
# 형식 : str.join(시퀀스)
# 리스트의 모든 항목을 하나의 문자열로 만듦
# 문자열을 항목으로 갖는 시퀀스의 항목 사이에 구분자 문자열(str)을 모두 넣은 후 문자열로 반환
# 시퀀스란. 리스트나 튜플과 같이 여러 데이터를 순서대로 담고 있는 나열형 데이터

address_list = ['서울시', '서초구', '반포대로', '201(반포동)']
a = ' '    # 구분자 문자열을 공백으로 할당 : 문자열 사이에 공백을 주겠다
print(a.join(address_list))


# 4. 문자열 바꾸기 : replace() 메서드
# 형식 : str.replace(old, new[, count])

str_r = 'Python is powerful. Python is easy to learn. Python is open.'
print(str_r.replace('Python', 'IPython'))
print(str_r.replace('Python', 'IPython', 2))

# 특정 문자열을 삭제할 때도 replace() 메서드를 이용할 수 있음
str_b = '[Python] [is] [fast]'
str_b1 = str_b.replace('[', '')
str_b2 = str_b1.replace(']', '')
print(str_b2)


# 5. 대소문자로 변경하기 : upper(), lower() 메서드
# 형식 : str.upper(), str.lower()
# 파이썬에서는 대소문자를 구분하므로 같은 의미의 문자열을 비교하더라도 대소문자까지 같지 않으면 다른 문자열임
string1 = 'Python is powerful. PYTHON IS EASY TO LEARN.'
print(string1.upper())
print(string1.lower())

print('python' == 'Python')
print('python'.upper() == 'Python'.upper())
print('python'.lower() == 'Python'.lower())