'''
useing multi-processing 
my result is faster
'''
import time
from multiprocessing import Process

first = time.perf_counter()
def show(name):
    print(f"process {name} is start")
    time.sleep(3)
    print(f"process {name} is finished")

p1 = Process(target=show,args=('Process1',))
p2 = Process(target=show,args=('Process2',))
 
p1.start()
p2.start()

p1.join()
p2.join()

second = time.perf_counter()

print( second - first)
print('proses end')
