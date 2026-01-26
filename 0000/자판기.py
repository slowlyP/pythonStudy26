# 목표
# 자판기 프로그램 만들기


# 필요한 변수
run = True
login_user = None




# 리스트
name = ["admin"]
password = ["123"]
id_admin = ["admin"]
admin = [True]



# 상품리스트 자판기?
#의류자판기 판매목록
item_type = ["shirt","shirt","pants","pants","coat","coat"] #카테고리
item_name = ["티셔츠","흰티셔츠","청바지","검은색바지","패딩","회색코트"] #이름
item_price = [20000,20000,30000,35000,50000,60000] #가격
item_qty = [10,10,5,10,3,3] #수량












main = """

======자판기====== 

1. 관리자로그인
2. 상품입고
3. 재고목록
4. 상품목록

=================

"""

submenu = """
======상품목록======
1. 셔츠
2. 바지
3. 코트
 
9. 뒤로가기
===================
"""


submenu2 = """
======재고수량======
1. 티셔츠
2. 흰티셔츠
3. 청바지
4. 검은색바지
5. 패딩
6. 회색코트
7. new
9. 뒤로가기
===================
"""



submenu3 = """
======상품입고======
1. 티셔츠
2. 흰티셔츠
3. 청바지
4. 검은색바지
5. 패딩
6. 회색코트
7. new
9. 뒤로가기
===================
"""

#관리자 로그인
while run:
    print(main)
    select = input(">>>")
    if select == "1":

        print("관리자 로그인")

        id = input("아이디: ")
    pw = input("비밀번호: ")


        if id in id_admin:
            idx = id_admin.index(id)
            if password[idx] == pw:
                login_user = idx
                print(f"{name[idx]}님 로그인 되었습니다.")


            else:
                print("비밀번호가 틀렸습니다.")
        else:
            print("존재하지 않는 계정입니다.")


    if select == "2":
        print(submenu3)
        if login_user is None:
            print("관리자 로그인이 필요합니다.")




        choice = input(">>>")


        if choice == "1":
            name = "티셔츠"
            category = "shirt"
            #price = menu_price[0]
        elif choice == "2":
            name = "흰티셔츠"
            category = "shirt"
            #price = menu_price[1]
        elif choice == "3":
            name = "청바지"
            category = "pants"
            #price = menu_price[2]
        elif choice == "4":
            name = "검은색바지"
            category = "pants"
            #price = menu_price[3]
        elif choice == "5":
            name = "패딩"
            category = "coat"
            #price = menu_price[4]
        elif choice == "6":
            name = "회색코트"
            category = "coat"
            #price = menu_price[5]

        elif choice == "7":
            name = input("새 상품 : ")
            category = input("카테고리(shirt,pants,coat): ")
            price = int(input("가격 : "))

        elif choice == "9":
            continue



        else:
            continue

        qty = int(input("수량 : "))

        if name in item_name:
            idx = item_name.index(name)
            item_qty[idx] += qty
            print("재고가 입고되었습니다.")

        else:
            item_name.append(name)
            item_qty.append(qty)
            item_type.append(category)
            item_price.append(price) # 신규상품입고시만
            print("상품입고 완료")

    if select == "3":
        print("재고목록")
        choice = input("1. shirt , 2. pants , 3. coat  >>>")
        for i in range(len(item_qty)):
            if choice =="1" and item_type[i] == "shirt":
                print(item_name[i], item_qty[i])
            elif choice =="2" and item_type[i] == "pants":
                print(item_name[i], item_qty[i])
            elif choice =="3" and item_type[i] == "coat":
                print(item_name[i], item_qty[i])
            else:
                continue

    if select == "4":
        print("상품목록")
        choice = input("1. shirt , 2. pants  , 3. coat  >>>")
        buy_map = []
        num = 1

        for i in range(len(item_qty)):

            if choice == "1" and item_type[i] == "shirt":
                print(f"{num}. {item_name[i]}재고 :,{item_qty[i]} 가격:,{item_price[i]}")
                buy_map.append(i)
                num += 1

            elif choice == "2" and item_type[i] == "pants":
                print(f"{num}.{item_name[i]}, 재고 :,{item_qty[i]} 가격:,{item_price[i]}")
                buy_map.append(i)
                num += 1

            elif choice == "3" and item_type[i] == "coat":
                print(f"{num}.{item_name[i]}, 재고 :,{item_qty[i]} 가격:,{item_price[i]}")
                buy_map.append(i)
                num += 1




        pay = input("구매할 상품 번호를 눌러주세요 (9:뒤로가기)>>> ")
if pay == "9":
            continue



        pay = int(pay)
        idx = buy_map[pay - 1]
        i = idx



        if item_qty[idx] == 0:
            print(f"{num}. {item_name[i]} (품절)")
            continue
        else:
            print(f"{num}. {item_name[i]} 재고:{item_qty[i]} 가격:{item_price[i]}")






        qty = int(input("구매 수량>>>"))
        if qty >item_qty[idx] :
            print("재고 부족")
            continue

        elif qty <= item_qty[idx] :


            total_price = item_price[idx] * qty
            print(f"총 구매 금액은 {total_price}원 입니다.")

            money = int(input("금액을 투입해주세요>>>"))

            if money > total_price:
                print("금액이 부족합니다.")
                continue

            change = money - total_price
            item_qty[idx] -= qty

            print("구매 완료")
            print(f"잔돈 : {change}")



        if item_qty[idx] == qty:
            item_qty[idx] -= qty
            print("구매 완료")
        else:
            #print("재고 부족")
            continue
