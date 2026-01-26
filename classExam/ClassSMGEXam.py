import os

class MemberFile:
    def __init__(self, file_name="memberslist.txt"):
        self.file_name = file_name
        self.members = []
        self.session = None
        self.load_member()

    # 파일 로드

    def load_memberlist(self):
        self.members = []

        if not os.path.exists(self.file_name):
            self.save_member()
            return