# List comprehensions
[x * x for x in range(10)]
[(x, y) for x in range(4) for y in 'abc']
[(x, y) for x in range(6) if x % 2 for y in range(6) if x > y]

[x*x for x in range(10)]
list(map(lambda x: x*x, range(10)))

list(map(int, '123456789'))  # here map is cleaner
[int(x) for x in '123456789']

# Dictionary comprehensions
{x: x*x for x in range(10)}

# Set comprehensions (like a dict with key = 0)
{x*x for x in range(10)}

a = {1, 2, 3}
type(a)
type({})
type(set())
len({None})
len({})
set([])  # set constructor takes iterables
