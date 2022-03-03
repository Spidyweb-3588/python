import time

def print_time_module():
    # 현재 시간을 unix시간으로 출력
    print(time.time())
    # 현지의 시간을 struct_time으로 반환
    print(time.localtime())
    # UCT기준의 시간을 struct_time으로 반환
    print(time.gmtime())
    # struct_time을 요일 월 시간:분:초 년도 형식의 문자열로 변환 후 반환
    print(time.asctime())
    #설정한 시간(초) 동안 대기
    time.sleep(5)

if __name__=='__main__':
    print_time_module()