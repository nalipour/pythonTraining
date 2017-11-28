# Run the commands below in the terminal
# import pyximport
# pyximport.install()
# import fib_cython
# fib_cython
# from memo_10 import time
# time(fib_cython.fib, 35)

cpdef int fib(int n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
