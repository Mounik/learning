chemin = "/home/mounik/learning/fichier.txt"

with open(chemin, "r") as f:
    contenu = f.read().splitlines()
    print(contenu)
