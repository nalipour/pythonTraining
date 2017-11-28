def make_queue():
    return []


def add_to_queue(queue, item):
    queue.append(item)


def remove_from_front_of_queue(queue):
    return queue.pop(0)


q = make_queue()
add_to_queue(q, 1)
add_to_queue(q, 2)
add_to_queue(q, 3)

remove_from_front_of_queue(q)
remove_from_front_of_queue(q)
remove_from_front_of_queue(q)

# Classes


class Counter:

    def __init__(self, start):
        # print(dir(self))
        self._count = start
        # print(dir(self))

    def up(self, n=1):
        self._count += n

    def down(self, n=1):
        self._count -= n


# Queue class
class Q:
    def __init__(self):
        self._q = []

    def add(self, item):
        self._q.append(item)

    def remove(self):
        try:
            return self._q.pop(0)
        except IndexError:
            raise EmptyQueue  # ("extra details")


# Inheritance
class AddCounter(Counter):

    def __repr__(self):
        return 'Addcounter({._count})'.format(self)

    def __add__(self, other):
        return AddCounter(self._count + other._count)

    def __eq__(self, other):
        return self._count == other._count


# __radd__=__add__ # reverse add.
# Creates confusion because the name for both will remain add

a = Counter(10)
a.up(2)
print(a._count)
str(Counter)

AddCounter
repr(Counter)
repr(AddCounter)
AddCounter(4) == AddCounter(2)

c = Counter(3)
a = AddCounter(4)
c + c
a + a

c + a
a + c


# Emergency Queue Classes
class EmergencyQueue(Q):

    def addFront(self, item):
        self._q.insert(0, item)


class EmptyQueue(Exception):
    pass
