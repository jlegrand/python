from personne import Personne
import pickle

with open('serial.p', 'rb') as fichier:
    moi = pickle.load(fichier)

print(moi)