# 상품에 대한 crud를 구현해보자
# C = 상품 등록
# R = 전체 상품 목록
# r = 단일 상품 자세히보기
# U = 상품 수정
# D = 상품 삭제 or 품절
from random import choice

# 사용할 변수 (전역 변수)

run = True

item_type = ["electric","daily","fashion"] # 상품 분류 카테고리
item_names = ["냉장고","다용도방석","남성블레이저"] # 상품명
item_prices = [2000000,12000,42000] # 단가
item_quantity = [4,10,8] # 수량
product_infor = ["남바완!","궁둥이가 따뜻해지는","영혼까지끌어올린멋!"] # 상품 정보


# 사용할 메서드(함수)

def new_item():
    # 새상품 추가용 실행문 넣으면됨
    print("new_item()호출 완료")
    #print("신상 추가용 함수로 진입합니다.")
    choice = input("신상품 등록은 1번 :")

    if choice == "1":
        #item_add_menu() # item 추가용 메뉴 함수

        if choice == "1":

            name = input("신상품 이름: ")
            category = input("카테고리(electric,daily,fashion): ")
            price = int(input("가격 : "))
            quantity = int(input("수량 : "))
            info = input("상품 설명 :")
        else:
            print("잘못된 입력")
            return

        item_type.append(category)
        item_names.append(name)
        item_prices.append(price)
        item_quantity.append(quantity)
        product_infor.append(info)

        print("상품등록완료")






def item_list():
    # 리스트 출력용 for item in item_names: 등등
    #print("item_list()호출 완")
    print("현재 판매중인 상품 리스트")

    temp_index = []
    num = 1

    choice = input("1. electric\n2. daily\n3. fashion\n")
    for i in range(len(item_type)):
        if choice =="1" and item_type[i] == "electric":
            print(num,item_names[i], item_quantity[i] , item_prices[i])
            temp_index.append(i)
            num +=1

        elif choice =="2" and item_type[i] == "daily":
            print(num,item_names[i], item_quantity[i] , item_prices[i])
            temp_index.append(i)
            num +=1

        elif choice =="3" and item_type[i] == "fashion":
            print(num,item_names[i], item_quantity[i] , item_prices[i])
            temp_index.append(i)
            num +=1



    select = int(input("상품 번호 선택 : ")) -1
    item_idx = temp_index[select]

    print("\n[상품 상세 정보")
    print("상품명 : ", item_names[item_idx])
    print("가격 : ", item_prices[item_idx])
    print("수량 : ", item_quantity[item_idx])
    print("설명 : ", product_infor[item_idx])

    buy = input("구매 할려면 y : ")
    if buy == "y":
        buy_qty = int(input("구매 수량 입력 : "))

        if buy_qty > item_quantity[item_idx]:
            print("재고가 부족합니다.")
            return

        elif buy_qty < item_quantity[item_idx]:

            total_price = item_prices[item_idx] *  buy_qty
            print(f" 총 구매 금액은 {total_price}원 입니다.")

            money = int(input("금액을 지불해주세요 >>>"))

            if money > total_price:
                print("결제 완료")
            else:
                print("금액이 부족합니다.")


            change = money - total_price


            #print(" 구매 완료 ")
            print(f" 잔돈 : {change}")





def item_update():
    #print("item_update()호출 완")
    print("상품 수정")
    # 상품에 대한 정보 수정

def item_delete():
    #print("item_delete()호출 완")
    print("상품 삭제(품절)")
    # 상품 삭제 or 품절 처리

def main_menu():
    print("""
◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆
mbc 아카데미 # 입니다.
1. 상품등록
2. 상품리스트
3. 상품수정
4. 상품삭제
9. 프로그램 종료
◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆
""")

def item_add_menu():
    print("""
◆◆◆상품등록◆◆◆
1. 전자
2. 생활
3. 패션


9. 종료

""")
    # 프로그램 주실행 코드 시작
while run:
    main_menu() # 메인 메뉴 함수 호출하여 출력
    select = input(">>>")
    if select == "1":
        #item_add_menu() # item 추가용 메뉴 함수
        new_item() # item 추가용 코드









    elif select == "2":
        item_list()





    elif select == "3":
        item_update()




    elif select == "4":
        item_delete()




    elif select == "9":
        run = False

    else:
        print("잘못된 입력")
        continue

















