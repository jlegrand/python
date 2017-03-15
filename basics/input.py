# cf diff input & raw_input dans onenote
from datetime import datetime # pour implem 3

# Implem 1

nom = input('Votre nom : ')
genre = input('[1] M. [2] Mme : ')

if genre == '1' :
    print('Bonjour M. ' + nom)
elif genre == '2' :
    print('Bonjour Mme ' + nom)
else:
    print('Taper 1 ou 2 ')


# Implem 2 using dictionnary
def gender(x):
    return {
        '1': 'M.',
        '2': 'Mme',
    }[x]

while genre not in ('1','2'):
    genre = input('[1] M. [2] Mme : ')

print('Bonjour ' + gender(genre) + ' ' + nom)

# Implem 3
heure = datetime.now().hour
#if heure < 4 and heure > 18:
if 4 < heure < 18:
    print('Bonjour ' + gender(genre) + ' ' + nom)
else :
    print('Bonsoir ' + gender(genre) + ' ' + nom)
