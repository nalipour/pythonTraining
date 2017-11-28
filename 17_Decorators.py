# ######################################
# # Phase 5: Use the decorator syntax ##
# ######################################


class Rectangle(object):

    def __init__(self, w, h):
        self.w = w  # Yes, just make it public!
        self.h = h

    @property
    def a(self):
        return self.w * self.h

    @a.setter
    def a(self, new_area):
        self.w = float(new_area) / self.h


r = Rectangle(2, 3)

assert r.w == 2
assert r.h == 3
assert r.a == 6

r.w = 4

assert r.w == 4
assert r.h == 3
assert r.a == 12

r.a = 24

assert r.w == 8
assert r.h == 3
assert r.a == 24

print("All's well")


# ######################################
class Foo:

    def meth(*args):
        return args


print('done')

Foo().meth()
Foo.meth()


# ######################################
class Foo:

    def meth(*args):
        return args

    def static(*args):
        return args
    static = staticmethod(static)


Foo().static()
Foo.static()


# ######################################
class Foo:

    def meth(*args):
        return args

    @classmethod  # decorator syntax
    def class_(*args):
        return args
    # class_= classmethod(class_)

    @staticmethod  # decorator syntax
    def static(*args):
        return args
    # static=staticmethod(static)


Foo().class_()
Foo.class_()
