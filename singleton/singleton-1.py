class Singleton(object):
    def __init__(self, func):
        self._func = func
    def Instance(self,*a,**k):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._func(*a,**k)
            return self._instance
    def __call__(self):
        raise TypeError('Singletons must be accessed by `Instance`.')
    def __instancecheck__(self,inst):
        return isinstance(inst,self._func)

@Singleton
class App(object):
    def __init__(self, ):
        pass

a= App.Instance()
b=App.Instance()

print(a is b)
