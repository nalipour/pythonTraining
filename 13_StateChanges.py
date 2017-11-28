class Happy:

    def __init__(self, name):
        self._name = name

    def greet(self):
        return self._name + ' says yipeeee'

    def sing(self):
        return self._name + ' la-de-lah'

    def change(self):
        self.__class__ = Sad


class Sad:
    def greet(self):
        return self._name + ' bugger off'

    def sing(self):
        return self._name + ' I am to depressed'

    def change(self):
        self.__class__ = Happy


h = Happy('Nil')
h.greet()
h.change()
h.greet()
