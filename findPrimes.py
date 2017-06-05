import math
import sys

import _thread
import time
import threading
from queue import Queue

allNumbers = []
primes = []
lock = threading.Lock()
q = Queue()

def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

def do_work(item):
    global primes
    if(is_prime(item)):
        with lock:
            primes.append(item)

def worker():
    while True:
        item = q.get()
        do_work(item)
        q.task_done()

def main():
    for i in range(4):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()

    for item in range(int(sys.argv[1])):
        q.put(item)

    q.join()

if __name__ == '__main__':
    start = time.perf_counter()
    main()
    print(primes)
    print('time:',time.perf_counter() - start)
