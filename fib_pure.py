# Run with cython: cython -a fib_pure.py
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
