#Metaclass for creating Singleton, this is a bad practice
class Singleton(type):
    __instance = None

    def __call__(cls, *args, **kw):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__call__(*args, **kw)
        return cls.__instance