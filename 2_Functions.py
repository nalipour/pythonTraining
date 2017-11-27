import math

help(zip)
list(zip(range(10), 'hello'))


def enumerate1(a):
    """ Non-lazy implementation of enumerate """
    return list(zip(range(len(a)), a))


t = enumerate1('hello')


def powers(n):
    """ Multiple return values (tuple)"""
    return n, n*n, n*n*n


ps = powers(2)
a, b, c = powers(2)


# First class objects
trig = math.sin, math.cos, math.tan
for fn in trig:
    print(fn, fn(math.pi/3))

# Lexical closures


def make_adder(n):
    """ Lexical closures """
    def adder(x):
        return n+x
    return adder


add3 = make_adder(3)
add9 = make_adder(9)
print(add3(4), add9(4))

# Argument passing


def one(*args):
    return args


def two(b=1, c=2):
    return b, c


def three(*args, **kwds):
    return args, kwds


def four(a, b=1, *args, **kwds):
    return a, b, args, kwds


one(1, 2, 'x')
two(c=9)
three("hello")

one(*'hello')
one(*range(3))
two(**{'c': 'banana', 'b': 'apple'})
three(*(list(range(3))+list(range(3))), **dict(a=1, b=2))
one(*(range(10)))
