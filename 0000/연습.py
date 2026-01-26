#C
#R
#U
#D

#사용할 변수
run = True
login_user = None

ids = ["1"]
passwords = ["1"]
names = ["1"]


meun = """
=================
1. 회원 가입
2. 로그인
3. 회원 정보 수정
4. 회원 탈퇴
=================
"""

while run:
    print(meun)
    select = input("1~4 사이를 입력해 주세요.")
    if select == "1":
        print(" 회원 가입 ")
        name = input("이름 : ")
        id = input("아이디 : ")


        if id in ids:
            print("아이디가 중복됩니다.")
            continue


        else:
            print("사용 가능한 아이디입니다.")
        password = input("비밀번호 : ")


        if input("y를 누르면 가입됩니다.") == "y":
            names.append(name)
            ids.append(id)
            passwords.append(passwords)
            idx = ids.index(id)
            print(f"{ids[idx]} 님 가입을 환영합니다.")
        else:
            print("회원가입이 취소되었습니다.")


    elif select == "2":
        print(" 로그인 ")
        id = input("아이디 : ")
        password = input("비밀번호 : ")

        if id in ids:
            idx = ids.index(id)
            if passwords[idx] == password:
                login_user = idx
                print(f"{ids[idx]} 님 로그인 되었습니다.")
            else:
                print("일반계정입니다.")
        else:
            print("비밀번호가 틀렸습니다.")

