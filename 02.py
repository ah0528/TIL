long_string1 = '''[삼중 작은 따옴표를 사용한 예]
파이썬에서는
큰따음표(")와 작은따옴표(')도 입력할 수 있습니다.'''

print(long_string1)

a = [1,2,3,4,5]
b = tuple([1,2,3,4,5])
print(b)

dict_data3 = {'list_data1':[11,12,13], 'list_data2':[21,22,23]}
print(dict_data3)
print(dict_data3['list_data1'])

set1 = {1,}
set1.update('학생','학원')
print(set1)

dict_fruits = {'사과':101,'배':102,'딸기':103}
dict_fruits2 = {'귤':104,'사과':102}
dict_fruits.update(dict_fruits2)
print(dict_fruits)
