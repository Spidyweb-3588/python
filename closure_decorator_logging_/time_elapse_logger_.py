import time

def estimate_time_elapse(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        print(start_time)
        print(func(*args,**kwargs))
        end_time = time.time()
        print(end_time)
        print("elapsed time :",round(end_time - start_time,2))
        return
    return wrapper

"""@estimate_time_elapse
def add_tenbillion():
    sum = 0
    for i in range(1000000000):
        sum = sum + 1
    return sum

if __name__=="__main__":
    add_tenbillion()"""