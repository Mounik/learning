lecture = input("Quels fichier ouvrir ? : ")

try:
    with open(lecture, 'r') as file:
        contenu = file.read()
        print(contenu)
except FileNotFoundError:
    print(f"Le fichier {lecture} n'existe pas.")
except Exception as e:
    print(f"Une erreur s'est produite : {e}")
