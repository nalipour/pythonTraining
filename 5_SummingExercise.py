# Summing exercise
from functools import reduce
from operator import add


def myint(token):
    try:
        return int(token)
    except ValueError:
        return 0


with open('numbers.txt') as f:
    for line in f.readlines():
        tokens = line.split()
        numbers = tuple(map(myint, tokens))

        print(reduce(add, numbers))
        print(sum(numbers))
