

import os

from datetime import datetime
from Member import Member



class MemberClass:
    def __init__(self,file_name="members.txt"):
        self.file_name = file_name
        self.members = []
        self.log_file = "member_log.txt"
        self.session = None
        self.load_members()

    def write_log(self, action, user_id):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(f"{now}\t{action}\t{user_id}\n")

    def run(self):
        run = True
        while run:
            self.main_menu()
            sel = input(">>>")
            
            if sel == "1": self.member_add()
            elif sel == "2": self.member_login()
            elif sel == "3": self.member_logout()
            elif sel == "4": self.member_modify()
            elif sel == "5": self.member_delete()
            elif sel == "9": run = False
            else:
                print("잘못된 접근입니다.")


    def load_members(self):
        if not os.path.exists(self.file_name):
            self.save_members()
            return
        self.members = []
        with open(self.file_name, "r", encoding="utf-8") as f:
            for line in f:
                member = Member.from_line(line)
                if member:
                    self.members.append(member)

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
        if self.session:
            print("로그아웃 후 회원가입이 가능합니다.")
            return

        print("\n[회원가입]")
        user_id = input("아이디 : ")
        
        if self.find_member(user_id):
            print("아이디가 중복됩니다.")
            return
        user_pw = input("비밀번호 : ")
        user_name = input("이름 : ")
        user_role = "user"
        
        self.members.append(Member(user_id, user_pw, user_name, user_role))
        self.save_members()
        self.load_members()
        print("회원가입완료.")
        
        
    def member_login(self):
        if self.session:
            print(f"{self.session.user_id}님이 이미 로그인 되어있습니다.")
            return

        print("\n[로그인]")
        user_id = input("아이디 : ")
        user_pw = input("비밀번호 : ")
        
        member = self.find_member(user_id)
        
        if not member:
            print("존재하지 않는 아이디")
            return
        if not member.active:
            print("계정 비활성화")
            return
        if member.user_pw == user_pw:
            self.session = member
            print(f"{member.user_name}님 로그인 ({member.user_role})")
            self.write_log("LOGIN",member.user_id)
            
            if member.user_role == "admin":
                self.member_admin()
        else:
            print("잘못된 접근입니다.")

    def member_logout(self):

        if not self.session:
            print("로그인 상태가 아닙니다.")
            return
        print(f"{self.session.user_id}님 로그아웃 되었습니다.")
        self.write_log("LOGOUT",self.session.user_id)
        self.session = None


    def member_modify(self):

        if not self.session:
            print("로그인 상태가 아닙니다.")
            return
        while True:
            print("\n[회원정보수정]")
            print("1. 비밀번호 변경")
            print("2. 이름 변경")
            print("9. 돌아가기")

            sel = input(">>>")

            if sel =="1":
                new_pw = input("새 비밀번호 : ")
                self.session.user_pw = new_pw
                self.save_members()
                self.write_log("MODIFY",self.session.user_id)
                print("비밀번호가 변경되었습니다.")

            elif sel =="2":
                new_name = input("새 이름 : ")
                self.session.user_name = new_name
                self.save_members()
                self.write_log("MODIFY",self.session.user_id)
                print("이름이 변경되었습니다.")

            elif sel =="9":
                break

            else:
                print("잘못된 입력입니다.")


    def member_delete(self):
        pass

    def save_members(self):
        with open(self.file_name, "w", encoding="utf-8") as f:
            for member in self.members:
                f.write(member.to_line())

    def find_member(self, user_id):
        for member in self.members:
            if member.user_id == user_id:
                return member
        return None

    def member_admin(self):
        subrun = True
        while subrun:
            print("\n[관리자 메뉴]")
            print("1. 회원 리스트 조회")
            print("2. 비밀번호 변경")
            print("3. 블랙리스트 처리")
            print("4. 권한 변경")
            print("9. 종료")

            sel = input("선택 : ")
            if sel == "1":
                self.show_member_list()

            elif sel == "2":
                user_id = input("대상 아이디 : ")
                member = self.find_member(user_id)
                if member:
                    member.user_pw = input("새 비밀번호 : ")
                    self.save_members()
                    print("비밀번호 변경 완료")

                else:
                    print("회원 없음")

            elif sel == "3":
                user_id = input("대상 아이디 : ")
                member = self.find_member(user_id)

                if member:
                    member.active = False
                    self.save_members()
                    self.write_log("BLACKLIST",member.user_id)
                    print("블랙리스트 처리완료(계정 비활성화)")
                else:
                    print("회원 없음")

            elif sel == "4":
                user_id = input("대상 아이디 : ")
                member = self.find_member(user_id)
                if member:
                    member.user_role = input("admin / user : ")
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
        print("\n[회원목록]")
        print("-"*60)
        print(f"{'ID':10} {'이름':10}{'권한':10}{'상태':10}")
        print("-"*60)
        for member in self.members:
            status = "활성" if member.active else "비활성"
            print(f"{member.user_id:10} {member.user_name:10} {member.user_role:10} {status}")
        print("-"*60)