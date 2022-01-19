# my_module.py

def func(a):
    print('입력한 숫자 :',a)

if __name__ == '__main__':
    print('모듈을 직접 실행')    # 모듈을 직접 수행할때만 실행되는 코드
    func(5)
    func(10)
else:
    print('my_module을 임포트해서 실행')   # 임포트됐을 때만 실행되는 코드
