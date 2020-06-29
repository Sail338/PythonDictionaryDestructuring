from destructure import Destructure

if __name__ == "__main__":

    class Foo(Destructure):
        def __init__(self, dictionary={}):
            super().__init__(dictionary)
            self.fname = "ranga"

    a = Foo({"test": "test"})
