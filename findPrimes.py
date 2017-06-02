import math

def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

print(list(x for x in range(1000001) if is_prime(x)))

