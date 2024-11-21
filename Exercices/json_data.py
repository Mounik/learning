import json

chemin = "/home/mounik/learning/data.json"

# ecrire "w" = json.dump
with open(chemin, "w") as f:
    json.dump(list(range(10)), f, indent=4)

# lire "r" = json.load
with open(chemin, "r") as f:
    liste = json.load(f)
    print(liste)

# Ajouter "w", on lit, on récupère dans une variable
# et on ajoute la valeur
with open(chemin, "r") as f:
    donnees = json.load(f)
donnees.append(10)

with open(chemin, "w") as f:
    json.dump(donnees, f, indent=4)
