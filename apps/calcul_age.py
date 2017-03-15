from datetime import date
from dateutil.relativedelta import relativedelta

# jour = input('JJ : ')
# mois = input('MM : ')
# annee = input('AAAA : ')
jour = 8
mois = 12
annee = 1980

today = date.today()
naissance = date(int(annee), int(mois), int(jour))

anniversaire = naissance.replace(year=today.year)

### method 1


def calculate_age(birth):
    return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))


print(calculate_age(naissance))

### method 2
rdelta = relativedelta(today, naissance)
print('Age in years - ', rdelta.years)
print('Age in months - ', rdelta.months)
print('Age in days - ', rdelta.days)

### method 3


def calcul_age(annee, mois, jour):
    aujourdhui = date.today()
    naissance = date(annee, mois, jour)
    anniversaries = naissance.replace(year=aujourdhui.year) # 2017 03 14
    age = aujourdhui.year - naissance.year #
    if anniversaries > aujourdhui:
        age -= 1
    return age


print(calcul_age(annee, mois, jour))

