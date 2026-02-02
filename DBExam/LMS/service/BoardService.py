from LMS.common.session import Session # 로그인 정보, db정보
from LMS.domain.Board import Board #oop board 객체



class BoardService:

    @classmethod
    def run(cls):
        if not Session.is_login(): # 로그인 상태 확인
            print("로그인 후 이용 가능합니다.")
            return

        while True: # board 주메뉴
            print(f"\n===== mbc 게시판 ({Session.login_member.name}접속중.)=====")
            cls.list_board()
            print("1. 글 쓰기")
            print("2. 글 상세 보기 (수정/삭제 가능)")
            print("0. 뒤로가기")

            sel = input(">>>")
            if sel == "1":
                cls.write_board()
            elif sel == "2":
                cls.view_detail()
            elif sel == "0":
                break



    @classmethod
    def write_board(cls):
        #   게시글 작성 메뉴 진입 안내
        print("\n[게시글 작성]")
        #   로그인 여부 확인( 비로그인 시 글 작성 불가 )
        if not Session.is_login():
            print("로그인 후 이용 가능합니다.")
            return
        #   현재 로그인한 사용자 정보 가져오기
        member = Session.login_member
        #   게시글 제목과 내용 입력
        title = input("제목 : ").strip()
        content = input("내용 : ").strip()

        #   제목 또는 내용이 비어있으면 등록 불가
        if not title or not content:
            print("제목과 내용은 비워둘 수 없습니다.")
            return
        #   DB 연결 객체 생성
        conn = Session.get_connection()
        try:
            #   커서 생성(dict 형태 결과 반환 가정)
            with conn.cursor() as cursor:
                #   게시글 등록 SQL
                #   active = 1 > 정상 게시글
                sql = """
                INSERT INTO boards (title, content, member_id, active)
                VALUES (%s, %s, %s, 1)
                """
                #   SQL 실행 (제목, 내용, 작성자 고유 번호 전달)
                cursor.execute(sql, (title, content, member.id))
                #   변경 사항 DB에 반영
                conn.commit()
                #   등록 완료 메시지 출력
                print("게시글 등록이 완료되었습니다.")
        finally:
            #   예외 발생 여부와 관계없이 DB 연결 종료
            conn.close()



    @classmethod
    def view_detail(cls):
        print("\n[게시글 상세보기]")

        keyword = input("게시글 번호 또는 제목 입력 : ").strip()

        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                if keyword.isdigit():
                    sql = """
                    SELECT b.*, m.name, m.uid
                    FROM boards b
                    JOIN members m ON b.member_id = m.id
                    WHERE b.id = %s
                        AND b.active = 1
                """
                    cursor.execute(sql, (int(keyword),))

                else:
                    sql = """
                        SELECT b.*, m.name, m.uid
                        FROM boards b
                        JOIN members m ON b.member_id = m.id
                        WHERE b.title LIKE %s
                            AND b.active = 1
                """
                    cursor.execute(sql,(f"%{keyword}%",))
                data = cursor.fetchone()

            if not data:
                print("검색 결과가 없습니다.")
                return

            board = Board.from_db(data)

            print("\n" + "=" * 60)
            print(f"번호   : {board.id}")
            print(f"제목   : {board.title}")
            print(f"작성자 : {board.writer_name} ({board.writer_uid})")
            print(f"내용   :\n{board.content}")
            print("=" * 60)
            
            while True:
                print("\n1. 수정")
                print("2. 삭제")
                print("0. 뒤로가기")
                sel = input(">>>")
                
                if sel == "1":
                    cls.update_board(board)
                    break
                elif sel == "2":
                    cls.delete_board(board)
                    break
                elif sel == "0":
                    break

        finally:
            conn.close()





    @classmethod
    def list_board(cls):
        print("\n" + "=" *60)
        print(f"{'번호':<5} | {'제목':<25} | {'작성자':<10} | {'작성일'}")
        print("=" * 60)

        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                # members 테이블과 join 하여 작성자 이름(name)을 가져온다.
                sql = """
                SELECT b.*, m.name
                FROM boards b
                JOIN members m ON b.member_id = m.id
                ORDER BY b.id DESC 
                """
                cursor.execute(sql)
                datas = cursor.fetchall()
                for data in datas:
                    # 날짜 형식 처리 (YYYY-MM-DD 형식으로 출력)
                    dete_str = data['created_at'].strftime('%Y-%m-%d')
                    print(f"{data['id']:<5} | {data['title']:<25} | {data['name']:<10} | {dete_str}")
        finally:
            conn.close()
        print("=" * 60)

    @classmethod
    def delete_board(cls, board):
        member = Session.login_member

        if member.role != "admin" and member.id != board.member_id:
            print("삭제 권한이 없습니다.")
            return

        confirm = input("정말 삭제하시겠습니까? (y/n) ").lower()
        if confirm != "y":
            print("삭제가 취소되었습니다.")
            return

        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                sql = "UPDATE boards SET active = 0 WHERE id = %s"
                cursor.execute(sql, (board.id,))
                conn.commit()
                print("게시글이 삭제되었습니다.")

        finally:
            conn.close()

    @classmethod
    def update_board(cls, board):
        member = Session.login_member

        # 권한 체크: 작성자 본인 또는 관리자만 가능
        if member.role != "admin" and member.id != board.member_id:
            print("수정 권한이 없습니다.")
            return

        print("\n[게시글 수정]")
        print("(Enter만 누르면 기존 값 유지)")

        # 새 제목 / 내용 입력
        new_title = input(f"제목 [{board.title}]: ").strip()
        new_content = input("내용 (Enter 시 기존 내용 유지): ").strip()

        # 입력 없으면 기존 값 유지
        title = new_title if new_title else board.title
        content = new_content if new_content else board.content

        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                sql = """
                    UPDATE boards
                    SET title = %s, content = %s
                    WHERE id = %s
                """
                cursor.execute(sql, (title, content, board.id))
                conn.commit()
                print("게시글이 수정되었습니다.")
        finally:
            conn.close()
