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

    def __contains__(self, item):
        return item in self.nom or item in self.prenom

    def __bool__(self):
        return self.age >= 18

    def __eq__(self, other):
        return self.nom == other.nom and self.prenom == other.prenom and self.age == other.age

    def get_age(self):
        aujourdhui = date.today()
        anniversaries = self.naissance.replace(year=aujourdhui.year)
        age = aujourdhui.year - self.naissance.year  #
        if anniversaries > aujourdhui:
            age -= 1
        return age

    # création d'un attribut property
    age = property(get_age, doc='doc : Age de Personne')



# Bool
moi = Personne('Legrand', 'Julien', 8, 12, 1980)
# moi = Personne('Legrand', 'Julien', 8, 12, 2000)
if moi:
    print(repr(moi) + " est majeur")
else:
    print(repr(moi) + " est mineur")

# Eq
toi = Personne('Legrand', 'Julien', 8, 12, 1980)
print(toi == moi)
