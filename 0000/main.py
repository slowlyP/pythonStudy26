# 대부분 프로그래밍에서 1번이 되는 또는 start가 되는 파일을 main으로 만듬


# 목표 : mbc 아카데미 LMS 프로그램을 만들어보자
# 회원 관리 : 시스템담당자, 교수 ,행정, 학생, 손님, 학부모 등등...
# 성적 관리 : 교수: 성적등록,수정 등등
#          : 행정담당자가 학기마다 백업(이전->삭제)
#          : 학생은 개인성적 일람,성적 출력 등 가능해야함
#          : 손님은 학교소개페이지 열람
#          : 학부모는 자녀학사관리
#  게시판   : 회원제, 비회원제, 문의사항, Q/A

# 필요한 변수
run = True # 메인 메뉴용 while
#subRun = True # 보조 메뉴용 while
session = None #로그인한 사용자의 인덱스를 기억하는 용

# 필요한 리스트
# 회원에 대한 리스트
sns = [1] # 회원 번호
ids = ["kkw"] # id 에 대한 리스트
pws = ["1234"] # 암호에 대한 리스트
groups = ["admin"] # 회원 등급
admins = [True, False]
# 회원등급이 관리자 = admin ,학생 = stu , 손님 = guest 등등



# 성적에 대한 리스트
pythonScores = []   # 파이썬 점수들
dataBaseScores = []  # 데이터 점수들
wwwScores = []  # 프론트 점수들
totalScores = [] # 총점 들
avgScores = [] # 평균 들
gradeScores = [] # 등급 들
stuIdxs = [] # 학생의 인덱스(학번) <-> 회원의 sns랑 연결?



# 게시판에 대한 리스트
board_no = [] # 게시물의 번호
board_title = [] # 게시물의 제목
board_content = [] # 게시물의 내용
board_writer = [] #게시물 작성자 <-> 회원의 sns랑 연결

# 메뉴 구성
mainMenu = """
================================
mbc 아카데미 LMS에 오신걸 환영합니다.

1. 로그인(회원가입)
2. 성적관리
3. 게시판
4. 관리자 메뉴
9. 프로그램 종료

================================
"""

memberMenu = """
--------------------------------
회원관리 메뉴입니다.

1. 로그인
2. 회원가입
3. 회원수정
4. 회원탈퇴
9. 뒤로가기

--------------------------------
"""

scoreMenu = """
--------------------------------
성적관리 메뉴입니다.

1. 성적입력(교수전용)
2. 성적보기
3. 성적수정(교수전용)
4. 성적백업(행정직원전용)
9. 뒤로가기 

--------------------------------
"""

boardMenu = """
--------------------------------
회원제 게시판 입니다.

1. 자유게시판
2. 건의게시판
3. 학부모게시판
9. 뒤로가기

---------------------------------
"""

# 주 실행문 구현

