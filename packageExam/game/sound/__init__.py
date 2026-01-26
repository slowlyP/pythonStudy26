# __all__ 내장변수 : 전부 찾아와라

# __init__.py 파일이 있는 상태에서
# from game.sound import * ( 하위 모든것 )
        #   패키지(__init__)라고 되어있는건 패키지


#       이런식으로 오류가 뜸)
#>>> echo.echo_test()
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#NameError: name 'echo' is not defined



# echo라는 이름이 정의 되지않았다 라는 오류가 나옴
# *을 사용하고 싶으면 2가지 해결방법이있다.
# 1.__init__.py 파일을 만들지 말것,(패키지가 아님)
# 2.__init__.py __all__을 이용해서 제공 할것.

__all__ = ["echo"] # 변수에 리스트화 하여 모듈을 넣는다.
#           echo.py
# __all__ 이 의미하는건 sound 패키지 하위 모듈을 import할 목록임

# 이때 착각하기 쉬운것은
# from game.sound.echo import * 은 __all__ 에 상관없이 import 됨
#           모듈
# from game.sound import * 은 패키지를 *로 import 해서 __init__.py에 영향을 받음
#           패키지

#