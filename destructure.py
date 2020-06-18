class Destructure:
    def __init__(self, a):
        for x in a:
            self.__setattr__(x, a[x])

    def __getattr__(self, name):
        try:
            return self.__getattribute__(name)
        except AttributeError:
            return None


class DeepDestructure(Destructure):
    def __init__(self, a):
        pass

def destructure(dictionary) -> Destructure:
    """
    Takes in a dictionary and returns a class repr 
    of this class
    
    :param: dictionary a dictionary to destructure
    
    :returns: Destructure class
    """
    return Destructure(dictionary)
