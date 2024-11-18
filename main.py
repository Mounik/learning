import random

def jouer_partie():
    # Générer un nombre aléatoire entre 0 et 100
    number_to_guess = random.randint(0, 100)

    # Définir le nombre d'essais disponibles
    essais_disponibles = 5

    print(f"Vous disposez de {essais_disponibles} essais pour trouver un numéro mystère.")

    for i in range(essais_disponibles):
        # Demander à l'utilisateur son guess
        user_guess = input("Entrez votre nombre : ")

        # Vérifier si le guess est un entier
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Le numéro doit être un entier.")
            continue

        # Vérifier si le guess est dans l'intervalle correct
        if user_guess < 0 or user_guess > 100:
            print("Le numéro doit être compris entre 0 et 100.")
            continue

        # Indiquer à l'utilisateur si son guess est plus petit ou plus grand que le nombre mystère
        if user_guess < number_to_guess:
            print(f"Votre guess ({user_guess}) est plus petit que le nombre mystère ({number_to_guess}).")
        elif user_guess > number_to_guess:
            print(f"Votre guess ({user_guess}) est plus grand que le nombre mystère ({number_to_guess}).")

    # Vérifier si l'utilisateur a gagné ou perdu la partie
    if user_guess == number_to_guess:
        print(f"Félicitations ! Vous avez trouvé le nombre mystère ({number_to_guess}) en {i+1} essais.")
    else:
        print(f"Malheureusement, vous n'avez pas pu trouver le nombre mystère. Le nombre correct était {number_to_guess}.")
        print(f"You aviez {essais_disponibles- i-1} chance(s) restant(e)s.")

# Appeler la fonction pour démarrer la partie
jouer_partie()