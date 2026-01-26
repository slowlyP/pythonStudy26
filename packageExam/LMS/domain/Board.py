class Board:
    def __init__(self,no,title,content,writer,active=True):
        self.no=no
        self.title=title
        self.content=content
        self.writer=writer
        self.active=active


    def to_line(self):
        return f"{self.no}|{self.title}|{self.content}|{self.writer}|{self.active}"

    @staticmethod
    def from_line(line):
        line = line.strip()
        if not line:
            return None

        parts = line.split("|")
        if len(parts) != 5:
            return None

        no,title,content,writer,active = parts
        return Board(int(no),title,content,writer,active=="True")