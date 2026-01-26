



class ScoreService:
    def __init__(self):
        self.score = 0





    def run(self):

        subrun = True
        while subrun:
            print("""
=================================
1. 성적조회
2. 전체성적조회(admin)
3. 성적수정(admin)
4. 성적입력(admin)

9. 성적관리서비스종료
================================
""")

            select = input(">>>")
            if select == "1":
                print(" 성적조회 서비스로 진입합니다.")

                print(" 성적조회 서비스를 종료합니다.")

            elif select == "2":
                print(" 전체성적조회 서비스로 진입합니다. ")

                print(" 성적조회 서비스를 종료합니다.")

            elif select == "3":
                print(" 성적수정 서비스로 진입합니다.")

                print(" 성적조회 서비스를 종료합니다")

            elif select == "4":
                print(" 성적입력 서비스로 진입합니다.")

                print(" 성적조회 서비스를 종료합니다")

            elif select == "9":
                print("성적관리서비스종료")
                subrun = False

            else:
                print("잘못된입력입니다.")
