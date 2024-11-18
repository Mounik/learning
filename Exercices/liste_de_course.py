# Créer une simple liste de course

liste_de_course = []

def ajouter_item():
    item = input("Entrez l'item à ajouter à la liste : ")
    liste_de_course.append(item)
    print(f"Item ajouté avec succès : {item}")

def afficher_liste():
    if len(liste_de_course) == 0:
        print("La liste de course est vide.")
    else:
        for i, item in enumerate(liste_de_course, start=1):
            print(f"{i}. {item}")

def supprimer_item():
    if len(liste_de_course) == 0:
        print("La liste de course est vide.")
    else:
        afficher_liste()
        num = int(input("Entrez le numéro de l'item à supprimer : "))
        item = liste_de_course.pop(num-1)
        print(f"Item supprimé avec succès : {item}")

def modifier_item():
    if len(liste_de_course) == 0:
        print("La liste de course est vide.")
    else:
        afficher_liste()
        num = int(input("Entrez le numéro de l'item à modifier : "))
        item = liste_de_course[num-1]
        nouveau_item = input(f"Entrez le nouveau {item} : ")
        liste_de_course[num-1] = nouveau_item
        print(f"{item} mis à jour avec succès.")

while True:
    print("\nMenu de la liste de course")
    print("1. Ajouter un item")
    print("2. Afficher la liste")
    print("3. Supprimer un item")
    print("4. Modifier un item")
    print("5. Quitter")

    choice = input("Entrez votre choix : ")

    if choice == "1":
        ajouter_item()
    elif choice == "2":
        afficher_liste()
    elif choice == "3":
        supprimer_item()
    elif choice == "4":
        modifier_item()
    elif choice == "5":
        print("Au revoir!")
        break
    else:
        print("Choix invalide. Veuillez essayer à nouveau.")
