tuple1 = tuple('OK !')
print(tuple1)

tuple2 = ('ok !', 1, 2, 'test', 50.)
print(tuple2)
tuple3 = 'ok !', 1, 2, 'test', 50.
print(tuple3)

(a,b) = ('test', 5)
print(a,b)
a,b = 'test', 5
print(a,b)

#tuple non mutable mais contenant des listes (mutables)
#donc tuple est mutable
L = [1,2],[3]
L[0][0] += 1
print(L)

I = (1)
print(type(I)) # => int
