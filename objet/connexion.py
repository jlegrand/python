import sqlite3

class Connexion:

    def __init__(self, db_name):
        self.connexion = sqlite3.connect(db_name)
        # creation de la table
        self.curseur = self.connexion.cursor()
        try:
            query = '''CREATE TABLE personne(id integer primary key, nom text, prenom text, date text)'''
            self.curseur.execute(query)
            self.connexion.commit()
        except:
            pass

    def execute_query(self, query):
        self.curseur.execute(query)
        self.connexion.commit()

    def insert(self, liste):
        query = "INSERT INTO personne (nom, prenom) VALUES ('%s', '%s')" % (liste[0], liste[1])
        self.execute_query(query)

    def select(self):
        query = "SELECT * FROM personne"
        self.execute_query(query)
        return self.curseur.fetchall()

    def count(self, nom, prenom):
        query = "SELECT count(*) FROM personne where nom='%s' and prenom = '%s'" % (nom, prenom)
        self.execute_query(query)
        return self.curseur.fetchone()

    def update(self, nom, prenom, id):
        query = "UPDATE personne SET nom='%s' , prenom = '%s' WHERE id = '%d'" % (nom, prenom, id)
        self.execute_query(query)

    def delete(self, id):
        query = "DELETE from personne where id='%s'" % id
        self.execute_query(query)

    def disconnect(self):
        self.connexion.close()


if __name__ == '__main__':

    # connection à la base
    sqlite3 = Connexion('example.db')

    # ajout d'une personne
    L = ['Legrand', 'Julien']
    sqlite3.insert(L)

    # compte des personnes
    print(sqlite3.count('Legrand', 'Julien'))

    # Mis à jour de Julien Legrand
    sqlite3.update('Legrand', 'Julien', 0)

    # suppression de la personne
    sqlite3.delete(0)
    print(sqlite3.count('Legrand', 'Julien'))

    # deconnection
    sqlite3.disconnect()

