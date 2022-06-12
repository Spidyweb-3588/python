from threading import Thread
from closure_decorator_logging_.time_elapse_logger_ import estimate_time_elapse
import time

@estimate_time_elapse
def work(id, start, end, result):
    total = 0
    for i in range(start,end):
        total += i
    result.append(total)
    return total

if __name__=="__main__":
    start,end = 0, 1000000000
    result = list()
    th1 = Thread(target=work, args=(1, start, end//2, result))
    th2 = Thread(target=work, args=(2, end//2, end, result))

    th1.start()
    th2.start()
    th1.join() # join()은 쓰레드가 끝날 때 까지 기다린다.
    th2.join()
    for i in range(200):
        print(i)
        time.sleep(0.1)
