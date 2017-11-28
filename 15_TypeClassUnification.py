class Old:
    pass


class New(object):
    pass


oldinstance = Old()
newinstance = New()

type(Old)
type(oldinstance)

type(New)
type(newinstance)


type(Old()) is Old
type(New()) is New

# This example makes sense for python2. Python3 has only new-style classes
