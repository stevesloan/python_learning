import math
import sys

import _thread
import time


allNumbers = []
primes = []

def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

def find_primes(count):
    print(list(x for x in range(count) if is_prime(x)))

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
    find_primes2(int(sys.argv[1]))
    # print(allNumbers)
