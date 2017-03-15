class Decorator:
    def __call__(self, cls):
        class enveloppe(cls):
            def multiplier(self, value):
                return value * 2
        return enveloppe


class TestClass:
    def multiplier(self, value):
        return value * 3

TestClass = Decorator()(TestClass)
if __name__ == '__main__':
    to = TestClass()
    print(to.multiplier(5))
