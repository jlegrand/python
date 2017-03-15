import time

def check(arg):
    def decorateur(f):
        def f_out(x):
            assert type(x) == arg
            return f(x)
        return f_out
    return decorateur


@check(int)
def f(x):
    return x**2

# print(f(3))
# print(f(3.))


###
def timer(arg):
    def decorateur(f):
        def f_out(*args):
            start = int(time.time() * 1000)
            out = f(*args)
            stop = int(time.time() * 1000)
            return (out, stop-start) if arg else out
        return f_out
    return decorateur


@timer(True)
def my_func(L):
    r = 0
    for e in L:
        r += e**2
    return r

L = range(1000000)
print(my_func(L))
