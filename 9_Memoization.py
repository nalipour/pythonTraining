import time as t


def fib(n):
    """ recursive Fibonacci """
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


def memo(fn):
    """ memoizer closure answer """
    cache = {}

    def proxy(*args, **kwds):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]
    return proxy


m = memo(fib)
time(m(35))
