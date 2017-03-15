

def iterateur(liste):
    for e in liste:
        print('ici')
        yield e**2


liste = (1, 2, 3)

generateur = iterateur(liste)
generateur2 = (e**2 for e in liste)

print(generateur)

# for e in generateur:
#     print(e)
#
# print(generateur)
#
# for e in generateur:
#     print(e)

print(next(generateur))
print(next(generateur))
print(next(generateur))
# print(next(generateur)) # => lève une erreur stopIteration

