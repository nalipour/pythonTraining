def gen_ints(start, stop):
    """ Generator function """
    while start < stop:
        yield start
        start += 1
    return


a = gen_ints(3, 6)
for i in a:
    print(i)

b = gen_ints(10, 12)
next(b)
next(b)
next(b)
