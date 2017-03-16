from datetime import date

class Personne:

    # def __new__(cls, nom, prenom, jour, mois, annee):
    #     return object.__new__(cls)

    def __init__(self, nom, prenom, jour, mois, annee):
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

    @property
    def age(self):
        '''doc : Age de Personne'''
        aujourdhui = date.today()
        try:
            anniversaries = self.naissance.replace(year=aujourdhui.year)
        except:
            anniversaries = self.naissance.replace(year=aujourdhui.year, day=28)

        age = aujourdhui.year - self.naissance.year  #
        if anniversaries > aujourdhui:
            age -= 1
        return age


if __name__ == '__main__':

    moi = Personne('Legrand', 'Julien', 8, 12, 1980)
    lui = Personne('Bissex', 'Tile', 29, 2, 1980)

    print(lui)







