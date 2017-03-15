L = ['coucou', 'ciao', 'bonjour']

###
def f(chaine):
    return 'c' in chaine

M = filter(f, L)
print(M)  # => return iterator. besoin de caster
print(list(M))

### avec Lambda
N = filter(lambda chaine: 'c' in chaine, L)
print(list(N))

### focntion qui retourne une fonction
def puissances(n):
    def f(x):
        return x**n
    return f

puissance_3 = puissances(3)
print(puissance_3(2))

###
def puissances_lambda(n):
    return lambda x: x**n

print(puissances_lambda(3)(2))


