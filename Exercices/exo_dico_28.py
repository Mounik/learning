employes = {
            "id01": {"prenom": "Paul", "nom": "Dupont", "age": 32},
            "id02": {"prenom": "Julie", "nom": "Dupuit", "age": 25},
            "id03": {"prenom": "Patrick", "nom": "Ferrand", "age": 36}
            }

# On efface Patrick
del employes["id03"]
# On modifie l'age de Julie
employes["id02"]["age"] = 26
# On récupère l'age de Paul
age_paul = employes["id01"]["age"]
print(f"Paul a {age_paul} ans.")
# On affiche le dico complet
print(employes)