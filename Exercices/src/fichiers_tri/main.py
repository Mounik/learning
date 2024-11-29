"""
Trier les fichiers contenus dans le dossier data selon les associations suivantes :
mp3, wav, flac : Musique
avi, mp4, gif : Videos
bmp, png, jpg : Images
txt, pptx, csv, xls, odp, pages : Documents
autres : Divers
"""
from pathlib import Path
import sys

dirs = {
        ".mp3": "Musique",
        ".wav": "Musique",
        ".flac": "Musique",
        ".avi": "Videos",
        ".mp4": "Videos",
        ".gif": "Videos",
        ".bmp": "Images",
        ".png": "Images",
        ".jpg": "Images",
        ".txt": "Documents",
        ".pptx": "Documents",
        ".csv": "Documents",
        ".xls": "Documents",
        ".odp": "Archives",
        ".pages": "Documents",
        }

# On désigne le dossier a trier
tri_dir = Path.home() / "python" / "learning" / "src" / "fichiers_tri" / "data"
# Ou on récupère l'argument du chemin du dossier à trier
# tri_dir = sys.argv[-1]
# Compréhension de liste pour obtenir la liste des fichiers du dossier a trier
files = [f for f in tri_dir.iterdir() if f.is_file()]
# On parcourt chaque fichier et on déplace le fichier dans le bon dossier en fonction de 
# l'extension du fichier.
# Si l'extension n'est pas dans la liste, on la place dans le dossier "Divers".
for f in files:
    # On crée le chemin du dossier de destination en fonction de l'extension du fichier.
    # Si l'extension n'est pas dans la liste, on la place dans le dossier "Divers".
    output_dir = tri_dir / dirs.get(f.suffix, "Divers")
    # On crée le dossier de destination si il n'existe pas. Si le dossier existe déjà, on ne fait rien.
    output_dir.mkdir(exist_ok=True)
    # On déplace le fichier dans le bon dossier en fonction de l'extension du fichier.
    f.rename(output_dir / f.name)
