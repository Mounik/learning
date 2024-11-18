import random

def jeu_du_nombre_mystere():
    # Génération du nombre mystère
    nombre_mystere = random.randint(0, 100)
    essais_max = 5  # Nombre maximum d'essais
    print("Bienvenue dans le jeu du Nombre Mystère !")
    print(f"Vous avez {essais_max} essais pour trouver le nombre entre 0 et 100.")

    for essai in range(1, essais_max + 1):
        try:
            # Demander une proposition au joueur
            proposition = int(input(f"Essai {essai}/{essais_max} - Entrez un nombre : "))
            
            # Vérifier la proposition
            if proposition < nombre_mystere:
                print("C'est plus grand !")
            elif proposition > nombre_mystere:
                print("C'est plus petit !")
            else:
                print(f"Félicitations ! Vous avez trouvé le nombre mystère {nombre_mystere} en {essai} essai(s) !")
                return
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    
    # Si le joueur n'a pas trouvé le nombre
    print(f"Dommage ! Vous avez utilisé vos {essais_max} essais. Le nombre mystère était {nombre_mystere}.")

# Lancer le jeu
if __name__ == "__main__":
    jeu_du_nombre_mystere()
