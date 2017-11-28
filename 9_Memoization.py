import time as t


# recursive Fibonacci
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def time(f):
    before = t.time()
    f
    after = t.time()
    return after - before


# time(fib(35))


# memoizer closure answer
def memo(fn):
    cache = {}

    def proxy(*args, **kwds):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]
    return proxy


m = memo(fib)
time(m(35))
