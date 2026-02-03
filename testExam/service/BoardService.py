import os

from testExam.common import Session
from testExam.domain import Board

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR,"..","data","board.txt")

class BoardService:
    boards = []

    @classmethod
    def load(cls):
        cls.boards = []

        if not os.path.exists(FILE_PATH):
            return

        with open(FILE_PATH, "r", encoding="utf-8") as f:
            for line in f:
                board = Board.from_line(line)
                if board is not None:
                    cls.boards.append(board)

    @classmethod
    def save(cls):
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            for b in cls.boards:
                if b is not None:
                    f.write(b.to_line()+"\n")

    @classmethod
    def write(cls):
        if not Session.is_login():
            print("로그인 후 이용 가능합니다.")
            return
        title = input("제목 : ")
        content = input("내용 : ")
        writer = Session.login_member.user_id

        no = max([b.no for b in cls.boards], default=0)+1
        cls.boards.append(Board(no, title, content, writer))

        cls.save()
        print("글 등록 완료")

    @classmethod
    def list(cls):
        print("\n[게시글 목록]")
        print(f"no. 제목 / 작성자 / 내용")
        for b in cls.boards:
            if b.active:
                print(f"{b.no}/{b.title}/{b.content}/{b.writer}")

    @classmethod
    def delete(cls):
        if not Session.is_login():
            print("로그인 후 이용 가능합니다.")
            return
        no = int(input("삭제할 글 번호 : "))

        for b in cls.boards:
            if b.no == no:
                if (Session.login_member.user_id == b.writer or
                    Session.login_member.role == "admin"):
                    b.active = False
                    cls.save()
                    print("삭제 완료")
                else:
                    print("권한 없음")
                return
        print("글 없음")

    @classmethod
    def my_list(cls):
        if not Session.is_login():
            print("로그인 후 이용 가능합니다.")
            return

        user_id = Session.login_member.user_id
        print("\n[내 글 목록]")
        print("no. 제목 / 내용")

        found = False
        for b in cls.boards:
            if b.active and b.writer == user_id:
                print(f"{b.no}/{b.title}/{b.content}")
                found = True

        if not found:
            print("작성한 글 없음")

    @classmethod
    def run(cls):
        cls.load()

                cls.delete()
        while True:
            print("""
            [게시판]
            1. 글쓰기
            2. 글목록
            3. 글삭제
            4. 내글목록
            9. 뒤로가기
            """)

            sel = input(">>>")
            if sel == "1":
                cls.write()
            elif sel == "2":
                cls.list()
            elif sel == "3":
            elif sel == "4":
                cls.my_list()
            elif sel == "9":
                break