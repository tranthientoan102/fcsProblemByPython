from functools import lru_cache


@lru_cache()
def fibonacci(n):
    result = 0
    if n == 0 or n == 1:
        result = 1
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
    return result


for i in range(1000):
    print("fibonacci({}) = {}".format(i, fibonacci(i)))
