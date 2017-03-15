class Personne:

    # initialisateur
    def __init__(self, nom, prenom, age, id):
        self.nom = nom
        self.prenom = prenom
        # attribut privée par convention. modifiable mais par convention, non manipulable => ajout _
        self._age = age
        # attribut privée => ajout de 2 _
        self.__id = id

    # methode
    def introduce(self):
        print ("Bonjour. Je m'appelle %s %s et j'ai %s ans" %(self.prenom, self.nom, self._age))

    # getter & setter
    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def del_id(self):
        print('del id')
        del self.__id

    # création d'une property
    id = property(get_id, set_id, del_id, 'ID Securite Social')
    # id = property(get_id, None,)
    # id = property(None, set_id)

# création d'une instance de Personne
moi = Personne('Legrand', 'Julien', 36, 1255545)
moi.introduce()

# accès attribut privé par convention
print(moi._age)
# accès à un attribut privé
# print(moi.__id) # => genere une erreur car attribut privée

# ajout d'un attribut à une instance
moi.__id = 5154154  # => ajout d'un attribut supplémentaire sur une instance
print(moi.__id)

# accès à un attribut public
moi.nom = 'Gilson'
moi.introduce()

# getter & setter
moi.set_id(2842154)
print(moi.get_id())

# accès à un attribut property
moi.id = 1255425
print(moi.id)
print(Personne.id.__doc__)
del moi.id
# print(moi.id)  # => genere erreur


