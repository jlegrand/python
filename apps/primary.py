# Liste de nombre permiers < N
from datetime import datetime

start = datetime.now()

n = int(input('Liste des nombres premiers jusque N : '))

premiers = []

for i in range(2,n+1):

    premier = True

    for j in range(2,i):

        if i % j == 0:
            premier = False
            break
    if premier:
        premiers.append(i)

print(premiers)

end = datetime.now()
print(end - start)
