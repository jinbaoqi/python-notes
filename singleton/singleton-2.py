class App(object):
    def __init__(self, ):
        pass
    _instance = None

    def __new__(cls,*a,**k):
        if not cls._instance:
            cls._instance = object.__new__(cls,*a,**k)
        return cls._instance

a = App()
b=App()
print(a is b)
