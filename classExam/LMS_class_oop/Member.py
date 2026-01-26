# Member.py 는 각 회원에 자료를 담당한다.
# 웹 프로그래밍에 백엔드에는 데이터베이스와 결합하는데
# MemberDTO, MemberVO 라는 이름으로 사용된다.
# DTO = Data Transfer Object, 데이터 전송 객체 라고함
# VO = Value Object, 값 그 자체 라고함


# 회원 각각의 자료를 리스트가 아닌 변수에 담아 제공하려고 함

class Member: # 클래스는 대문자로 시작 해야함 Member 이런식
    def __init__(self, uid, pw, name, role="user",active=True):
        self.id = uid           # id
        self.pw = pw            # pw
        self.name = name        # 이름
        self.role = role        # 권한
        self.active = active    # 활성화여부

        # 사용법 member = Member() -> 객체를 생성해서 변수에 연결함.
        # 이름 : member.id
        # 암호 : member.pw

        # 파일 저장용 문자열 변환

    def to_line(self):
        return f"{self.id}|{self.pw}|{self.name}|{self.role}|{self.active}\n"



        # 사용법  = member - Member()
        # member.to_line() -> kkw|1234|김기원|admin|True엔터
        # 메모장에 객체 기록용

        # 파일에서 불러온 내용 객체처리


    # @classmethod # 객체(self)가 아니라 클래스 자체를 (cls)를 다루는 메서드 라고 정의를 해줌
    # def from_line(cls, line): # line = 메모장의 문자열 한줄
    #     line = line.split()
    #     if not line:
    #         return None
    #     parts = line.split("|")
    #     if len(parts) < 5:
    #         parts +=['Y'] * (5 - len(parts))
    #     uid,pw,name,role,active = parts
    #     return cls(uid,pw,name,role,active)

    @classmethod
    def from_line(cls, line):
        line = line.strip()  # 줄 끝 공백/엔터 제거
        if not line:  # 빈 줄이면 None 반환
            return None
        parts = line.split("|")  # 여기서 문자열을 |로 나눔
        if len(parts) < 5:  # 부족한 값은 기본값 채움
            parts += ['Y'] * (5 - len(parts))
        uid, pw, name, role, active = parts
        active_bool = active in ['True', 'Y', 'y', True]
        return cls(uid, pw, name, role, active_bool)

    # 사용법 : m = Member(uid,pw,name,role,active) -> 권장하지 않음(바로 넣는방법)
    #         self를 이용하는방법임(객체변수)

    # 권장법 : m = Member.from_line(line) -> 권장이유 : 객체생성 책임을 클래스가 담당하기때문
    #         cls를 사용하는 방법(클래스변수)


    # 면접시 자주 물어보는 내용
    # 직렬화, 역직렬화 가 뭔지?

    # 직렬화(Serialization) : 객체를 저장가능한 형태로 바꾸는것 (메모리에있는것을 파일로만드는)
    #       member.to_line() 이게 직렬화 임

    # 역직렬화(Deserialization) : 저장된 데이터를 객체로 만들때 사용 -> 객체 (@classmethod)
    #       Member.from_line(line) 이게 역직렬화 임


