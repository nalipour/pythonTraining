class cls:
    a = 1


inst = cls()
dir(cls)
dir(inst)
cls.__dict__
inst.__dict__

inst.a = 22
inst.b = 333
dir(cls)
dir(inst)
cls.__dict__
inst.__dict__
