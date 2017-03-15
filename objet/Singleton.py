class Singleton:

    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
        return cls.instance


s1 = Singleton()
s2 = Singleton()

print(s1)
print(s2)