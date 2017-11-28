def message(text):
    if __name__ == "__main__":
        print(text)


class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.a = w * h


r = Rectangle(2, 3)
assert r.w == 2
assert r.h == 3
assert r.a == 6

r.w = 4

assert r.w == 4
assert r.h == 3
assert r.a == 12

# ########################################################
# # Phase 2: Make a depend on current values of w and h ##
# ########################################################


class Rectangle:

    def __init__(self, w, h):
        self.w = w  # Yes, just make it public!
        self.h = h

    # How to calculate the area from the other data
    def a(self):
        return self.w * self.h


r = Rectangle(2, 3)

assert r.w == 2
assert r.h == 3

try:
    assert r.a == 6
except AssertionError:
    message("Area interface has been broken")

# It fails because we have changed the interface: the public datum
# became a public function. This is exactly the sort of problem which
# the all-data-must-be-private dogma of Java and C++ tries to address

# In Python we can use properties to avoid this problem


# ###############################################
# # Phase 3: Fix the interface with a property ##
# ###############################################

class Rectangle(object):

    def __init__(self, w, h):
        self.w = w  # Yes, just make it public!
        self.h = h

    # How to calculate the area from the other data
    def a(self):
        return self.w * self.h

    # Here comes the magic line
    a = property(a)


r = Rectangle(2, 3)

assert r.w == 2
assert r.h == 3
assert r.a == 6

r.w = 4

assert r.w == 4
assert r.h == 3
assert r.a == 12

# Everything works as intended so far. But, if we try to assign a new
# area, it fails:

try:
    r.a = 24
except AttributeError:
    message("Assigning new area fails")


# #####################################
# # Phase 4: Make the area writeable ##
# #####################################

class Rectangle(object):

    def __init__(self, w, h):
        self.w = w  # Yes, just make it public!
        self.h = h

    # How to calculate the area from the other data
    def geta(self):
        return self.w * self.h

    # What does it mean to set the area
    def seta(self, new_area):
        self.w = float(new_area) / self.h

    # Here comes the magic line
    a = property(fget=geta, fset=seta)

    # Purely optional cleaning up of the namespace
    del geta, seta


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

message("All's well")
