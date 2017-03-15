# Liste de nombre permiers < N
from time import time

start = time()

n = int(input('Liste des nombres premiers jusque N : '))

premiers = []

for i in range(2,n+1):
    for j in premiers:
        if i % j == 0:
            break
    else:
        premiers.append(i)

print(premiers)

end = time()
print(end - start)
