from time import time as tick


def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def memo(fn):
    cache = {}

    def proxy(*args, **kwds):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]
    return proxy


def time(fn, *args, **kwds):
    start = tick()
    result = fn(*args, **kwds)  # stars to unpack args and keywords
    stop = tick()

    return stop - start, result
