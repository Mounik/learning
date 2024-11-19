import random

# Initialisation des variables
player_health = 50
enemy_health = 50
potions = 3
skip_turn = False

print("Bienvenue dans le jeu de rôle textuel !")

# Boucle principale du jeu
while player_health > 0 and enemy_health > 0:
    if not skip_turn:
        print("\n--- Nouveau Tour ---")
        print(f"Votre santé : {player_health} | Santé de l'ennemi : {enemy_health}")
        print(f"Potions restantes : {potions}")
        
        # Demande à l'utilisateur de choisir une action
        action = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

        if action == "1":
            # Attaque du joueur
            damage = random.randint(5, 10)
            enemy_health -= damage
            print(f"Vous avez infligé {damage} points de dégâts à l'ennemi !")
        elif action == "2":
            # Utilisation d'une potion
            if potions > 0:
                potion_heal = random.randint(15, 50)
                player_health += potion_heal
                potions -= 1
                skip_turn = True
                print(f"Vous avez utilisé une potion et récupéré {potion_heal} points de vie.")
            else:
                print("Vous n'avez plus de potions !")
                continue
        else:
            print("Choix invalide. Veuillez choisir 1 ou 2.")
            continue
    else:
        skip_turn = False  # Passe le tour sans action

    # Vérification de la victoire
    if enemy_health <= 0:
        print("\nFélicitations ! Vous avez vaincu l'ennemi !")
        break

    # Attaque de l'ennemi
    enemy_damage = random.randint(5, 15)
    player_health -= enemy_damage
    print(f"L'ennemi vous a infligé {enemy_damage} points de dégâts !")

    # Vérification de la défaite
    if player_health <= 0:
        print("\nVous êtes mort. L'ennemi a gagné.")
        break

    # Affichage des statistiques à la fin du tour
    print(f"\nVotre santé : {player_health} | Santé de l'ennemi : {enemy_health}")

print("Merci d'avoir joué !")
