# 클래스는 대부분 파일명을 대문자로 만드는게 관례이다
# 클래스는 인스턴스를 목적으로 만든다.

class Calculator: # 파일 명과 클래스 명도 대문자로 시작
    # : (콜론) 으로 끝나기 떄문에 들여쓰기 해야함
    # 내부에 함수(메서드)를 생성한다.
    def __init__(self):
        # 초기화 메서드(init)
        # 클래스 선언시 기본적으로 실행되는 문법
        self.result = 0 # 클래스가 생성되면서 변수를 만듬

    def add(self, num):
        self.result += num
        return self.result


    def sub(self,num):
        self.result -= num
        return self.result


    def mul(self,num):
        self.result *= num
        return self.result


    def div(self,num):
        self.result /= num
        return self.result


# class 선언 종료
cal1 = Calculator()# 객체에 변수를 연결함
cal2 = Calculator()
# 클래스를 사용하려면 변수에 연결해야함 그래야 (스택 과 힙 영역이 연결)
# 이때 사용하는 게 self
# 객체 인스턴스 생성 과 변수 연결 (self) 끝



# 객체.메서드(값) self 로 연결된 주소의 객체를 찾아서
# .add(5) 를 실행 -> '메서드'라고함
kkwresult = cal1.add(5)
print(kkwresult)

ksbresult = cal2.add(7)
print(ksbresult)

print(cal1.mul(10))
print(cal2.add(9))
print(cal1.sub(11))

