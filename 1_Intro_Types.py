""" First lessons """

import sys

a = sys.maxsize
b = a + 1

print(a, b, type(a), type(b))

c = 1 + 1j
type(c)

c.real
c.imag

c.conjugate
c.conjugate()

dir(complex)
complex.conjugate(c)

f = complex.conjugate
f(c)

help('modules')
help('numpy')
help('if')  # Help for keywords


# Tuples
type(())  # Empty tuple
(1, )  # 1-element tuple

a = 1, 2, 3  # tuple, parantheses are not always required
t = (1, 2, 3)
t[0] = 9
t


""" Lists """
l1 = [1, 2, 3]
l2 = l1
l2 == l1, l2 is l1
l2 += [4, 5]
l1, l2
l1 == l2, l2 is l1
l1 is l2

""" Tuples """
t1 = (1, 2, 3)
t2 = t1
t2 == t1, t2 is t1
t2 += (4, 5)

t1, t2
t1 == t2, t2 is t1

i1 = 0
i2 = i1
i2 == i1, i2 is i1
i2 += 1
i1, i2
i1 == i2, i2 is i1

# swap variables in tuples
a, b, c = 1, 2, 3
a, b = b, a

w = 5, 6, 7
x, y, z = w

a = range(10)

a[3]
a[-3]
list(a[3:6])
a[3:-3]
a[6:3]
a[:6]
a[0:6:2]
a[2:4] = ['x']
list(a)
a[-1:] = 'abc'

list(a)

# Sequence operations
a = range(4)
list(a) + [9, 8, 7]
a * 4