while run:
    print(mainMenu)
    select = input(">>>") # 사용자가 주메뉴선택 값

    if select == "1":
        print("로그인(회원가입)")

        subRun = True
        while subRun: # 부메뉴 반복용
            print(memberMenu) # 회원관리 메뉴 출력

            subSelect = input(">>>") # 회원 부메뉴 선택

            if subSelect == "1":
                print(" 로그인 ")
                sn = input(" 학번 >>>")
                if sn in sns:
                    print("학번이 없습니다.")
                    continue

                id = input(" 아이디 >>>")
                pw = input(" 비밀번호 >>>")

                if id in ids:
                    idx = ids.index(id)
                    if pws[idx] == pw:
                        session = idx
                        if admins[idx]:
                            print("관리자 계정입니다.")
                        else:
                            print("일반 계정입니다.")
                        print(f"{ids[idx]} 님 로그인 되었습니다.")
                        continue

                    else:
                        print("비밀번호가 틀렸습니다.")

                else:
                    print("아이디가 없습니다..")


            elif subSelect == "2":
                print("회원가입 메뉴")
                sn = input(" 학번 >>>")




                id = input(" 아이디 >>>")

                if id in ids:
                    print("아이디가 중복됩니다.")
                    print("다시 시도해주세요.")
                    continue

                else:
                    print("사용 가능한 아이디입니다.")
                pw = input("비밀번호 >>>")

                if input("y를 누르면 가입됩니다.") == "y":
                    ids.append(id)

                    sn=len(sns) +1
                    sns.append(sn)
                    pws.append(pw)
                    idx = ids.index(id)






                    print(f"{ids[idx]} 님 가입을 환영합니다.")
                    continue
                else:
                    print("회원가입이 취소되었습니다.")


            elif subSelect == "3":
                print("회원수정 메뉴")
                pw = input("비밀번호 >>> ")
                if pw in pws:
                    print("비밀번호가 확인되었습니다.")
                    idx = pws.index(pw)

                    pws[idx] = input("수정할 비밀번호 >>>")



            elif subSelect == "4":
                print("회원 탈퇴 메뉴")
                id = input("회원 탈퇴할 아이디를 입력하세요. >>>")
                if id in ids:
                    idx = ids.index(id)
                    if input(f"{ids[idx]} 님 회원 탈퇴하시려면 비밀번호 를 눌러주세요") == pws[idx]:
                        if pws[idx] in pws:
                            print("비밀번호가 틀렸습니다.")
                            print("다시 입력해주세요.")
                        sns.pop(idx)
                        ids.pop(idx)
                        pws.pop(idx)






                        print("회원 탈퇴가 완료되었습니다.")
                else:
                    print("잘못 입력하셧습니다.")
                    continue





            elif subSelect == "9":
                print("뒤로가기")
                subRun = False # 회원 while 종료
            else:
                print("잘못 입력하셧습니다.")
    elif select == "2":
        print("성적 관리")
        subRun = True
        while subRun:
            print(scoreMenu)

            subSelect = input(">>>")

            if subSelect == "1":

                print("성적입력")

                sn = input("학번 >>>")
                python = int(input("파이썬 점수 >>>"))
                dataBase = int(input("데이터베이스 점수 >>>"))
                www = int(input("프론트 점수 >>>"))
                total = python + dataBase + www






                if input("입력한 정보를 확인하시고 맞으면 y를 눌러주세요") == "y":

                    pythonScores.append(python)
                    dataBaseScores.append(dataBase)
                    wwwScores.append(www)
                    avg=total / 3
                    avgScores.append(avg)
                    totalScores.append(total)


                    if avg >= 90:
                        grade= "A"
                    elif avg >= 80:
                        grade = "B"
                    elif avg >= 70:
                        grade = "C"
                    else:
                        grade = "D"

                    gradeScores.append(grade)

                    #gradeScores.append(gradeScores)
                    print("등급 : " + str(gradeScores) + "입니다." )







            elif subSelect == "2":
                print("성적보기")
                for i in range(len(sns)):
                    print("-------------------------------")
                    #print("파이썬 :" + str(pythonScores[i]) + "데이터 베이스 : " + str(dataBaseScores[i]) + "프론트 : " + str(wwwScores[i]))
                    #print("총점 : " + str(totalScores[i]) + "평균 : " + str(avgScores[i]))

                    print("파이썬 : ", pythonScores[i])
                    print("데이터베이스 : ", dataBaseScores[i])
                    print("프론트 : ", wwwScores[i])
                    print("총점 : ", pythonScores[i] + dataBaseScores[i] + wwwScores[i])
                    print("평균 : ", avgScores[i] /3)

                    print("등급 : " + str(gradeScores[i]) + "등급 입니다.")



                    print("-------------------------------")


            elif subSelect == "3":
                print("성적수정")
                sn = input("수정할 학번 : ")
                if sn in sns:




                    print("학번이 있습니다.")
                    idx = sns.index(int(sn))
                    #pythonScores[idx] = int(input(f"수정할 파이썬 점수 : {pythonScores[idx]} >> "))
                    #dataBaseScores[idx] = int(input(f"수정할 데이터베이스 점수 : {dataBaseScores[idx]}"))
                    #wwwScores[idx] = int(input(f"수정할 프론트 점수 : {wwwScores[idx]}"))
                    stuIdx = int(input("학번 : "))
                    pythonScores = int(input("파이썬 : "))
                    dataBaseScores = int(input("데이터베이스 : "))
                    wwwScores = int(input("프론트 : "))






                    totalScores[idx] = pythonScores[idx] + dataBaseScores[idx] + wwwScores[idx]
                    avgScores[idx] = totalScores[idx] / 3

                    if avgScores[idx] >= 90:
                        gradeScores = "A"
                    elif avgScores[idx] >= 80:
                        gradeScores = "B"
                    elif avgScores[idx] >= 70:
                        gradeScores = "C"
                    else:
                        gradeScores = "D"
                    print("수정되었습니다.")
                else:
                    print("학번이 확인되지않습니다.")
                    print("다시 시도해 주세요.")



            elif subSelect == "4":
                print("성적백업")


            elif subSelect == "9":
                print("뒤로가기")
                subRun = False
            else:
                print("잘못 입력하셧습니다.")

    elif select == "3":
        print(boardMenu)
        subRun = True
        while subRun:
            select = input(">>>")
            if select == "1":
                print("자유게시판.")
                board_titel = input("제목 : ")
                board_content = input("내용 : ")
                board_writer = input("작성자 : ")

            elif select == "2":
                print("건의게시판.")

            elif select == "3":
                print("학부모게시판.")










