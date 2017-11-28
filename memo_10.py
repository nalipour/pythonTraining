from time import time as tick


def time(fn, *args, **kwds):
    start = tick()
    result = fn(*args, **kwds)  # stars to unpack args and keywords
    stop = tick()

    return stop - start, result


def fib(n):
    """ Recursive Fibonacci"""
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fibi(n):
    """ Iterative Fibonacci """
    c, p = 1, 1
    while n > 1:
        c, p = c + p, c
        n -= 1
    return c


def fibir(n, c=1, p=1):
    """ stack size exceeds if n>10000 """
    if n > 1:
        return fibir(n-1, c+p, c)
    return c


# tuple(map(fibi, range(10)))  # a good way to evaluate function


def memo(fn):
    cache = {}

    def proxy(*args, **kwds):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]
    return proxy
