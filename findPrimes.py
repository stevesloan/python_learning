import math
import sys

import _thread
import time
import threading
from queue import Queue

allNumbers = []
primes = [1,]
lock = threading.Lock()
q = Queue()

def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

def do_work(item):
    print('working')
    if(is_prime(item)):
        with lock:
            print(item)
            global primes
            primes.push(item)

def worker():
    while True:
        item = q.get()
        do_work(item)
        q.task_done()

def main():
    for i in range(int(sys.argv[1])):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()


def test():
    global allNumbers
    global primes
    while allNumbers.length > 1:
        number = allNumbers.pop()
        if(is_prime(number)):
            primes.append(number)

def find_primes2(count):
    global allNumbers
    allNumbers = list(range(count))
    try:
        _thread.start_new_thread(test)
    except:
        print('cant do it')


if __name__ == '__main__':
    #find_primes2(int(sys.argv[1]))
    # print(allNumbers)
    main()
    print(primes)

