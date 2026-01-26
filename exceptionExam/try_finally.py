# try-finally : try문 실행중 예외 발생 여부에 상관없이
# 무조껀 수행되는 문장임

try : # 예외가 발생할것 같은 실행문
    f = open("foo.txt","w")
    # 실행문들 ~~~~

finally: # 중간에 오류가 나도 실행 안나도 실행
    f.close()