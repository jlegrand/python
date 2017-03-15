class Decorator:
    def __init__(self, arg):
        self.arg = arg

    def __call__(self, cls):
        arg = self.arg

        class Enveloppe(cls):
            @staticmethod
            def multiplier(value):
                return value * arg
        return Enveloppe


@Decorator(4)
class TestClass:
    def multiplier(self, value):
        return value * 3

# TestClass = Decorator(4)(TestClass)
if __name__ == '__main__':
    to = TestClass()
    print(to.multiplier(5))
