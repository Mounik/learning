# Pathlib

La gestion des chemins de fichiers avec Python, c'est toute une histoire !

Python est excellent pour créer des scripts qui ont pour vocation de gérer des fichiers et des dossiers. J'ai personnellement une bonne dizaine de scripts qui tournent tous les jours sur ma machine pour différentes tâches de classification et organisation de mon système d'exploitation.

Historiquement, on utilisait des modules comme le module os, glob ou encore shutil pour exécuter des opérations de création, suppression et gestion des fichiers.

Le module pathlib, disponible depuis la version 3.4 de Python, permet d'effectuer presque toutes les opérations courantes sur un système d'exploitation, avec une syntaxe orientée objet beaucoup plus agréable à utiliser.

## La classe Path

La classe Path permet de créer un objet représentant un chemin vers un fichier ou un dossier de notre ordinateur. Ce chemin peut exister ou ne pas exister sur notre disque dur, ce n'est pas un prérequis.

La classe Path dispose de plusieurs méthodes de classes permettant d'accéder à des chemins courants de notre système d'exploitation, comme le dossier utilisateur :
```python
from pathlib import Path

dossier_utilisateur = Path.home()
```

On peut également récupérer le dossier courant :
```python
from pathlib import Path

dossier_courant = Path.cwd()
```

Ou encore créer un chemin spécifique en passant une chaîne de caractères à la classe Path :
```python
from pathlib import Path

documents = Path("/Users/thibh/Documents")
```

Si on affiche l'objet créé à partir de la classe Path, on se retrouve avec un objet PosixPath. Cet objet représente les chemins des systèmes Linux et Mac OS. Sur Windows, l'objet sera différent, car les chemins sur Windows ne sont pas les mêmes que sur Mac et Linux. Cela ne change cependant rien aux méthodes et attributs que l'on peut utiliser sur cet objet.
```python
>>> from pathlib import Path
>>> documents = Path("/Users/thibh/Documents")
>>> print(documents)
PosixPath('/Users/thibh/Documents')
```
## Concaténer des chemins

Pour concaténer des chemins, c'est très simple, il suffit d'utiliser une barre oblique (un slash en bon franglais) :
```python
from pathlib import Path

home = Path.home()              # PosixPath('/Users/thibh/')
documents = home / "Documents"  # PosixPath('/Users/thibh/Documents')
```
Le résultat de cette concaténation nous retourne un nouvel objet PosixPath, nous pouvons donc concaténer plusieurs chaînes de caractères à la suite.

pathlib se charge de son côté de gérer les différents systèmes d'exploitation et d'utiliser un slash ou un antislash selon que vous utilisiez Mac / Linux ou Windows. Ce comportement est donc similaire à la fonction os.path.join du module os.
```python
from pathlib import Path

home = Path.home()                         # PosixPath('/Users/thibh/')
documents = home / "Documents" / "Projet"  # PosixPath('/Users/thibh/Documents/Projet')
```
On peut également utiliser la méthode joinpath sur un objet Path. Ça peut être pratique si vous avez par exemple une liste de dossiers que vous souhaitez concaténer (grâce à l'unpacking et à l'opérateur splat *) :
```python
from pathlib import Path

home = Path.home()                        # PosixPath('/Users/thibh/')
dossiers = ['Projets', 'Django', 'blog']
home.joinpath(*dossiers)                  # PosixPath('/Users/thibh/Projets/Django/blog')
```
Si vous utilisez des slashs et que vous souhaitez utiliser une méthode de l'objet Path, pensez à utiliser les parenthèses pour entourer les chemins concaténés :
```python
from pathlib import Path

home = Path.home() # PosixPath('/Users/thibh/')

# Ne fonctionne pas car on essaie de récupérer l'attribut suffix sur la chaîne de caractères "main.py"
home / "Projet" / "main.py".suffix

# Avec des parenthèses, ça fonctionne !
(home / "Projet" / "main.py").suffix
```

Récupérer des informations sur un chemin

Grâce à l'orienté objet, on peut accéder à de nombreuses informations sur un chemin avec les attributs de l'objet Path :
```python
from pathlib import Path

p = Path("/Users/thibh/Documents/index.html")
p.name    # "index.html"
p.parent  # "/Users/thibh/Documents"
p.stem    # "index"
p.suffix  # ".html"
p.parts   # ("/", "Users", "thibh", "documents", "index.html")
```
Il existe également des méthodes qui permettent de vérifier l'existence et le type d'un chemin :
```python
from pathlib import Path

p = Path("/Users/thibh/Documents/index.html")
p.exists()   # True
p.is_dir()   # False
p.is_file()  # True
```
Là encore, quand un chemin peut nous être retourné par un de ces attributs, on récupère un objet Path.

On peut donc mettre bout à bout plusieurs fois le même attribut pour remonter de plusieurs dossiers par exemple :
```python
from pathlib import Path

p = Path("/Users/thibh/Documents/index.html")
p.parent.parent  # "/Users/thibh"
```
## Créer et supprimer des dossiers

Pour créer un dossier, on peut utiliser la méthode mkdir. Cette méthode ne fonctionnera par défaut que si le dossier n'existe pas.

