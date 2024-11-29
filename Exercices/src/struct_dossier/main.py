# Importez les modules nécessaires
import os
from pathlib import Path


# Définissez le chemin du dossier source
chemin = Path("/home/mounik/python/learning/Exercices/src/struct_dossier")

# Créez la structure de dossiers en utilisant le module os
def cree_structure_dossier(chemin):
    # Récupérez les clés et leurs valeurs du dictionnaire
    d = {
        "Films": ["Le seigneur des anneaux",
                "Harry Potter",
                "Moon",
                "Forrest Gump"],
        "Employes": ["Paul",
                    "Pierre",
                    "Marie"],
        "Exercices": ["les_variables",
                    "les_fichiers",
                    "les_boucles"]
    }
    
    # Créez chaque dossier et fichier
    for dossier, sousdossiers in d.items():
        print(f"Création du dossier {dossier}")
        os.makedirs(chemin / dossier, exist_ok=True)
        
        # Récupérez les fichiers à créer dans le dossier
        for sousdossier in sousdossiers:
            # Créez chaque fichier
            os.makedirs(chemin / dossier / sousdossier, exist_ok=True)

        print("Dossier créé avec succès")


# Appelez la fonction pour créer la structure de dossiers
cree_structure_dossier(chemin)

print("Structure de dossiers créée avec succès")