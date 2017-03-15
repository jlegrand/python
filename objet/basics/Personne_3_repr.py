from datetime import date

class Personne:

    def __init__(self, nom, prenom, jour, mois, annee):
        self.nom = nom
        self.prenom = prenom
        self.naissance = date(annee, mois, jour)

    def __str__(self):
        return "Bonjour. Je m'appelle %s %s et j'ai %s ans" % (self.prenom, self.nom, self.age)

    # Représentation de l'objet
    def __repr__(self):
        return "%s %s" % (self.prenom, self.nom)

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

print(repr(moi))
print((moi,))
print(moi)




