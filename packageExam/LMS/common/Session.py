# 로그인 상태 관리 클래스
# 현재 로그인한 회원(Member객체를 보관
# 전연변수 대신 객체로 돌려씀
# 로그인,로그아웃,로그인여부,관리자여부

class Session:
    login_member = None

    @classmethod
    def login(cls,member):
        cls.login_member = member

    @classmethod
    def logout(cls):
        cls.login_member = None

    @classmethod
    def is_login(cls):
        return cls.login_member is not None

    @classmethod
    def is_admin(cls):
        return cls.is_login() and cls.login_member.is_admin()