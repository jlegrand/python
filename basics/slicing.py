### slicing
z = 'ceci est une chaine de caractere'
# caractère 5 à 10 exclu
print(z[5:10])
print(z[2:-2])
print(z[25:-20])
print(len(z))
print(z[32:])

print(z[:4])
print(z[-4:])

# avec un pas de 2
print(z[2:-2:2])
# pas de -1 sur l'ensmble de la chaine => inverse les caractères
print(z[::-1])
