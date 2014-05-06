# Run it with and without memo to see the time difference.
import sys
from functools import wraps

def memo(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap   


@memo
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def main():
    N = int(sys.argv[1])
    i = 1
    count = 0
    divisor = 21
    
    while i <= N:
        f = fib(i)
        if f % divisor == 0.0:
            count += 1
        i += 1
    print(count)
        
if __name__ == "__main__":
    main()
