class Foo:
   
    def __init__(self, a):
        for i in a:
            self.__setattr__(i, a[i])
   
    def __getattr__(self, name):
 
        try:
            return self.__getattribute__(name)
        except Exception:
            return None
           
   
 
a = Foo({"bar": "bar2"})
print(a.bar)

