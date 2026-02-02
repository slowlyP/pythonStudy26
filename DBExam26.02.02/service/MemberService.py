from common import Session
from domain import Member

class MemberService:

    @classmethod
    def load(cls):
        conn = Session.get_connection()

        try:
            with conn.cursor() as cursor:
                cursor.execute("select count(*) as cnt from members")
                count = cursor.fetchone()['cnt']
                print(f"시스템에 현재 등록된 회원수는 {count}명 입니다. ")

        except:
            print("MemberService.load()메서드 오류발생...")

        finally:
            print("데이터베이스 접속 종료됨...")
            conn.close()

    @classmethod
    def login(cls):
        print("\n[로그인]")
        if Session.is_login():
            print("이미 로그인 상태입니다.\n로그아웃후 이용해주세요.")
            return
        uid = input("아이디 : ").strip()
        pw = input("비밀번호 : ").strip()

        conn = Session.get_connection()

        try:
            with conn.cursor() as cursor:
                sql = "SELECT * FROM members WHERE uid = %s AND password = %s"
                print("sql = " + sql)
                cursor.execute(sql, (uid, pw))
                row = cursor.fetchone()

                if row:
                    member = Member.from_db(row)
                    if not member.active:
                        print("비활성화된 계정입니다. 관리자에게 문의하세요.")
                        return
                    Session.login(member)
                    print(f"{member.name}님 로그인 성공({member.role})")
                else:
                    print("아이디 또는 비밀번호가 틀렸습니다.")
        except:
            print("MemberService.login()메서드 오류 발생...")

        finally:
            conn.close()
    @classmethod
    def logout(cls):
        if not Session.is_login():
            print("현재 로그인 상태가 아닙니다.")
            return
        Session.logout()
        print("로그아웃 되었습니다.")


    @classmethod
    def signup(cls):
        print("\n[회원가입]")
        if Session.is_login():
            print("로그인 상태에서 진행할수없습니다.")
            return

        uid = input("아이디 : ").strip()

        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                check_sql = "SELECT id FROM members WHERE uid = %s"
                cursor.execute(check_sql,(uid,))
                if cursor.fetchone():
                    print("이미 존재하는 아이디 입니다.")
                    return

                pw = input("비밀번호 : ").strip()
                name = input("이름 : ").strip()

                insert_sql = "INSERT INTO members (uid, password, name) VALUES (%s, %s, %s)"
                cursor.execute(insert_sql,(uid, pw, name))
                conn.commit()
                print("회원가입 완료! 로그인해 주세요.")

        except Exception as e:
            conn.rollback()
            print(f"회원가입 오류:{e}")
        finally:
            conn.close()

    @classmethod
    def modify(cls):
        if not Session.is_login():
            print("로그인 후 이용 가능합니다.")
            return

        member = Session.login_member
        print(f"내 정보 확인 : {member}")
        print("\n[내 정보 수정]\n1. 이름 변경 2. 비밀번호 변경 3. 계정 비활성 및 탈퇴 0. 취소")
        sel = input("선택 : ")

        new_name = member.name
        new_pw = member.pw

        if sel == "1":
            new_name = input("새 이름 : ").strip()
        elif sel == "2":
            new_pw = input("새 비밀번호 : ").strip()
        elif sel == "3":
            cls.delete()

        else:
            return

        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                sql = "UPDATE members SET name = %s, password = %s WHERE id = %s"
                cursor.execute(sql, (new_name,new_pw, member.id))
                conn.commit()

                member.name = new_name
                member.pw = new_pw
                print("정보 수정 완료")

        finally:
            conn.close()

    @classmethod
    def delete(cls):
        if not Session.is_login():
            print("로그인 후 이용 가능합니다.")
            return
        member = Session.login_member

        print("\n[회원 탈퇴]\n1. 완전 탈퇴 2. 계정 비활성화")
        sel = input("선택 : ")

        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                if sel == "1":
                    sql = "DELETE FROM members WHERE id = %s"
                    cursor.execute(sql, (member.id,))
                    print("회원 탈퇴 완료")
                    Session.logout()
                elif sel == "2":
                    sql = "UPDATE members SET active = FALSE WHERE id=%s"
                    cursor.execute(sql, (member.id,))
                    print("계정 비활성화 완료")
                    Session.logout()


                else:
                    print("잘못된 선택입니다.")
                    return

                conn.commit()

        finally:
            conn.close()

    @classmethod
    def admin_menu(cls):
        pass








