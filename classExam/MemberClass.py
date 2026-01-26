import os

# 함수는 뒤에 self 가 안들어감
# 메서는 뒤에 self 가 들어감 구분해야함

class MemberManager: # 객체를 담당하는 클래스 사용법은 변수 = MemberManager() 생성
    # 클래스에서 self 는 객체의 주소를 가지고 있음
    # def __init__ 클래스 구현시 필수요소
    def __init__(self, file_name="members.txt"): # 객체 생성시 만드는 기본값을 가지고있는 "생성자"
        self.file_name = file_name # 객체에 파일 이름을 넣는다. file_name(members.txt)
        self.members = []          # 객체에 members 리스트를 만든다
        self.load_member()         # 객체에 세션 변수를 만들고 기본값으로 None 처리(정수)
        self.session = None        # 아래에 선언된 load_members() 메서드를 호출한다.

    #=============================================
    #파일 로드
    #=============================================

    def load_member(self):         # 앞으로 만들 메서드는 ()괄호안에 self 가 필수
        self.members = []          # 빈 배열로 생성 (이전에 리스트가 남아있을수가있음)

        if not os.path.exists(self.file_name): # 동일 디렉토리에 파일명이 없으면
            self.save_member()                 # save_members() 메서드를 호출(open()으로 파일생성)
            return                             # load_member() 메서드를 빠져나와라 라는뜻

        with open(self.file_name, "r", encoding="utf-8") as f:
            #        members.txt  읽기전용          한글처리필수      를 f라는 변수에 넣어라 라는 뜻
            for line in f: # f 변수에 있는 파일 객체를 줄 단위로 "반복"하려고 for를 사용
                data = line.strip().split("|") # 한 줄 읽은 값을 split("|")엔터 제거 |를 기준으로 자른다. ->1차원리스트로생성

                if len(data) == 5:
                    data.append(0) #kor
                    data.append(0) #eng
                    data.append(0) #math

                data[4] = True if data[4] =="True" else False
                # 리스트 5번째 값이 문자열 True 이면 불타입 True 로 변경 아니면 False
                data[5] = int(data[5])
                data[6] = int(data[6])
                data[7] = int(data[7])
                self.members.append(data)
                # 2차원 배열로 만든 members 맨뒤에 추가 해라 for 종료 할때 까지

    #============================
    # 파일 저장
    #============================
    def save_member(self):  # members 2차원 리스트 값을 파일로 덮어쓰기 해라
        # 파일 처리는 수정을 하지않는다. r (읽기전용), w (덮어쓰기), a (마지막에 추가용)
        with open(self.file_name, "w", encoding="utf-8") as f:
            #      members.txt    덮어쓰기       한글처리  를 f라는 변수에 넣어라

            for m in self.members: # 메모리에 있는 members 2차원 리스트를 한 줄씩 가져와서 m 변수에 넣어라
                f.write(f"{m[0]}|{m[1]}|{m[2]}|{m[3]}|{m[4]}|{m[5]}|{m[6]}|{m[7]}\n")
                #    m =  [uid,   pw,   name,   role,  True    국어    영어   수학  줄바꿈 ])
                #           asdf|asdf|321|admin|True|70|80|80  < 이런식으로 txt에 저장됨 -> write 저장
                #                                                                     -> for문 끝날때 까지

    #============================
    # 회원 가입
    #============================
    def member_add(self):# self 는 클래스의 객체 주소
        print("\n[회원가입]")
        uid = input("아이디 : ") # 키보드로 입력한 값을 uid 변수에 넣음

        for m in self.members: # 2차원 배열인 members에 1차원 리스트를 in = 1줄 씩
            if m[0] == uid:
                print(" 이미 존재하는 아이디 입니다.")
                return # member_add() 메서드를 빠져나와라

        # 중복된 아이디가 없으면 아래쪽 코드가 실행됨 -> else : 로 처리해도되지만 -> 들여쓰기가 필요해짐
        pw = input("비밀번호 : ")
        name = input("이름 : ")

        print("1.admin 2. manager 3.user")
        r = input("권한 선택 : ")

        role = "user"
        if r == "1":
            role = "admin"
        elif r == "2":
            role = "manager"
        # 여기까지가 변수에 입력완료
        self.members.append([uid, pw, name, role, True, 0, 0, 0])
        # 메모리에 있는 2차원 리스트 members 뒤에 추가 .append()
        self.save_member()         # 파일로 저장
        self.load_member()         # 파일 변경사항 불러오기

        print("회원가입 완료")

    #==========================
    #로그인
    #==========================
    def member_login(self):
        print("\n[로그인]")
        uid = input("아이디 : ")
        pw = input("비밀번호 : ")

        # enumerate() -> 2차원 배열 인덱스와 리스트를 추출한다.
        for i, m in enumerate(self.members):
        #   i=index m=members
            if m[0] == uid:
                if not m[4]: # for  문 중에 같은 아이디가 있으면
                             # active 가 false인지 확인
                    print("비활성화된 계정입니다.")
                    return  # member_login() 메서드를 빠져나온다.
                # active가 true 이면
                if m[1] == pw: #member[]
                    self.session = i # session 변수에 인덱스를 넣는다.(회원주소)
                    print(f"{m[2]}님 로그인 성공 ({m[3]})")

                    if m[3] == "admin": # 관리자 이면
                        self.member_admin() # 관리자 메서드를 호출한다 (관리자 메뉴)
                    return
                else: # if m[1] == pw: 결과가 false이면
                    print("비밀번호 오류")
                    return # member_login()메서드를 빠져나온다.

        print("존재하지 않는 아이디") # for문에 return이 안걸리면 여기까지 옴

    #===================================
    #관리자 기능
    #===================================
    def member_admin(self): # 로그인시 admin = role 이면 진입
        print("\n[관리자 메뉴")
        print("1. 비밀번호 변경")
        print("2. 블랙리스트")
        print("3. 권한 변경")
        print("0. 종료")

        sel = input("선택 : ") # 관리자 메뉴 선택용
        if sel =="0":
            return
        uid = input("대상 아이디 : ") # 대상 id 찾는 역활

        for m in self.members: # members에 2차원 배열을 반복
            if m[0] == uid:    # 대상 id를 찾으면
                if sel == "1": # 비밀번호 변경
                    m[1] = input("새 비밀번호 : ")
                elif sel == "2":# 블랙리스트 처리
                    m[4] = False
                elif sel == "3":# 권한 변경 입력
                    m[3] = input("admin / manager / user : ")

                self.save_member() # 파일로 저장
                self.load_member()
                print("관리자 작업 완료")
                return

        print("대상 회원 없음")

    #=================================
    #로그아웃
    #=================================

    def member_logout(self):
        self.session = None # session 값에 있는 인덱스를 None 처리함
        print("로그아웃 완료")

    #==================================
    #내정보수정
    #==================================

    def member_modify(self):
        if self.session == None: # 현재 session 의 값이 None 면 로그인이 필요하다
            print("로그인 필요")
            return

        print("\n[내 정보 수정]")
        print("1. 이름 변경")
        print("2. 비밀번호 변경")

        sel = input("선택 : ")

        if sel == "1":
            self.members[self.session][2] = input("새 이름 : ")
            #    2차원 배열 로그인 인덱스 이름필드
        elif sel == "2":
            self.members[self.session][1] = input("새 비밀번호 : ")
            #    2차원 배열 로그인 인덱스  암호필드
        else:
            print("잘못된 입력입니다.")
            return

        self.save_member() # 파일로 저장
        self.load_member()
        print("수정 완료")

    #===================================
    #회원탈퇴
    #===================================

    def member_delete(self):
        if self.session is None:
            print("로그인 필요")
            return

        print("\n[회원 탈퇴]")
        print("1. 완전 탈퇴")
        print("2. 계정 비활성화")

        sel = input("선택 : ")

        if sel == "1":
            self.members.pop(self.session)
        elif sel == "2":
            self.members[self.session][4] = False

        self.session = None
        self.save_member()
        self.load_member()
        print("처리 완료")


    #===============================================
    #성적 입력
    #===============================================

    def score_add(self):
        if self.session == None:
            print("로그인 필요")
            return

        role = self.members[self.session][3]
        if role not in ["admin", "manager"]:
            print("권한이 없습니다.")
            return

        uid = input(" 성적 입력할 아이디 : ")

        for m in self.members:
            if m[0] == uid:
                try:
                    m[5] = int(input("국어 점수 : "))
                    m[6] = int(input("영어 점수 : "))
                    m[7] = int(input("수학 점수 : "))
                except:
                    print("숫자만 입력하세요.")
                    return

                self.save_member()
                print("성적 입력 완료")
                return
        print("해당 회원 없음")

    #===============================================
    #전체성적조회
    #===============================================
    def score_read_all(self):
        if self.session == None:
            print("로그인 필요")
            return

        role = self.members[self.session][3]
        if role not in ["admin", "manager"]:
            return

        print("\n[전체 성적 조회]")

        print("이름 | 국어 | 영어 | 수학| 총점 | 평균")
        print("=" * 40)

        for m in self.members:
            if not m[4]: # 비활성화 계정 제외
                continue
            if m[3] == "admin":
                continue
            kor = m[5]
            eng = m[6]
            math = m[7]
            total = kor + eng + math
            avg = total / 3

            print(f"{m[2]}님의 성적 | {kor} | {eng} | {math} | {total} | {avg} 입니다.")

    #======================================================
    #개인성적조회
    #======================================================
    def score_read_my(self):
        if self.session == None:
            print("로그인 필요")
            return

        m = self.members[self.session]

        if not m[4]:
            print("비활성화된 계정입니다.")
            return



        kor = m[5]
        eng = m[6]
        math = m[7]
        total = kor + eng + math
        avg = total / 3

        print("\n[내 성적 조회]")
        print("이름 | 국어 | 영어 | 수학 | 총점 | 평균 ")
        print(f"{m[2]} | {kor} | {eng} | {math} | {total} | {avg:.1f}")







    def menu_score(self): # 6번 메서드
        if self.session is None:
            print("로그인 필요")
            return

        role = self.members[self.session][3]

        if role == "admin":
            self.score_add()

        else:
            self.score_read_my()

    def menu_score_admin(self):
        if self.session is None:
            print("로그인 필요")
            return

        role = self.members[self.session][3]
        if role !="admin":
            print("권한이 없습니다.")
            return
        self.score_read_all()


    def score_update(self):
        if self.session is None:
            print("로그인 필요")
            return

        role = self.members[self.session][3]
        if role not in ["admin", "manager"]:
            print("권한이 없습니다.")
            return

        uid = input("성적 수정할 아이디 : ")


        for m in self.members:
            if m[0] == uid:
                if m[3] =="admin":
                    print("관리자의 성적은 수정할수없습니다.")
                    return


                print(f"현재 성적 -> 국어 : {m[5]} 영어 : {m[6]} 수학 : {m[7]}")

                try:
                    new_kor = int(input("새 국어 점수 : "))
                    new_eng = int(input("새 영어 점수 : "))
                    new_math = int(input("새 수학 점수 : "))
                except:
                    print("숫자만 입력하세요.")
                    return

                m[5] = new_kor
                m[6] = new_eng
                m[7] = new_math


                self.save_member()
                print("성적 수정 완료")
                return
    print("해당 회원 없음.")










    #====================================
    #메뉴
    #====================================
    def main_menu(self):
        print("""
===회원관리 프로그램(Class 기반)===
1. 회원가입 
2. 로그인
3. 로그아웃
4. 회원정보수정
5. 회원탈퇴
9. 종료
""")
        if self.session is not None:
            role = self.members[self.session][3]

            if role =="admin":
                print("6. 성적입력 (admin)")
                print("7. 전체성적조회 (admin)")
                print("8. 성적수정 (admin)")
            else:
                print("6. 내 성적 조회 ")


    #====================================
    #실행
    #====================================
    def run(self):
        while True:
            self.main_menu()

            sel = input(">>>")

            if sel == "1": self.member_add()
            elif sel == "2": self.member_login()
            elif sel == "3": self.member_logout()
            elif sel == "4": self.member_modify()
            elif sel == "5": self.member_delete()
            elif sel == "6": self.menu_score()
            elif sel == "7": self.menu_score_admin()
            elif sel == "8": self.score_update()


            elif sel == "9": break

#========================================
#프로그램 시작
#========================================
                      # ★★★★★★★★★가장 중요한 포인트 ★★★★★★★★★★
app = MemberManager() # 지금까지 만든 클래스를 객체로 만들고 실행
app.run()             # 객체에 있는 .run() 메서드를 실행한다.



























