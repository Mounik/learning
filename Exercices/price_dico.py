films = {
    "Le Seigneur des Anneaux" : 12,
    "Harry Potter" : 9,
    "Blade Runner" : 7.5
}


# Initialisation de la variable pour le total du prix
prix = 0
total_prix = 0
# Boucle for pour itérer sur les films et calculer le total du prix
for film, prix in films.items():
    print(f"{film} : {prix}")
    total_prix += prix
    prix = total_prix
    
# Affichage du total du prix
print(f"\nTotal du prix des DVDs : {prix}")