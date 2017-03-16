from threading import Thread

def boucle(n, t):
    for i in range(n):
        print(i, t)

t1 = Thread(target=boucle, args=(3, 't1'))
t2 = Thread(target=boucle, args=(2, 't2'))

t1.start()
t2.start()
t1.join()
t2.join()
