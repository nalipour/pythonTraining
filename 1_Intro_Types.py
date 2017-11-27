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

# Sequence operations: in Python3 range is an iterable, to make a list
a = list(range(4))
a + [9, 8, 7]
a * 4
b = [[0] * 4] * 4
b[0][0] = 1

3 in a
3 not in a
# max([1, 'x', 2, 'a'])  # not supported by python3
a = a
a += [9]
a.append(7)

# Variable, binding, call-by-value
i = 3
i = "hello"


def foo(a):
    a.append(6)


x = list(range(3))
foo(x)
print(x)


def bar(a):
    a = [5]


x = list(range(3))
bar(x)
print(x)

# Loops
epsilon = 1.0

while 1+epsilon > 1:
    epsilon /= 2
    print(epsilon)

for c in 'hello':
    print(c)

help(enumerate)

for index, item in enumerate('my data'):
    print(item, ' was in position ', index)

list(enumerate(range(10, 20)))


# Dictionaries
type({})
d = {}
d = dict()  # Empty dictionary
d[1] = 'eins'
d[2] = 'zwei'
d[1]
# d['eins']  # key error
len(d)
1 in d
'eins' in d
1 not in d

squares = {2: 4, 3: 9, 4: 16, 5: 25}
dict(a=1, b=2, c=3)
