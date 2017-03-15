c = input('nb occurrences des lettres de la chaine : ')
R = []
letters = set(c)

for l in letters:
    R.append((l, c.count(l)))


print(sorted(R, key=lambda x: x[1], reverse=True))

