'''
when dont be useing multi-processing
my result is very slower
'''
import time

first = time.perf_counter()

def show(name):
    print(f"process {name} is start")
    time.sleep(3)
    print(f"process {name} is finished")

p1 = show('Process1')
p2 = show('Process2')

second = time.perf_counter()

print( second - first)
print('proses end')
