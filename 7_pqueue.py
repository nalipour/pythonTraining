class EmptyQueue(Exception):
    pass


class WrongType(Exception):
    pass


"""
def PriorityQueue():
    pass
"""


class PriorityQueue():

    def __init__(self):
        self._q = []

    def add(self, item, priority=2):

        if not isinstance(priority, int):
            raise TypeError
        elif priority < 0 or priority > 4:
            raise ValueError

        self._q.append((item, priority))
        self._q = sorted(self._q, key=lambda x: x[1])

    def pop(self):
        try:
            return self._q.pop(0)[0]
        except:
            raise EmptyQueue

    def __len__(self):
        return len(self._q)
