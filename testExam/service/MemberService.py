import os

from testExam.common.Session import Session
from testExam.domain import Member

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
        with open(FILE_PATH,"r",encoding="utf-8") as f:
            for line in f:
                cls.members.append(Member.from_line(line))

    @classmethod
    def save(cls):
        with open(FILE_PATH,"w",encoding="utf-8") as f:
            for m in cls.members:
                f.write(m.to_line()+"\n")

    @classmethod
    def login(cls):
        if Session.is_login():
            print("이미 로그인한 상태입니다.")
            return

        print("\n[로그인]")

        user_id = input("아이디 : ")
        user_pw = input("비밀번호 : ")
        for m in cls.members:
            if m.user_id == user_id:
                if not m.active:
                    print("비활성화된 계정입니다.")
                    return
                if m.user_pw == user_pw:
                    Session.login(m)
                    print(f"{m.user_name}님 로그인 되었습니다.\n권한({m.role})")
                    print(m)
                    return
                else:
                    print("비밀번호가 틀렸습니다.")
                    return
        print("없는 계정입니다.")

    @classmethod
    def logout(cls):
        if not Session.is_login():
            print("로그인 상태가 아닙니다.")
            return
        Session.logout()
        print("로그아웃 완료")

    @classmethod
    def signup(cls):
        if Session.is_login():
            print("로그아웃 후 이용가능합니다.")
            return


        print("\n[회원가입]")
        user_id = input("아이디 : ")
        if any(m.user_id == user_id for m in cls.members):
            print("중복된 아이디입니다.")
            return

        user_pw = input("비밀번호 : ")
        user_name = input("이름 : ")
        member = Member(user_id, user_pw, user_name)
        cls.members.append(member)
        cls.save()

        print(f"{member.user_id}님 회원가입을 환영합니다.")

    @classmethod
    def modify(cls):
        if not Session.is_login():
            print("로그인 상태가 아닙니다.")
            return

        member = Session.login_member

        print("""
        [정보수정]
        1. 이름 변경
        2. 비밀번호 변경
        9. 뒤로가기
        """)

        sel = input("선택 : ")

        if sel == "1":
            member.user_name = input("새 이름 : ")
        elif sel == "2":
            member.user_pw = input("새 비밀번호 : ")
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
            print("로그인 상태가 아닙니다.")
            return
        member = Session.login_member
        print("""
        [회원탈퇴]
        1. 회원 탈퇴하기
        2. 계정 비활성화
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
            print("잘못된 입력입니다.")

    @classmethod
    def admin_menu(cls):
        if not Session.is_login() or not Session.login_member.is_admin():
            print("관리자만 접근 가능합니다.")
            return

        while True:
            print("""
            [관리자메뉴]
            1. 회원 목록 조회
            2. 권한 변경
            3. 블랙리스트 등록
            4. 블랙리스트 해제
            9. 뒤로가기
            """)

            sel = input("선택 : ")
            if sel == "1":
                cls.list_member()
            elif sel == "2":
                cls.change_role()
            elif sel == "3":
                cls.black_member()
            elif sel == "4":
                cls.unblack_member()
            elif sel == "9":
                break

    @classmethod
    def list_member(cls):
        print("[회원 목록]")
        for m in cls.members:
            print(m)

    @classmethod
    def change_role(cls):
        user_id = input("대상 아이디 : ")
        for m in cls.members:
            if m.user_id == user_id:
                m.role = input("admin / user : ")
                cls.save()
                return
        print("회원 없음")

    @classmethod
    def black_member(cls):
        user_id = input("대상 아이디 : ")
        for m in cls.members:
            if m.user_id == user_id:
                if not m.active:
                    print("이미 비활성화된 계정입니다.")
                    return

                m.active = False
                cls.save()
                print("블랙리스트 처리완료")
                return
        print("회원 없음")

    @classmethod
    def unblack_member(cls):
        user_id = input("대상 아이디 : ")
        for m in cls.members:
            if m.user_id == user_id:
                if m.active:
                    print("이미 활성화된 계정입니다.")
                    return



                m.active = True
                cls.save()
                print("블랙리스트 해제완료")
                return

        print("회원 없음")


