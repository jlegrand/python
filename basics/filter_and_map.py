L = ['test', 'Toto', 'TITI', 'tATA']

print(list(filter(lambda x: x[0].isupper(), L)))

print(list(map(lambda x: x.capitalize(), L)))

