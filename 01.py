# 10진법, 2진법, 8진법, 16진법
# 2진수를 --> 10진수로 0b(2진수로 나타낸 수)
# 8진수로 --> 10진수로 0o(8진수로 나타낸 수)
# 16진수로 --> 10진수로 0x(16진수로 나타낸 수)

print(17)
print(0b10001)
print(0o21)    #2진수로 나타낸 수를 뒤에서부터 3자리씩
print(0x11)    #2진수로 나타낸 수를 뒤에서부터 4자리씩


# 10진수를
# 2진수로 나타내는 함수 bin(10진수의 수)
# 8진수로 나타내는 함수 oct(10진수의 수)
# 16진수로 나타내는 함수 hex(10진수의 수)
# 주의 : 출력결과는 문자열이므로 진수변환은 연산이 모두 끝난 후에 해야한다.
print(bin(0o21+0x11))

 
