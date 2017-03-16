D0 = {'hello' : 'World', 'age' : 4, 'c' : 10}
print(D0)

D1 = dict([['a', 3], ['b', 4]])
print(D1)

print(D1['a'])
D1['a'] = 2
print(D1['a'])
D1['c'] = 5
print(D1)

D1.update(D0)
print(D1)

D1.pop('c')
print(D1)

D1.keys()
D1.values()

for e in D1.items():
    print(e)
