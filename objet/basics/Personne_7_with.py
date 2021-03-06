from datetime import date

class Personne:

    def __new__(cls, nom, prenom, jour, mois, annee):
        print('new')
        return object.__new__(cls)

    def __init__(self, nom, prenom, jour, mois, annee):
        print('init')
        self.nom = nom
        self.prenom = prenom
        self.naissance = date(annee, mois, jour)

    def __str__(self):
        return "Bonjour. Je m'appelle %s %s et j'ai %s ans" % (self.prenom, self.nom, self.age)

    # Représentation de l'objet
    def __repr__(self):
        self.annee, self.mois, self.jour = str(self.naissance).split('-')
        return "Personne(%r, %r, %i, %i, %i)" % (self.nom, self.prenom, int(self.jour), int(self.mois), int(self.annee))

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

    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')
        print(exc_type)

# new
with Personne('Legrand', 'Julien', 8, 12, 1980) as moi:
    print(moi)


