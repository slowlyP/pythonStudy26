
class Member:
    def __init__(self,user_id,user_pw,user_name,role="user",active=True):
        self.user_id=user_id
        self.user_pw=user_pw
        self.user_name=user_name
        self.role=role
        self.active=active


    def __str__(self):
        status = "활성화" if self.active else"비활성화"
        return f"{self.user_id}|{self.user_pw}|{self.user_name}|{self.role}|{status}"

    def to_line(self):
        return f"{self.user_id}|{self.user_pw}|{self.user_name}|{self.role}|{self.active}"

    @classmethod
    def from_line(cls,line: str):
        user_id,user_pw,user_name,role,active=line.strip().split("|")
        return Member(
            user_id=user_id,
            user_pw=user_pw,
            user_name=user_name,
            role=role,
            active=(active == "True")
        )

    def is_admin(self):
        return self.role == "admin"
