 # 성적 처리용 프로그램

 #Create : 성적입력
 #Read   : 성적보기
 #Update : 성적수정
 #Delete : 성적삭제

 # 필요한 변수
sns = [] #학번
names = [] # 이름
kors = [] #국어 점수
engs = [] # 영어 점수
mats = [] # 수학 점수
tots = [] # 총점 빈 배열
avgs = [] # 평균 빈 배열
grades = [] # 학점 빈 배열

menu = """
====================
'mbc' 아카데미 성적처리
====================

1. 성적입력
2. 성적보기
3. 성적수정
4. 성적삭제
5. 프로그램 종료

"""

run = True #프로그램 실행중


while run: # run 변수가 False 처리 될때까지 반복 하는역활
    # : 아래는 들여쓰기 4칸 정도 처리
    # 들여쓰기를 진행하면 하위 실행문 역활


    print(menu) #콘솔창에 메뉴 출력
    select = input("(1~5)값 입력 : ") #select 변수에 숫자를 넣는다
    #              키보드로 입력 받는 앞쪽에 출력메시지 이다.

    if select == "1": # 키보드로 입력한 숫자가 1이면 ==는 같은지 비교할때
        print("성적 입력.") # 입력한 숫자가 1일때 처리되는 부분

        sn = input("학번 : ")
        name = input("이름 : ")
        kor = int(input("국어 : "))
        eng = int(input("영어 : "))
        mat = int(input("수학 : ")) #키보드를 이용한 점수 입력
        # 키보드로 입력한 숫자는 문자로 인식되므로 int()로 감싸 계산용으로 변경해야함

        print("입력한 정보를 확인합니다.")
        #print(" 학번 : " + sn)
        #print(" 이름 : " + name)
        #print(" 국어 : " + kor)
        #print(" 영어 : " + eng)
        #print(" 수학 : " + mat) #키보드로 입력한 점수 확인
        #print에서 문자와 숫자가 같이 출력되려면 str()으로 숫자를 문자를 변경해야한다.
        #f" 포멧팅은{} 안에 변수가 숫자든 문자든 상관없이 출력해준다.
        #print("총점 : " + str(kor[i]) + str(eng[i]) + str(mat[i]))

        #print(f"평균 : {kor} + {eng} + {mat} ")

        if input("저장 y: ") == "y" : # 저장 시 y입력

            sns.append(sn)
            names.append(name)
            kors.append(kor)
            engs.append(eng)
            mats.append(mat) # 변수뒤에 s는 배열(리스트)
            tot = kor + eng + mat
            tots.append(tot) #입력후 저장시 총점 계산하여 넣음
            avgs.append(tot / 3)     #입력후 저장시 평균 계산하여 넣음

            avg = tot / 3

            if avg >= 90:
                grade = "A"
            elif avg >= 80:
                grade = "B"
            elif avg >= 70:
                grade = "C"
            else:
                grade = "F"

            grades.append(grade)
            print("학점 : " + grade + " 입니다.")



            print("저장 완료")
        else:
            print("저장되지 않았습니다.")
            print("처음부터 다시 입력하세요.")

    elif select == "2": # 키보드로 입력한 숫자가 2 일때
        print("성적 출력") # 2 입력했을때 출력 되는 부분
        print("===================================")
        print("[성적목록]")

        for i in range(len(sns)): # 리스트의 처음부터 끝까지 반복용
        #               len(sns) > sns 리스트의 길이를 가져온다 5(리스트가 5개일때)
        #         range(5) > 0부터 5까지 증가
        #    i in 5   > i 값에 0 ~ 5까지 반복 하고 끝난다.

        #tots[i] = kors[i] + engs[i] + mats[i]
        #avgs[i] = tots[i] / 3
        #오류 발생으로 주석처리 > index out of range
        #비어 있는 리스트는 주소가 없다.
        #해결방법 : .append()를 사용한다.
        #grades[i] =
        # 학점 a,b,c,f 만들어보기



            print("------------------------------------------------------------")
            print("학번 : " + sns[i] + " 이름 : " + names[i])
            print("국어 : " + str(kors[i]) + " 영어 : " + str(engs[i]) + " 수학 : " + str(mats[i]))
            print("총점 : " + str(tots[i]) + " 평균 : " + str(avgs[i]))
            print("학점 : " + str(grades[i]) + "학점 입니다.")
            print("------------------------------------------------------------")



    elif select == "3": # 키보드로 입력한 숫자가 3 일때
        print("성적 수정") # 3 입력했을때 출력되는 부분
        #등록된 학생의 점수를 가져온다.
        #학번을 이용해서 학생을 찾는다.
        sn = input("수정할 학번 : ")
        if sn in sns: #sns 학번이 들어있는 리스트 in은 안에 있는지
            print("학번이 있습니다.")
            idx = sns.index(sn) # 찾은 학번의 주소를 가져옴
            #print(f"이름 : {names[idx] , kors[idx] , engs[idx] , mats[idx] , tots[idx] , avgs[idx]} ")

            kors[idx] = int(input(f"수정할 국어 점수 : {kors[idx]} >> "))
            engs[idx] = int(input(f"수정할 영어 점수 : {engs[idx]} >> "))
            mats[idx] = int(input(f"수정할 수학 점수 : {mats[idx]} >> "))

            tots[idx] = kors[idx] + engs[idx] + mats[idx]
            avgs[idx] = tots[idx] / 3

            if avgs[idx] >= 90:
                grades[idx] = "A"
            elif avgs[idx]>= 80:
                grades[idx] = "B"
            elif avgs[idx] >= 70:
                grades[idx] = "C"
            else:
                grades[idx] = "F"

            print("===================================")
            print("[수정된 성적]")





            # 수정된 값을 기준으로 총점과 평균과 등급을 다시 등록한다.
        else:
            print("학번이 없습니다.")
            print("처음으로 돌아갑니다.")

        #등록된 학생의 점수를 수정한다.
        #수정된 값을 기준으로 총점과 평균과 등급을 다시 등록한다

    elif select == "4": # 키보드로 입력한 숫자가 4일때
        print("성적 삭제") # 4 입력했을때 출력되는 부분
        sn = input("학번 >>>")
        if sn in sns:
            idx = sns.index(sn)
            if input("삭제 하려면 'Y'를 눌러주세요.>>>") == "Y" :
                sns.pop(idx)
                names.pop(idx)
                kors.pop(idx)
                engs.pop(idx)
                mats.pop(idx)
                tots.pop(idx)
                avgs.pop(idx)
                grades.pop(idx)
                print("삭제가 완료되었습니다.")

            else:
                print("잘못 입력하셧습니다.")
                print("다시 시도해 주세요.")

    elif select == "5": # 키보드로 입력한 숫자가 5일때
        print("프로그램 종료") # 5 입력했을때 출력되는 부분
        run = False # while 문을 종료하여 프로그램이 꺼지도록 설정.

    else: # 1~5까지 값 이외의 문자를 입력하면 처리하는 용으로 넣는다.
        print("1~5값만 넣어주세요.")








