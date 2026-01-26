# 패키지  : 관련된 모듈(*.py)를 디렉토리로 묶어서 실행할수있게 만드는것
# 대부분 하위 폴더 아래쪽에 관련 파일들을 모아 관리한다.

# main.py
# 메뉴들
# __init__(패키지관리용 :  이 패키지가 제공하는 API 목록)
# -service 하위 디렉토리
# --MemberService.py
# --ScoreService.py
# --BoardService.py

# 객체들
# -domain 하위 디렉토리
# __init__(패키지관리용)
# --Member.py
# --Score.py
# --Board.py

# 텍스트파일
# -data 하위 디렉토리
# __init__(패키지관리용)
# --member.txt
# --score.txt
# --board.txt

#__init__.py : 패키지와 관련된 설정이나 초기화 코드를 포함함
# 패키지 변수밑 함수를 정의
# 패키지 내 모듈을 미리 import 하면 하위 py 파일을 한번에 import 할수있다.
from.graphic.render import render_test
#       폴더  .모듈         함수()
# . 은 현재 폴더(디렉토리) ..은 상위 폴더(디렉토리)
#

VERSION = 3.5 # 변수명을 대문자로 사용하면 상수(변하지않는값)

def print_version_info():
    print(f"이 게임의 버전은 {VERSION} 입니다.")


# 패키지 초기화 :  패키지를 처음 불러올때 => import game 라고 할때
# 실행 되어야 하는 코드를 작성할 수 있다.
# 예를 들면 데이터베이스 접속용 코드 / 파일로드 코드 등등
print("게임 패키지를 실행합니다.")
print("패키지 초기화중.......")
print("데이터베이스 연결중.....")
print("게임접속완료 -> 메뉴를 출력합니다.")















