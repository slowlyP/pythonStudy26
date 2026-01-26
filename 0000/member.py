# 회원 관리용 코드를 만든다
# c > 회원 추가
# r > 관리자일경우 (전체회원보기), 일반회원(로그인)
# u > 관리자일경우 (회원차단,암호변경문의,), 일반회원(내정보수정,암호변경)
# d > 회원탈퇴

# 메뉴구현
run = True #프로그램 동작중을 관리하는 변수
login_user = None

menu = """
============================
mbc 아카데미 회원 관리 프로그램
1. 회원가입
2. 로그인
3. 회원보기
4. 내정보수정
5. 프로그램 종료
============================
"""

# 사용할 리스트 변수를 생성한다.
sns = [1, 2]  #사용자 관리번호 (사번,학번,등등)
ids = ["smg","hww"]  #로그인용 아이디
passwords = ["1234", "4321"]  #로그인용 비밀번호
names = ["관리자","회원용"]  #사용자 명
emails = ["admin@mbc.com","hww@mbc.com"]  #이메일주소
admins = [True,False]  #관리자 유무 : 관리자 :True 일반사용자 : False




while run:
    print(menu)
    select = input("1~5숫자를 입력하세요: ")
    if select == "1":
        print("회원가입 메뉴에 진입하였습니다. ")
        sn = input("사원번호를 입력하세요. ")
        id = input("아이디를 입력하세요. ")
        pw = input("암호를 입력하세요. ")
        name = input("이름을 입력하세요. ")
        email = input("이메일을 입력하세요. ")
        admin = False

        print("입력된 값을 확인하시고 y를 누르면 가입됩니다.")
        print("이름 : " + name)
        print("id : " + id)
        print("pw : " + pw)
        print("name : " + name)
        print("emails : " + email)



        if input("y/n : ") == "y":
            sns.append(sn)
            ids.append(id)
            passwords.append(pw)
            names.append(name)
            emails.append(email)
            admins.append(admin)
            print("입력이 완료 되었습니다. ")
        else:
            print("처음부터 다시 진행하세요.")


    elif select == "2":
        print("로그인 메뉴")

        id = input("아이디: ")
        pw = input("비밀번호: ")


        if id in ids:
            idx = ids.index(id)
            if passwords[idx] == pw:
                login_user = idx
                print(f"{names[idx]}님 로그인 되었습니다.")

                if admins[idx]:
                    print("관리자 계정입니다.")
                else:
                    print("일반 계정입니다.")
            else:
                print("비밀번호가 틀렸습니다.")
        else:
            print("존재하지 않는 계정입니다.")



    elif select == "3":
        if login_user is None:
            print("로그인이 필요합니다.")
            continue

        if admins[login_user]:
            print("\n[전체 회원 목록]")
            for i in range(len(ids)):
                print(f"{i+1}. {names[i]} ㅣ {ids[i]} ㅣ {emails[i]} ㅣ 관리자:{admins[i]}")

        else:
             print("\n[내 정보]")
             print(f"이름 : {names[login_user]}")
             print(f"아이디 : {ids[login_user]}")
             print(f"비밀번호 : {passwords[login_user]}")





    elif select == "4":
        if login_user is None:
            print("로그인후 이용가능합니다.")
            continue
        print("\n내정보 수정")
        print("1. 이름 변경")
        print("2. 아이디 변경")
        print("3. 비밀번호 변경")
        print("4. 회원탈퇴")

        choice = input("선택 : ")

        if choice == "1":
            names[login_user] = input("새 이름 : ")
            print("이름 변경 완료 : " + names[login_user])

        elif choice == "2":
            ids[login_user] = input("새 아이디 : ")

            print("아이디 변경 완료 : " + ids[login_user])


        elif choice == "3":
            passwords[login_user] = input("새 비밀번호 : ")

            print("비밀번호 변경 완료 : " + passwords[login_user])

        elif choice == "4":
            if login_user is None:
                print("로그인후 이용가능합니다.")
                continue


            if id in ids:
                idx = ids.index(id)
                if passwords[idx] == pw:
                    login_user = idx
                    print("로그인 확인되었습니다.")
                else:
                    print("정보가 틀렸습니다.")
                    continue







    elif select == "5":
        print("회원가입 프로그램을 종료합니다. ")

        run = False
    else:
        print("1~5 사이 숫자를 입력하세요. ")
