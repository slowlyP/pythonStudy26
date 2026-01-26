# 주민번호를 입력 받아 생년월일 남녀 구분을 하는 코드
# input() 함수를 사용하면 콘솔로 데이터를 넣을수 있다.
# 처리0 : 주민번호 입력 검증 -> 14글자인지? 체크 6번째에 -가 있는지 -유무
# 처리1 : 생년월일을 추출 -> 1,2,5,6 1900년생 , 나머지 2000생
# 처리2 : 주민번호 8번째 글자를 추출 -> 남여 구분
# 처리3 : 9~10번째 글자를 추출해서 출생지역 구분


print("주민번호를 입력하세요(-포함 14자)")
ssn = input(">>>")
# 입력된 주민번호 검증 코드
if len(ssn) == 14: #키보드로 입력된 문자열이 14자인지 확인
    print("14자 입력이 확인되었습니다.")

else:
    print("주민번호 14자가 입력되지않았습니다.")
    exit(0) #강제 종료 됨

if ssn[6] == "-" :
    print("주민번호 7번째 구문자 인식완료")
else:
    print("주민번호 7번째 구문자 입력되지 않음")
    print("프로그램을 처음부터 다시시작 하세요")
    exit(0)

print("입력된주민번호 : "+ssn)
# 주민번호 앞 6자리를 생년월일로 추출 -> 1,2,5,6 1900년생
# 나머지는 2000년생

year = ssn[0:2] #생년
month = ssn[2:4] #생월
day = ssn[4:6] #생일

fullYear = "" #if 안쪽에서 변수를 만들면 버그가 생길수있기에 밖에 미리 변수를 만든다
# "" 두개는 null 처리용

if ssn[7] in ["1","2","5","6"] :
    fullYear = "19"+year
else :
    fullYear = "20"+year

print("귀하의 생년은 : "+ fullYear + "년생 입니다.")

#나이 계산
age = 2026 - int(fullYear)
print("귀하의 나이는" + str(age) + "세 입니다.")
# print는 문자열 + 숫자로 출력 오류가 발생
# 문자열로 변환(강제타입변환) str(age) > str로() 가둔다
gender = "" #성별 null변수
# 주민번호 8번째 숫자가 1,3,5,7 이면 남자 나머지는 여자
if ssn[7] in ["1","3","5","7"] :
    gender = "남성"
elif ssn[7] == "9" :
    gender = "외계인"
else :
    gender = "여성"
print("성별 " + gender + "은 입니다")

local = "" #출생지
ssnLocal = ssn[8:10] #출생지 코드 추출

if int(ssnLocal) <= 8 :
    local = "서울"
elif int(ssnLocal) <= 12 :
    local = "부산"
elif int(ssnLocal) <= 15 :
    local = "인천"
elif int(ssnLocal) <= 25 :
    local = "경기"
elif int(ssnLocal) <= 34 :
    local = "강원"
elif int(ssnLocal) <= 47 :
    local = "충청"
elif int(ssnLocal) <= 66 :
    local = "전라"
elif int(ssnLocal) <= 91 :
    local = "경상"
else:
    local = "제주"

print("귀하의 출생지는 " + local + "입니다.")
print("*" * 15)



















