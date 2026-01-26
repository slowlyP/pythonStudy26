# 회원관리 프로그램 만들기

# C 회원가입
# R 회원의 리스트에서 관리자인 경우 회원 암호 변경 or 블랙리스트 등록 or 권한 부여
# r 로그인 id 와 pw 를 활용 하여 로그인 상태 유지 session
# U 회원 정보 수정
# D 회원 탈퇴 or 회원 비활성화

# 프로그램에서 사용될 변수들
# 전역변수 (global) -> 파일 안에서 사용되는 변수

import os
run = True
session = None
FILE_NAME = "members.txt"
LOGIN_LOG_FILE = "login_log.txt"
members = []
# 지역변수 (local) -> while,if,for,def 안에서 사용되는 변수

# 프로그램에서 사용될 리스트( 더미 데이터)


admin_pw = ["1004"] # 관리자 로그인시 사용되는 비밀번호


def show_member(member):
    result = []

    for value in member:
        if value != "":
            result.append(value)

    return result






def write_login_log(new_name,action):
    from datetime import datetime
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOGIN_LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{new_name}|{action}|{now}\n")






def save_members() :

    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for member in members:
            line = (f"{member[0]}|{member[1]}|{member[2]}|{member[3]}|{member[4]}|"
                    f"{member[5]}|{member[6]}\n")

            f.write(line)

def load_members():
    members.clear()

    if not os.path.exists(FILE_NAME):
        save_members()
        return

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        for line in f:
            data = line.strip().split("|")

            if len(data) > 4:
                data[4] = True if data[4] == "True" else False

            while len(data) <7:
                data.append("")

            members.append(data)








# 관리자용 함수
#def admin ():
    #print("admin 함수로 진입합니다.")

def member_add_menu():
    print(f"""
회원 권한 선택

1. admin      2. user

""")
def member_admin ():
    print("관리자 페이지")






# 회원 가입용 함수
def member_add ():
    global session

    if session is not None:
        print("로그아웃 후 회원가입이 가능합니다.")
        return

    print("member_add 함수로 진입합니다.")
    new_id = input("아이디 : ") # 키보드로 아이디 입력

    for member in members:
        if member[0] == new_id:
            print("중복된 아이디입니다.")
            return


    new_nick_name = input("닉네임 : ")
    new_pw = input("암호 : ")
    new_name = input("이름 : ")
    member_add_menu()
    role_set = input(">>>")
    if role_set == "1":
        admin_key = input("admin pw: ")
        if admin_key != admin_pw[0]:
            print("admin 인증 실패")
            return
        new_role = "admin"
    else:
        new_role = "user"








    print(f"""
입력된 정보를 확인하세요.
이름 : {new_name} 닉네임 : {new_nick_name}
아이디 : {new_id} 권한 : {new_role}""")

    save_select = input("저장 'y' :")
    if save_select == "y":
        print("저장 시작")
        members.append([new_id,new_pw, new_nick_name, new_role, True,"",""])
        save_members()
        print("저장 완료")
    else:
        print("회원 가입에 실패하셧습니다.")
        print("다시 진행 하세요")




def member_login (): # 로그인용 함수
    #print("member_login 함수로 진입합니다.")

    global session

    if session is not None:

        print(" 이미 로그인한 상태입니다.")
        print(f" 로그인한 사용자는 {members[session][2]}님 입니다.")
        return
    user_id = input("아이디 : ")
    user_pw = input("암호 : ")

    for idx,member in enumerate(members):

        if session is not None and members[session][3] == "ademin":
            print("idx :",idx)
            print("member : ",show_member(member))


        if member[0] == user_id:

            if not member[4] :
                print("로그인 할 수 없는 계정입니다.")
                return

            if member[1] == user_pw:
                session = idx

                clean_member = show_member(member)


                print(f"{clean_member[2]}님 로그인 되셧습니다.")
                print(f"{clean_member[3]}권한 입니다.")
                write_login_log(member[0],"LOG_IN")

                if clean_member[3] =="admin":
                    member_admin()
                return

            else:
                print("비밀번호가 다릅니다.")
                print("다시 시도해 주세요")
                return













def member_update ():
    print("member_update 함수로 진입합니다.")
    global session

    print("전체 회원 리스트")













def member_logout (): # 로그아웃용 함수
    print("member_logout 함수로 진입합니다")
    global session

    if session is None:
        print("로그인 상태가아닙니다.")
        return

    write_login_log(members[session][0],"LOG_OUT")

    print(f"{members[session][2]}, 님 로그아웃 되셧습니다")
    session = None







def member_modify (): # 회원 정보 수정함수
    global session
    if session is None:
        print("로그인후 이용가능합니다.")
        return

    member = members[session]
    new_nick = input(" 새 닉네임 입력 (변경 안하려면 Enter):")
    if new_nick != "":
        member[2] = new_nick

    user_pw = input("새 암호 입력 (변경 안하려면 Enter):")
    if user_pw != "":
        member[1] = user_pw

    save_members()
    print("회원정보가 수정되었습니다.")







def member_delete (): # 회원 정보 삭제 or 계정 처리
    global session

    if session is None:
        print("로그인후 이용가능합니다.")
        return

    confirm = input(f"{members[session][2]}님의 계정을 정말 삭제하시겠습니까? (y/n) : ")
    if confirm.lower() == "y":
        removed = members.pop(session)
        print(f"{removed[2]}님의 계정이 삭제처리 되었습니다.")
        save_members()
        session = None

    else:
        print("삭제가 취소되었습니다.")
















def main_menu(): # 메인메뉴용 함수



    print(f"""
mbc 아카데미 회원 관리 프로그램

1. 회원가입     2. 로그인      3.로그아웃
4. 회원정보수정   5. 회원탈퇴
9. 프로그램종료
""")
    if session is not None and members[session][3] == "admin":
        print("6. 회원 관리(admin only)")





# 메인메뉴 함수끝
load_members()
# 프로그램 시작
while run: # 메인 프로그램 실행코드
    main_menu() # 메인메뉴 호출 함수
    select = input(">>>") # 키보드 메뉴선택
    if select == "1":
        member_add() # 회원가입용 함수 호출


    elif select == "2":
        member_login()

    elif select == "3":
        member_logout()

    elif select == "4":
        member_modify()

    elif select == "5":
        member_delete()

    elif select == "6":
        print("")
    elif select == "9":
        run = False
        print("프로그램을 종료합니다.")

