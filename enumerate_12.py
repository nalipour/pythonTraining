def genumerate(iterable, start=0):
    count = start
    for item in iterable:
        yield (count, item)
        count += 1


# In python 3, zip is lazy
from itertools import count
def ienumerate(iterable, start=0):
    return zip(count(start), iterable)

# In python2.1 no generators and no itertools->cenumerate, is the way to implement laziness
class cenumerate():
    def __init__(self, iterable, start=0):
        self._it = iter(iterable)
        self._n = start-1

    def __next__(self):
        self._n+=1
        return self._n, next(self._it)

    next=__next__

    # if the iterator on cenumerate is called (in a for loop for example), it should have a definition of the __iter__ function
    def __iter__(self):
        return self
