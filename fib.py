import time
from functools import lru_cache

def timer(func):

    def wrapper(*args, **kwargs):
        '''Decorator for @timer'''
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Finished in {elapsed_time:.8f}s: {func.__name__}({', '.join(map(repr, args))}) -> {result}")
        return result
    
    return wrapper

@lru_cache
@timer
def fib(n: int) -> int:
    ''' Runs the fibonacci sequence '''
    
    if n < 0:
        return "Input should be a non-negative integer"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    fib(100)













