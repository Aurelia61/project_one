def age() :
    mon_age = int(input())
    prenom = "Auré"
    return mon_age, prenom

def date(age_def, prenom_def):
    annee = 2020 - age_def
    print(f"{prenom_def} est née en {annee}")

mon_age, prenom = age()
date(mon_age, prenom)