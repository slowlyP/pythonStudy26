class Member:
    def __init__(self,user_id, user_pw, user_name, user_role,active=True):
        self.user_id = user_id
        self.user_pw = user_pw
        self.user_name = user_name
        self.user_role = user_role
        self.active = active

    def to_line(self):
        return f'{self.user_id},{self.user_pw},{self.user_name},{self.user_role},{self.active}\n'





    @classmethod
    def from_line(cls, line):
        line = line.strip()
        if not line:
            return None

        parts = line.split(",")
        if len(parts) != 5:
            return None

        user_id, user_pw, user_name, user_role, active = parts
        active_bool = active == 'True'

        return cls(user_id, user_pw, user_name, user_role, active_bool)

