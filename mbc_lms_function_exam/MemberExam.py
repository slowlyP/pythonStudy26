# 회원관리 crud를 함수로 만들기
# C : 회원가입
# R : 회원의리스트 관리자인경우 회원암호 변경 or 블랙리스트 등록 , 권한 부여
# r : 로그인 id와 pw를 활용하여 로그인 상태 유지 session
# U : 회원정보 수정
# D : 회원탈퇴 or 회원 비활성화

# 프로그램에서 사용될 변수들
# 전역변수 (global) -> 파일 안에서 전체적으로 사용되는 변수
run = True # while 에서 전체적으로 사용되는 변수( 프로그램 구동 )
session = None # login 상태 저장용 -> login 한 user의 list index 기억용

# 지역변수 (local) -> while, if, for, def 안에서 사용되는 변수

# 프로그램에서 사용될 리스트 들 ( 더미 데이터 )
# sns = [1,2,3] # 회원 번호 들 회원삭제및 추가시 번호가 흔들릴수 있음(인덱스로만 사용해보기)
ids = ["kkw","lhj","ljj"] # 로그인 아이디 들
pws = ["1234", "5678","8888"] # 암호 들
names = ["김기원","임효정","이재정"] # 사용자 명
roles = ["admin","manager","user"] # 사용자 권한(admin, manager, user)
active = [True,True,True] # 회원사용중,탈퇴,중지,블랙리스트 등
com_pw = ["1111"] # 권한 설정시 필요암호
nick_names = []
# 차후에는 파일처리로 변환 할 예정

# 프로그램에서 사용될 함수들


# 회원 가입용 함수
def member_add ():
    print("member_add 함수로 진입합니다.")
    new_id = input("아이디 :  ") # 키보드로 아이디를 넣음

    if new_id in ids: # ids ids 리스트에서 찾아 중복되는지 확인
        # True 일때(이미 존재할경우)
        print("이미 존재하는 아이디 입니다.")
        return # if 문 종료

    else:
        new_pw = input("암호 : ")
        new_name = input("이름 : ")
        new_nick_name = input("닉네임 : ")
        member_add_menu() # 회원 권한 메뉴 출력
        role_set = input("권한 선택 : ")
        if role_set == "1":
            new_role = "admin"
        elif role_set == "2":
            new_role = "manager"
        else:
            new_role = "user"

        print(f"""
입력된 정보를 확인하세요.
이름 :  {new_name}  암호 : {new_pw}    닉네임 : {new_nick_name}
아이디 :  {new_id}  권한 : {new_role}""")

        save_select = input("저장  'y' : ")
        if save_select == "y":
            print("저장 시작")
            ids.append(new_id)
            pws.append(new_pw)
            names.append(new_name)
            nick_names.append(new_nick_name)
            roles.append(new_role)

            active.append(True) # 인덱스에 업데이트 되는 코드 입력 완료
            print("저장 완료")

            # 여기에 로그인 함수를 추가해도됨
        else :
            print("회원 가입에 실패하셧습니다.")
            print("다시 진행 하세요.")





    print("member_add  함수를 종료합니다.")


# 가입된 회원을 확인하여 로인 처리후 session 변수에 인덱스를 넣는다.
def member_login ():
    print("member_login 함수로 진입합니다.")

    global session # 맨위에 전역변수로 지정한 내용 활용

    if session is not None: # session 에 이미 값이 있으면 이라는 의미
    # if session != None -> 숫자 처리할때 사용


        # True 상태
        print(" 이미 로그인한 상태입니다.")
        print(f" 로그인한 사용자는 {names[session]}님 입니다.")
        return # 되돌아가는 역활.
    else:
        # False
        user_id = input("아이디 :  ")
        user_pw = input("암호 : ")
        if user_id in ids : # 키보드로 받은 id 값이 ids에 있는지 확인
            # 있으면 True
            idx = ids.index(user_id)
            if not active [idx] : # 회원 활성화 상태인지 확인 하는용도
                # False 일때
                print("비활성화/차단된 계정입니다.")
                return
        else:
            # True 일때 # 암호를 비교한다.
            if user_pw == pws[idx] : # 키보드로 넣은 암호와 리스트의 주소 암호 일치 인지 확인
                session = idx # 로그인 상태로 완성
                # 글로벌 영역에 세션값이 있는 상태가 됨.
                print(f"{names[session]}님 환영합니다.")
                print(f"{roles[idx]} 권한을 가지고있습니다.")
            else:
                print("비밀번호가 다릅니다.")


    print("member_login 함수를 종료합니다.")



# 관리자가 로그인했을경우 할수있는 기능
def member_admin():
    print("member_admin 함수로 진입합니다.")
    # 다른 사용자 암호 변경 코드 입력

    # 블랙리스트로 변환 > active를 False 처리

    # 권한 부여 -> 사용자의 권한을 변경 roles를 변경(manage 에서 user로 변경하던 user 에서 manage로 변경)





    print("member_admin 함수를 종료합니다.")




# 회원 로그아웃으로 상태 전환 -> session 값을 None 으로 변경
# 로그인 상태인지를 확인하고 session 을 None 으로 바꿔주면된다고함
def member_logout():
    print("member_logout 함수로 진입합니다.")




    print("member_logout 함수를 종료합니다.")



# 회원 정보 수정 함수
# 로그인 상태인지를 확인하고 자신의 정보를 확인하여 수정한다.
def member_modify():
    print("member_modify 함수로 진입합니다.")



    print("member_modify 함수를 종료합니다.")


# 회원 탈퇴 또는 회원 유휴등 처리
# 로그인 상태인지를 확인해야함
# 탈퇴는 pop, 유휴는 (휴직상태) active=False 처리? 하라고함)
def member_delete():
    print("member_delete 함수로 진입합니다")



    print("member_delete 함수를 종료합니다.")

# ================기능에 대한 함수 생성====================

def main_menu():
    print(f"""
    mbc 아카데미 회원 관리 프로그램입니다.
    
    1. 회원가입     2. 로그인      3. 로그아웃
    4. 회원정보수정       5. 회원탈퇴
    9. 프로그램종료
    """)

# 메인메뉴 함수 종료


def member_add_menu(): # 회원가입에서 사용할 메뉴
    print(f"""
    회원 권한을 확인하세요.
    
    1. 관리자      2. 매니저       3. 일반사용자

    """)

# 메뉴 함수 끝

# 프로그램 시작

while run:  # 메인 프로그램 실행코드
    main_menu() # 위에서 만든 메인메뉴를 실행
    select = input(">>>") # 키보드로 메뉴선택
    if select == "1": # 회원가입 코드
        member_add() # 회원가입용 함수 호출



    elif select == "2": # 로그인 메뉴 선택
        member_login() # 로그인용 함수 호출

    elif select == "3": # 로그아웃 메뉴 선택
        member_logout() # 로그아웃용 함수 호출

    elif select == "4": # 회원 정보 수정 선택
        member_modify() # 회원 정보 수정 함수 호출

    elif select == "5": # 회원 탈퇴 선택
        member_delete() # 회원 정보 삭제 함수 호출

    elif select == "9": #프로그램 종료 선택
        run = False

# while 문 종료



















