from pathlib import Path
import shutil

p = Path("/home/mounik/learning/test.html")
print(p.name) # Donne le nom du fichier
print(p.parent) # Donne le parent du chemin
print(p.stem) # Donne le nom du fichier sans l'extension
print(p.suffix) # Donne le suffixe du fichier
print(p.suffixes) # Donne LES suffixes du fichier (ex : .tar.gz)
print(p.parts) # Décompose le chemin complet
print(p.exists()) # Vérifie son existence
print(p.is_dir()) # Vérifie si c'est un dossier
print(p.is_file()) # Vérifie si c'est un fichier

# Créer un dossier
p = Path("/home/mounik/learning/")
p = p / "DossierTest"
p.mkdir(exist_ok=True) # Si le dossier existe pas d'erreur ni de re-création de dossier

# Créer des sous dossiers
p = p / "1" / "2" / "3"
p.mkdir(parents=True, exist_ok=True)

# Crée un fichier
p = p / "readme.md"
p.touch()
# Remove un fichier
p.unlink()

# Supprime un dossier si il ne contient rien (le 3)
p = p. parent
p.rmdir()

# Supprimer une hierarchie de dossier, on passe par shutil (import shutil)
p = p.parent.parent.parent
shutil.rmtree(p)

# Ecrire dans un fichier
p = Path("/home/mounik/learning/Exercices")
p = p / "readme.txt"
p.touch()
p.write_text("Bonjour")

# Lire le fichier
p.read_text()
# print(p.read_text())
