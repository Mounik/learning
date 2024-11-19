# importer random
import random
# définir les points de vie des deux adversaires
PV_JOUEUR1 = 50
PV_JOUEUR2 = 50

# définir le nombre de potions
POTION = 3


# définir la question à poser au joueur
QUESTION1 = "Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? "

# créer la boucle while avec les if. La condition de sortie doit être la mort d'un adversaire
while PV_JOUEUR1 > 0 and PV_JOUEUR2 > 0 :
    reponse = input(QUESTION1)
    if reponse == "1" :
        # définir les attaques
        ATTAQUE_J1 = random.randint (5,10)
        ATTAQUE_J2 = random.randint (5,15)
        # jeu de combat
        print(f"Vous avez infligé {ATTAQUE_J1} points de dégats à l'ennemi.")
        PV_JOUEUR2 -= ATTAQUE_J1
        if  PV_JOUEUR2 <= 0 :
            print(f"Il vous reste {PV_JOUEUR1} point{'s'if PV_JOUEUR1>1 else ''} de vie.")
            print ("L'ennemi est mort")
            break
        print(f"L'ennemi vous a infligé {ATTAQUE_J2} point de dégats.")
        PV_JOUEUR1 -= ATTAQUE_J2
        if PV_JOUEUR1 <= 0 :
            print ("Vous êtes mort")
            print(f"Il reste {PV_JOUEUR2} point{'s'if PV_JOUEUR1>1 else ''} de vie à l'ennemi.")
            break
        # si aucun adversaire n'est mort, afficher les points de vie
        else :
            print(f"Il vous reste {PV_JOUEUR1} point{'s'if PV_JOUEUR1>1 else ''} de vie.")
            print(f"Il reste {PV_JOUEUR2} point{'s'if PV_JOUEUR1>1 else ''} de vie à l'ennemi.")

        print ("-"*50)

    elif reponse == "2" :
        # vérifier si il reste des potions
        if POTION == 0 :
            print ("Tu n'as plus de potion")
            continue
        # définir les PV de la potions
        PV_POTION = random.randint (15,50)
        # décrémenter la potion
        POTION -= 1

        PV_JOUEUR1 += PV_POTION
        print (f"Vous récuperez {PV_POTION} points de vie")
        # empêcher les PV d'être > 50
        if PV_JOUEUR1 >= 50 :
            PV_JOUEUR1 = 50
        # attaque du J2
        ATTAQUE_J2 = random.randint (5,15)
        print(f"L'ennemi vous a infligé {ATTAQUE_J2} point de dégats.")
        PV_JOUEUR1 -= ATTAQUE_J2

        if PV_JOUEUR1 <= 0 :
            print ("Vous êtes mort")
            print(f"Il reste {PV_JOUEUR2} point{'s'if PV_JOUEUR1>1 else ''} de vie à l'ennemi.")
            break
        # si aucun adversaire n'est mort, afficher les points de vie
        else :
            print(f"Il vous reste {PV_JOUEUR1} point{'s'if PV_JOUEUR1>1 else ''} de vie.")
            print(f"Il reste {PV_JOUEUR2} point{'s'if PV_JOUEUR1>1 else ''} de vie à l'ennemi.")

        print("-"*50)
        # deuxième attaque après avoir fait passer un tour
        print ("Vous passez votre tour")
        print(f"L'ennemi vous a infligé {ATTAQUE_J2} point de dégats.")
        PV_JOUEUR1 -= ATTAQUE_J2

        if PV_JOUEUR1 <= 0 :
            print ("Vous êtes mort")
            print(f"Il reste {PV_JOUEUR2} point{'s'if PV_JOUEUR1>1 else ''} de vies à l'ennemi.")
            break
        # si aucun adversaire n'est mort, afficher les points de vie
        else :
            print(f"Il vous reste {PV_JOUEUR1} point{'s'if PV_JOUEUR1>1 else ''} de vie.")
            print(f"Il reste {PV_JOUEUR2} point{'s'if PV_JOUEUR1>1 else ''} de vie à l'ennemi.")
        print ("-"*50)

    else :
        print ("Veuillez choisir la réponse 1 ou 2 !")
        continue

# afficher la fin des combats et si J1 a gagné ou perdu
print ("-"*50)
if PV_JOUEUR1 <= 0 :
    print ("Vous avez perdu !")
else :
    print("Vous avez gagné !")
print ("-"*50)
print("fin des combats.")