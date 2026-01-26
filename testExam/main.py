
from testExam.common.Session import Session
from testExam.service import *

def main():
    MemberService.load()

    run = True
    while run:
        print("""
        =======================
        엠비씨 아카데미 관리 시스템
        1. 회원가입
        2. 로그인
        3. 로그아웃
        4. 정보변경
        5. 회원관리(관리자)
        6. 회원탈퇴
        7. 게시판
        9. 종료
        =======================
        """)
        member = Session.login_member
        if member:
            print(f"{member.user_name}님 환영합니다.")

        sel = input(">>>")
        if sel == "1": MemberService.signup()

        elif sel == "2": MemberService.login()

        elif sel == "3": MemberService.logout()

        elif sel == "4": MemberService.modify()

        elif sel == "5": MemberService.admin_menu()

        elif sel == "6": MemberService.delete()

        elif sel == "7": BoardService.run()

        elif sel == "9":
            print("프로그램 종료")
            run = False

if __name__ == "__main__":
    main()
