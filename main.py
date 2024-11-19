chemin = "/home/mounik/learning/fichier.txt"

with open(chemin, "r", "encoding='utf-8'") as f:
    contenu = f.read().splitlines()
    print(contenu)
