# 클래스 용도로 파일 생성시 대문자로 시작

class FourCal:
    # pass #아무동작 안하고 넘어가는 코드

    # 변수 선언부 __init__
    def __init__(self):
        self.first = 0
        self.second = 0
        # 이건 취약한 코드 라고함



    # 메서드 선언부

    # 세터와 게터를 이용해 구현을 함
    def setdata(self, first, second):
# a.first 와 a.second 를 직접 가서 처리가 가능하지만 검증해서 값을 처리 하는것도 필요하다
# 데이터를 넣는 메서드를 세터 라고한다.

        if first <= 0 :
            self.first = 0
        else :
            self.first = first
        if second <= 0 :
            self.second = 0
        else :
            self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def div(self):
        result = self.first / self.second
        # 나누는 값이 0이면 pc는 오류를 발생시킴
        return result






a = FourCal()

#a.first = 100 # 객체 변수에 바로 입력이 됨
#a.second = 200
a.setdata(-10,10)
result1 = a.add()
print(f"-10+10을 : add() 메서드 실행결과 : {result1}")

result2 = a.add()




print(a.first) # 객체 변수에 바로 출력이 됨
print(a.second)
# 위에 방법은 개발자들이 취약한 코드라고 판단을해서 안함
# 바로 넣는것보다 검증을 거쳐서 넣는다.





# a 변수에 FourCal() 클래스를 연결한다.
print(type(a))
# 출력하면 이렇게 나옴 <class '__main__.FourCal'>
# __main__ <<는  모듈의 이름을 담고있는 파이썬 내장 변수
# 최상위 코드가 실행되는 환경의 이름( 주 실행코드)
# 건물에는 무조건 1층 입구가 있듯이 프로그램 실행은 main 으로 판단을한다고함.

class MorFourCal(FourCal):
    #               부모객체(+,-,*,/ 사칙연산 기능을 넣었으면 이런게 들어있음 다른것도 가능)
    # 부모객체의 모든 기능을 사용하면서 추가 메서드를 만든다.
    def pow(self):
        result = self.first ** self.second
        #           부모의 추가 메서드(제곱)
        return result

    def div(self): # 부모와 같은 메서드명
        if self.second == 0:
            # 나누는 뒷 값이 0이면 나눌 필요없이 0을 리턴
            return 0
        else:
            return self.first / self.second



c = MorFourCal()
c.add() # 부모의 메서드 활용
c.pow() # 자식의 메서드 활용


# 메서드 오버라이딩 ( 부모가 만든 메서드를 튜닝할때)

# d = FourCal()
# d.setdata(8,0)
# result = d.div()
# print(result)

e = MorFourCal()
e.setdata(9,0)
result = e.div() # 부모에서 개선된 자식 div() 를 실행함.
print(result)

# 클래스 변수(필드)라고 함 : __init__ or 일반 메서드에 밖 변수
class Family :
    lastname = "김"


    # 밑에는 메서드들이 들어감

print(Family.lastname) # 쓰지마셈 전역변수

a = Family()
b = Family()
a.lastname = "최"
print(a.lastname)
print(b.lastname)













