def yrange(n, m=0, p=1):
    while n > m:
        yield n
        n -= p


for e in yrange(10):
    print(e)

for e in yrange(10,5):
    print(e)

for e in yrange(10, 5, 2):
    print(e)

# for e in yrange(10, 5, -1):
#     print(e)
