import math
import time
import sys

def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
        return True

start = time.perf_counter()
print(list(x for x in range(int(sys.argv[1])) if is_prime(x)))
print('time:',time.perf_counter() - start)
