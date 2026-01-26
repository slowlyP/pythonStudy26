# Member 객체를 CRUD 기능을 넣는다.
# 메뉴 구현
# 텍스트 파일 처리(파일읽기, 파일저장)
# 회원 가입, 로그인, 로그아웃, 회원수정, 회원탈퇴, 등등
import os
from Member import Member # 회원 객체 추가연결
# 사용법 member = Member() -> 이러면 객체가 생성됨
#       member. 필드/메서드 = .찍으면 나옴


class MemberService:
    def __init__(self,file_name="members.txt"): #클래스가 생성할때 초기값 을 관리해줌.
        self.file_name = file_name
        self.members = [] # 회원들을 리스트로 만들어서 Member() 객체를 담는다.
        self.session = None # 로그인 상태를 담당(members의 인덱스 보관용)
        self.load_members() # 아래쪽에 메서드 호출

    def run(self):
        run = True
        while run:
            self.main_menu()
            sel = input(">>>")

            if sel == "1": self.member_add()
            elif sel =="2": self.member_login()
            elif sel =="3": self.member_logout()
            elif sel =="4": self.member_modify()
            elif sel =="5": self.member_delete()
            elif sel =="9": run = False
            else:
                print("잘못 입력하셧습니다.")



    def load_members(self): # 파일에서 메모리로 불러온다.
        if not os.path.exists(self.file_name):
            self.save_members()
            return
        self.members = []
        with open(self.file_name,"r",encoding="utf-8") as f:
            for line in f:
                self.members.append(Member.from_line(line))
                #                   Member 객체에 .from_line() 메서드 실행
                #                                한줄을 가져와 클래스로 만듬
                #   members 리스트 뒷부분에 추가




    def main_menu(self):
        print("""
===회원관리 프로그램===
1. 회원가입
2. 로그인
3. 로그아웃
4. 회원정보수정
5. 회원탈퇴
9. 종료
====================
""")

    def member_add(self):
        print("\n[회원가입]")
        uid = input("아이디 : ")

        if self.find_member(uid): # 자주쓰는 중복코드로 메서드 처리함
            print("이미 존재하는 아이디입니다.")
            return
        pw = input("비밀번호 : ")
        name = input("이름 : ")
        role = "user"

        self.members.append(Member(uid,pw,name,role))
        #                   Member 클래스의 init 메서드로 바로 들어가 객체를 생성함 간편하게 할수있뜸
        self.save_members()
        self.load_members()
        print("회원가입완료.")


    def member_login(self):
        print("\n[로그인]")
        uid = input("아이디 : ")
        pw = input("비밀번호 : ")

        member = self.find_member(uid)

        if not member:
            print("존재하지 않는 아이디")
            return
        if not member.active:
            print("계정 비활성화")
            return
        if member.pw == pw:
            self.session = member
            print(f"{member.name}님 로그인 ({member.role})")

            if member.role == "admin":
                self.member_admin() # 관리자용 메서드로 들어감
        else:
            print("비밀번호 오류")



    def member_logout(self):
        pass

    def member_modify(self):
        pass

    def member_delete(self):
        pass

    # 파일 저장용 코드
    def save_members(self):
        with open(self.file_name,"w",encoding="utf-8") as f:
            for member in self.members:
                f.write(member.to_line())
                #       Member 객체의 메서드를 사용하여 한줄 씩 기록함


    # id를 이용해 members에서 찾는 공통 메서드
    def find_member(self, uid):
        for member in self.members: # members 리스트에서 한개씩 member 객체를 가져와서
            if member.id == uid:    # 가져온 member객체.id와 전달받은 id가 같은지
                print(member.name,"님을 찾았습니다")
                # 이전에는 member[2] 이런식으로 찾았는데 이렇게하면 간편하게 할수있음
                return member       # 같은게 있으면 member객체를 리턴
        return None                 # 없으면 None로 리턴해라 라는뜻

    def member_admin(self):
        # role 가 admin 일경우만 진입가능한 메서드
        subrun = True
        while subrun:
            print("\n[관리자 메뉴]")
            print("1. 회원 리스트 조회")
            print("2. 비밀번호 변경")
            print("3. 블랙리스트 처리")
            print("4. 권한 변경")
            print("9. 종료")

            sel = input("선택 : ")


            # 회원 목록 보기
            if sel == "1":
                self.show_member_list()
            # 비밀번호 변경
            elif sel == "2":
                uid = input("대상 아이디 : ")
                member = self.find_member(uid)
                if member:
                    member.pw = input("새 비밀번호 : ")
                    self.save_members()
                    print("비밀번호 변경 완료")

                else:
                    print("회원 없음")

            elif sel == "3":
                uid = input("대상 아이디 : ")
                member = self.find_member(uid)
                self.save_members()
                if member:
                    member.role = input("admin / user : ")
                    self.save_members()
                    print("블랙리스트 처리 완료")
                else:
                    print("회원 없음")

            elif sel == "4":
                uid = input("대상 아이디 : ")
                member = self.find_member(uid)
                if member:
                    member.role = input("admin / user : ")
                    self.save_members()
                    print("권한 변경 완료")
                else:
                    print("회원 없음")

            elif sel == "9":
                subrun = False

            else:
                print("잘못된 입력입니다.")
                return


    def show_member_list(self):
        # 관리자가 볼수 있는 회원 리스트
        print("\n[회원목록]")
        print("-"*60)
        print(f"{'ID':10} {'이름':10} {'권한':10} {'상태':10}")
        print("-"*60)

        for member in self.members:
        # members 리스트에 있는 객체를 하나씩 가져와 member에 넣음
            status = "활성" if member.active else "비활성"
            #member.active == True면 status변수에 "활성"을 넣고 아니면 "비활성" 이라고 표시됨
            print(f"{member.id:10} {member.name:10} {member.role:10} {status}")
        #                                                              "활성"이나"비활성"으로 들어감
        print("-"*60)




























