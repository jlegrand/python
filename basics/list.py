
# mutabilité
L = ['el1', 'el2', 'el3', 56]
L[1] + '.changed'
L[3] += 4
print(L)

# reference
L = M = [1,2,3]
L[0] += 2
print(L,M)

# ref 2
L = [1,2,3]
M = ['x', L, 'y']
print(M)
M[1][1] = 0
print(M)
print(L)

# ref 3 : recupérer contenu et plus reference
L = [1,2,3]
M = ['x', L[:], 'y']
print(M)
M[1][1] = 0
print(M)
print(L)

# manipulation de listes
L=[5,8,9,3,7,4,6,1,0]

print(len(L))
print(min(L))
print(max(L))
print(sum(L))

# tri
print(L)
print(sorted(L))
print(L)
print(L.sort())
print(L)

# reverse
print(list(reversed(L)))
print(L.reverse())

L = [[],[]]
print(len(L))

#
L = list("coucou")
print(L)

# range
L = range(10)
print(L)

for i in range(10):
    print(i)

for i in range(2,10,3):
    print(i)

#enumerate
for i, element in enumerate(L):
    print(i, element)
