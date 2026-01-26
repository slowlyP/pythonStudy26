import os

from packageExam.LMS.common import Session
from packageExam.LMS.domain import *


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR,"..","data","member.txt")

class MemberService:
    members = []

    @classmethod
    def load(cls):
        cls.members = []

        if not os.path.exists(FILE_PATH):
            cls.save()
            return

        with open(FILE_PATH,"r", encoding="utf-8") as f:
            for line in f:
                cls.members.append(Member.from_line(line))



    @classmethod
    def save(cls):
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            for m in cls.members:
                f.write(m.to_line() + "\n")

    @classmethod
    def login(cls):
        print("\n[로그인]")

        uid = input("아이디 : ")
        pw = input("비밀번호 : ")
        for m in cls.members:
            if m.uid == uid:
                if not m.active:
                    print("비활성화된 계정입니다.")
                    return

                if m.pw == pw:
                    Session.login(m)
                    print(f"{m.name}님 로그인 성공 ({m.role})")
                    print(m)
                    return
                else:
                    print("비밀번호가 틀렸습니다.")
                    return
        print("존재하지 않는 아이디입니다.")

    @classmethod
    def logout(cls):
        if not Session.is_login():
            print("로그인 상태가 아닙니다.")
            return

        Session.logout()
        print("로그아웃 완료")

    @classmethod
    def signup(cls):
        print("\n[회원가입]")
        uid = input("아이디 : ")

        if any(m.uid == uid for m in cls.members):
            print("중복된 아이디입니다.")
            return

        pw = input("비밀번호 : ")
        name = input("이름 : ")
        member = Member(uid, pw , name)
        cls.members.append(member)
        cls.save()

        print(f"{member.uid}님 환영합니다. ")

    @classmethod
    def modify(cls):
        if not Session.is_login():
            print("로그인 후 이용 가능합니다.")
            return

        member = Session.login_member

        print("""
        [내 정보 수정]
        1. 이름 변경
        2. 비밀번호 변경
        9. 뒤로가기
        """)

        sel = input("선택 : ")

        if sel == "1":
            member.name = input("새 이름 : ")
        elif sel == "2":
            member.pw = input("새 비밀번호 : ")
        elif sel == "9":
            return

        else:
            print("잘못된 입력입니다.")


        cls.save()
        Session.logout()
        print("정보 수정 완료")
        print("다시 로그인해주세요.")

    @classmethod
    def delete(cls):
        if not Session.is_login():
            print("로그인 후 이용 가능합니다.")
            return

        member = Session.login_member

        print("""
        [회원탈퇴]
        1. 회원 탈퇴하기
        2. 계정 비활성화하기
        9. 뒤로가기        
        """)

        sel = input("선택 : ")
        if sel == "1":
            cls.members.remove(member)
            Session.logout()
            cls.save()
            print("회원 탈퇴 완료")

        elif sel == "2":
            member.active = False
            Session.logout()
            cls.save()
            print("계정 비활성화 완료")
        elif sel == "9":
            return
        else:
            print("잘못된 입력입니다")


    @classmethod
    def admin_menu(cls):
        if not Session.is_login() or not Session.login_member.is_admin():
            print("관리자만 접근 가능합니다.")
            return

        while True:
            print("""
            [관리자 메뉴]
            1. 회원 목록 조회
            2. 권한 변경
            3. 블랙리스트
            9. 뒤로가기
            """)
            sel = input("선택 : ")
            if sel == "1":
                cls.list_member()
            elif sel == "2":
                cls.change_role()
            elif sel == "3":
                cls.black_member()
            elif sel == "9":
                break

    @classmethod
    def list_member(cls):
        print("[회원목록]")
        for m in cls.members:
            print(m)

    @classmethod
    def change_role(cls):
        uid = input("대상 아이디 : ")
        for m in cls.members:
            if m.uid == uid:
                m.role = input("admin / manager / user: ")
                cls.save()
                return
        print("회원 없음")

    @classmethod
    def black_member(cls):
        uid = input("대상 아이디 : ")
        for m in cls.members:
            if m.uid == uid:
                m.active = False
                cls.save()
                print("블랙리스트 처리완료")
                return
        print("회원 없음")



