films = {
    "Le Seigneur des Anneaux": 12,
    "Harry Potter": 9,
    "Blade Runner": 7.5
    }

prix = 0
for key in films:
    prix += films[key]

# Affichage du total du prix
print(f"\nTotal du prix des DVDs : {prix}")