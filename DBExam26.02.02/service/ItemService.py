from common import Session
from domain.Item import Item

class ItemService:

    @classmethod
    def load(cls):
        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) as cnt FROM item")
                count = cursor.fetchone()['cnt']
        finally:
            conn.close()


            # 상품 관리 admin,manager 전용

    @classmethod
    def add_item(cls):
        if not Session.is_login() or Session.login_member.role != "manager":
            print("manager 권한이 필요합니다.")
            return

        code = input("아이템 코드 : ").strip()
        name = input("아이템 이름 : ").strip()
        price = int(input("가격 : "))
        stock = int(input("재고수량  : "))

        print("\n카테고리 선택")
        for idx, cat in enumerate(Item.CATEGORIES, start=1):
            print(f"{idx}. {cat}")

        sel = int(input("번호 선택:"))
        category = Item.CATEGORIES[sel - 1]

        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                sql = "INSERT INTO items (code, name, category, price, stock) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (code, name, category, price, stock))
                conn.commit()
                print("아이템 등록 완료")
        except Exception as e:
            print(f"등록 실패 : {e}")
        finally:
            conn.close()
            


