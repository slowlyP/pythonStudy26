class Score:
    def __init__(self,uid,kor,eng,math):
        self.uid = uid
        self.kor = kor
        self.eng = eng
        self.math = math

    @property
    def total(self):
        return self.kor +self.eng + self.math

    @property
    def avg(self):
        return (round(self.total /3,2))

    @property
    def grade(self):
        if self.avg >= 90:
            return 'A'
        elif self.avg >= 80:
            return 'B'
        elif self.avg >= 70:
            return 'C'
        else:
            return 'F'

    def to_line(self):
        return f"{self.uid}|{self.kor}|{self.eng}|{self.math}\n"

    @classmethod
    def from_line(cls, line):
        line = line.strip()
        if not line:
            return None

        parts = line.split("|")
        if len(parts) != 4:
            return None

        uid, kor, eng, math = parts
        return cls(uid,int(kor),int(eng),int(math))