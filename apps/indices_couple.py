X = range(6)
Y = range(4)
Z = 'abcd'

indices = []
for i in Y:
    for j in X:
        indices.append((i,j))
print(indices)

# idem avec liste de compréhension
indices2 = [(i,j) for i in Y for j in X]
print(indices2)
