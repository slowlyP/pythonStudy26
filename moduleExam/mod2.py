# 이번엔 클래스와 변수 등을 포함하는 import 를 만들어보쟈


PI = 3.1415926 # 대문자로 변수 를 만들면 상수 역할을 함( 변하지 않는 값 )
class Math: # math 클래스
    def solv(self,r): # r은 반지름
        return PI * (r**2)# 원의 넓이를 구하는 공식
    # 원의 넓이 구하는 메서드 종료

def add(a,b):
    return a+b
