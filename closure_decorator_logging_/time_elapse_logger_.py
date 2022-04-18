import time
from time_datetime_pendulum import datetime_skill_up

def estimate_time_elpase(func):
    def wrapper():
        start_time = time.time()
        print(start_time)
        print(func())
        end_time = time.time()
        print(end_time)
        print("elapsed time :",end_time - start_time)
        return func
    return wrapper

@estimate_time_elpase
def add_tenbillion():
    sum = 0
    for i in range(1000000000):
        sum = sum + 1
    return sum

def recursive_func():
    pass

if __name__=="__main__":
    pass