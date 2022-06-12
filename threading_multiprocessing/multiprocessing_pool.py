import time
from multiprocessing import Pool

def count(name):
    for i in range(0,1000000):
        print(name," : ",i)
    return

if __name__=="__main__":
    start_time = time.time()
    num_list = ['p1', 'p2', 'p3', 'p4']
    pool = Pool(processes=4)
    pool.map(count,num_list)
    pool.close()
    pool.join()
    print("--- %s seconds ---" % (time.time()-start_time))