Vous pouvez utiliser le paramètre exist_ok pour signifier que vous ne souhaitez pas qu'une erreur soit levée si le dossier existe déjà :
```python
from pathlib import Path

dossier = Path("/Users/thibh/Documents/SiteWeb")
dossier.mkdir()  # Lève une erreur si le dossier existe déjà
dossier.mkdir(exist_ok=True)
```
Si vous souhaitez créer une hiérarchie de dossier qui n'existent pas, il faut ajouter le paramètre parents :
```python
from pathlib import Path

# Le dossier SiteWeb et ses sous-dossiers n'existent pas
dossier = Path("/Users/thibh/Documents/SiteWeb/sources/css")

# On peut tout créer d'un coup avec le paramètre parents
dossier.mkdir(parents=True)
```
Pour supprimer un dossier, on utilise la méthode rmdir :
```python
from pathlib import Path

dossier = Path("/Users/thibh/Documents/SiteWeb")
dossier.rmdir()
```
Cette méthode ne fonctionne que si le dossier est vide.

Si le dossier contient des fichiers ou d'autres sous-dossiers, cette méthode ne fonctionne pas, et c'est le seul cas de figure où nous sommes obligés de repasser par le module shutil et la fonction rmtree :
```python
import shutil
from pathlib import Path

dossier = Path("/Users/thibh/Documents/SiteWeb")
shutil.rmtree(dossier)
```
## Créer, lire et écrire dans un fichier

Pour créer et supprimer un fichier, on peut utiliser respectivement les méthodes touch et unlink :
```python
from pathlib import Path

fichier = Path("/Users/thibh/Documents/SiteWeb/index.html")
fichier.touch()   # On crée le fichier
fichier.unlink()  # On supprime le fichier
```
Pour écrire du contenu dans un fichier, on utilise la méthode write_text :
```python
from pathlib import Path

fichier = Path("/Users/thibh/Documents/SiteWeb/index.html")
fichier.write_text("Accueil du site")
```
Il n'est pas obligatoire de créer le fichier au préalable avec la méthode touch.

Vous conviendrez que c'est plus rapide que de faire :
```python
from pathlib import Path

fichier = Path("/Users/thibh/Documents/SiteWeb/index.html")
with open(fichier, "w") as f:
    f.write("Accueil du site")
```
De la même façon, pour lire le contenu d'un fichier, on peut utiliser la méthode read_text :
```python
>>> from pathlib import Path

>>> fichier = Path("/Users/thibh/Documents/SiteWeb/index.html")
>>> fichier.read_text()
"Accueil du site"
```
Scanner un dossier

Là où pathlib rayonne, c'est vraiment dans la possibilité de scanner les dossiers de votre ordinateur avec des méthodes beaucoup plus faciles à retenir que le module glob.

Pour récupérer tous les fichiers et dossiers à l'intérieur d'un dossier, on peut utiliser la méthode iterdir :
```python
from pathlib import Path

for f in Path.home().iterdir():
    print(f.name)
```
On peut combiner cette méthode avec la méthode is_dir pour ne récupérer que les dossiers (ici avec une compréhension de liste) :
```python
from pathlib import Path

dossiers = [d for d in Path.home().iterdir() if d.is_dir()]
```
Pour scanner un dossier avec un peu plus de flexibilité, on peut utiliser la méthode glob (et oui, comme le module !). On peut par exemple ne récupérer que les fichiers dont l'extension est .png :
```python
from pathlib import Path

for f in Path.home().glob("*.png"):
    print(f.name)
```
Si vous souhaitez scanner un dossier de façon récursive, il suffit d'utiliser rglob à la place de glob :
```python
from pathlib import Path

for f in Path.home().rglob("*.png"):
    print(f.name)
```
Facile non 🥳 ?
## Quelques cas pratiques

Voici quelques cas pratiques qui vous montrent la flexibilité et la facilité d'utilisation de pathlib.

Ajouter un suffixe à un nom de fichier
```python
from pathlib import Path

p = Path.home() / "image.png"               # "/Users/thibh/image.png"
p.parent / (p.stem + "-lowres" + p.suffix)  # "/Users/thibh/image-lowres.png"
```
### Trier des fichiers selon leur extension
```python
from pathlib import Path

dirs = {".jpg": "Images",
        ".gif": "Images",
        ".mp4": "Videos",
        ".pdf": "Documents",
        ".mp3": "Musiques",
        ".wav": "Musiques"}

tri_dir = Path.home() / "Tri"
files = [f for f in tri_dir.iterdir() if f.is_file()]
for f in files:
    # Si aucune correspondance n'est trouvé pour l'extension, on place les fichiers dans un dossier Autres
    output_dir = tri_dir / dirs.get(f.suffix, "Autres")
    output_dir.mkdir(exist_ok=True)
    f.rename(output_dir / f.name)
```
On peut utiliser la méthode rename pour déplacer un fichier.

### Créer les constantes d'un dossier avec file
```python
from pathlib import Path

SOURCE_FILE = Path(__file__).resolve()  # resolve permet de résoudre les liens symboliques
SOURCE_DIR = SOURCE_FILE.parent
ROOT_DIR = SOURCE_DIR.parent
DATA_DIR = SOURCE_DIR / "DATA"
```