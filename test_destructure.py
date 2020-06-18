from destructure import Destructure


class Foo(Destructure):
    def __init__(self, dictionary={}):
        super().__init__(dictionary)
        self.fname = "ranga"


a = Foo({"test": "test"})
print(a.test)

