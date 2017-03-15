from datetime import date

class Personne:

    def __init__(self, nom, prenom, jour, mois, annee):
        self.nom = nom
        self.prenom = prenom
        self.naissance = date(annee, mois, jour)

    def introduce(self):
        print("Bonjour. Je m'appelle %s %s et j'ai %s ans" % (self.prenom, self.nom, self.age))

    def get_age(self):
        aujourdhui = date.today()
        anniversaries = self.naissance.replace(year=aujourdhui.year)
        age = aujourdhui.year - self.naissance.year  #
        if anniversaries > aujourdhui:
            age -= 1
        return age

    # création d'un attribut property
    age = property(get_age, doc='doc : Age de Personne')

# création d'une instance de Personne
moi = Personne('Legrand', 'Julien', 8, 12, 1980)
moi.introduce()

# accès à un attribut property
print(moi.age)




