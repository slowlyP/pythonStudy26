
print("이름을 입력하세요")
name = input(":")

print("(-)포함 전화번호를 입력해주세요.")
phone = input(":")
if len(phone) == 15 :
    print("전화번호가 확인되었습니다.")

print("=" * 30)
print("주민번호 14자리를 입력하세요(-포함)")
ssn = input(">>>")
if len (ssn) == 14 :
    print("주민번호 14자리가 확인되었습니다.")
else :
    print("주민번호가 확인되지않습니다. 다시입력하세요")
    exit(0)

if ssn [6] == "-" :
    print("-" "입력확인완료")
else:
    print("-" "입력이 안되었습니다.")
    print("다시 입력해주세요.")
    exit(0)
# 031212 - 3456789
print("입력된 이름 : " + name[0] + "*" + name[2] )
print("입력된 주민번호 :" +ssn[0:8] + "******" )
year = ssn[0:2]
month = ssn[2:4]
day = ssn[4:6]

fullYear = ""

if ssn[7] in ["1","2","5","6"] :
    fullYear = "19"+year
else :
    fullYear = "20"+year

print("귀하의 생년 은 " + fullYear + "생 입니다.")

age = 2026 - int(fullYear)

print("귀하의 나이 는 " + str(age) + " 입니다")


gender = ""

if ssn[7] in ["1","3","5","7"] :
    gender = "'남성'"
elif ssn[7] in ["9"] :
    gender = "'물음표'"
else :
    gender = "'여성'"

print("성별 은 " + gender + " 입니다")

local = ""
ssnLocal = ssn[8:10]


if int(ssnLocal) <= 8 :
    local = "'서울'"
elif int(ssnLocal) <= 12 :
    local = "'부산'"
elif int(ssnLocal) <= 15 :
    local = "'인천'"
elif int(ssnLocal) <= 25 :
    local = "'경기'"
elif int(ssnLocal) <= 34 :
    local = "'강원'"
elif int(ssnLocal) <= 47 :
    local = "'충청'"
elif int(ssnLocal) <= 66 :
    local = "'전라'"
elif int(ssnLocal) <= 91 :
    local = "'경상'"
else:
    local = "'제주'"

print("출생지 는 " + local + " 입니다")

print("=" * 30)








