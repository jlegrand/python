#entete de fichier (pour python 7)
#-*- coding: utf8 -*-
# ou  #!/path_to_python

# ceci est un commentaire
print('instruction 1'); print('instruction 2')

total = 'objet_1' + \
        'objet_2' + \
        'objet_3'
print(total)

# indentation = 4 espaces
# permet de séparer les blocs

x=1
if x==1:
    print('x est égal à 1')
else:
    pass #instruction pass = break

print('x=1', 'y=2', end='.', sep=':')
print('fin')

# pour executer certaines fonction de python 3 dans python 2
# ligne ignorée si executé en python 3
# inséré en début de fichier
# from __future__ import print_function
