from pprint import pprint


with open("prenoms.txt", "r") as f:
    lines = f.read().splitlines()

# pprint(lines)

prenoms = []
for line in lines:
    prenoms.extend(line.split())

# pprint(prenoms)

# nettoyage des , . et espaces superflus
prenoms_final = [prenom.strip(",. ") for prenom in prenoms]

pprint(prenoms_final)

with open("/Users/thibh/Documents/prenoms_final.txt", "w") as f:
    f.write("\n".join(sorted(prenoms_final)))
