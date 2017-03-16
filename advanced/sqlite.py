import sqlite3

connexion = sqlite3.connect('example.db')
curseur = connexion.cursor()

query = '''CREATE TABLE personne(id integer primary key, nom
text, prenom text, date text)'''

curseur.execute(query)

connexion.commit()
connexion.close()
