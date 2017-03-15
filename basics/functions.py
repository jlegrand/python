def f(x,y):
    return x+y, x*y

print(f(2,3))

### recursivité
def fact(n):
    s = 1
    for i in range (2,n+1):
        s *= i
    return s

print(fact(5))

### portée
a = [2]
b = 5

def f(x):
    x[0] += 1
    return x

def g(x):
    x += 1
    return x

print(f(a))
print(a)
print(g(b))
print(b)

###
def puissance(puissance, nombre = 2):
    return puissance * nombre

print(puissance(5))
print(puissance(5, 10))
print(puissance(nombre = 7, puissance = 2))

### nb args variables
def g(*args):
    print(args)
    print(type(args))
    return args[0],sum(args[1:])

print(g('a',1,2,3))

###
def h(a,b,c):
    return a*b+c

L = (4,5,6)
print(h(*L))
