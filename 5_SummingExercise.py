# Summing exercise
from functools import reduce
from operator import add, mul


def myint(token):
    try:
        return int(token)
    except ValueError:
        return 0


with open('numbers.txt') as f:
    for line in f:
        tokens = line.split()
        numbers = tuple(map(myint, tokens))

        print(reduce(add, numbers))
        print(sum(numbers))

# A general purpose code for multiplication, addition and strings
# -------IMPORTANT-------


def convert(identity_element):
    def clever(token):
        try:
            return int(token)
        except ValueError:
            return identity_element
    return clever


# op, identityElement = add, 0
op, identityElement = mul, 1

with open('numbers.txt') as f:
    for line in f:
        tokens = line.split()
        numbers = tuple(map(convert(identityElement), tokens))

        print(reduce(op, numbers, identityElement))
