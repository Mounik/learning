import pymysql
import logging

# Définition des paramètres de connexion
paramètres_connexion = {
    'host': 'localhost',
    'database': 'votre_base_de_donnees',
    'user': 'votre_utilisateur',
    'password': 'votre_mot_de_passe'
}

try:
    # Création d'une connexion à la base de données
    connexion = pymysql.connect(**paramètres_connexion)
    logging.info("Connexion réussie à la base de données")

except pymysql.Error as err:
    # Affichage d'un message d'erreur si la connexion échoue
    logging.error(f"Erreur de connexion : {err}")

# Exécution d'une requête SELECT
try :
    with connexion.cursor() as curseur :
        requete_select = "SELECT * FROM votre_table"
        curseur.execute(requete_select)
        resultat = curseur.fetchall()
        logging.info(resultat)

except pymysql.Error as err:
    # Affichage d'un message d'erreur si la requête SELECT échoue
    logging.error(f"Erreur de requête SELECT : {err}")

# Exécution d'une requête INSERT
try :
    with connexion.cursor() as curseur :
        valeurs_insert = ('valeur1', 'valeur2')
        requete_insert = "INSERT INTO votre_table (chemin_column, valeur) VALUES (%s, %s)"
        curseur.execute(requete_insert, valeurs_insert)
        connexion.commit()
        logging.info("Donnée insérée avec succès")

except pymysql.Error as err:
    # Affichage d'un message d'erreur si la requête INSERT échoue
    logging.error(f"Erreur de requête INSERT : {err}")

# Exécution d'une requête UPDATE
try :
    with connexion.cursor() as curseur :
        valeur_update = ('valeur_nuvelle',)
        requete_update = "UPDATE votre_table SET chemin_column = %s WHERE condition"
        curseur.execute(requete_update, valeur_update)
        connexion.commit()
        logging.info("Donnée mise à jour avec succès")

except pymysql.Error as err:
    # Affichage d'un message d'erreur si la requête UPDATE échoue
    logging.error(f"Erreur de requête UPDATE : {err}")

# Fermeture de la connexion
connexion.close()