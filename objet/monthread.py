from threading import Thread, Lock

verrou = Lock()

class MonThread(Thread):

    def __init__(self, nom):
        Thread.__init__(self)
        self.nom = nom

    def run(self):
        for i in range(5):
            verrou.acquire()
            print(self.nom, i)
            verrou.release()

if __name__=='__main__':
    t1=MonThread('T1')
    t2=MonThread('T2')
    t1.start()
    t2.start()