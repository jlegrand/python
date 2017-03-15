from personne import Personne


class Etudiant(Personne):

    def __init__(self, *args):
        super(Etudiant, self).__init__(*args[:-1])
        self.identifiant = args[-1]


fred = Etudiant('Legrand', 'Fred', 30, 5, 1998, 1500)
fred = Etudiant('Legrand', 'Fred', 30, 5, 1998, 1500)
print(fred)
