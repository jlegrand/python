from personne import Personne
import pickle

moi = Personne('Legrand', 'Julien', 8, 12, 1980)

with open('serial.p', 'wb') as fichier:
    pickle.dump(moi, fichier)