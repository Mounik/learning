# Ouvrir le fichier prenoms.txt et lire son contenu.
with open('prenoms.txt', 'r') as file:
    lines = file.read().splitlines()
# print(lines)

# Récupérer chaque prénom séparément dans une liste.
prenoms = []
for line in lines:
    prenoms.extend(line.split())
# print(prenoms)

# Nettoyer les prénoms pour enlever les virgules, points ou espace.
prenoms_final = [prenom.strip('., ') for prenom in prenoms]
# print(prenoms_final)

# Écrire la liste ordonnée et nettoyée dans un nouveau fichier texte.
with open('prenoms_final.txt', 'w') as file:
    for prenom in sorted(prenoms_final):
        file.write(f"{prenom}\n")
