import pwd
import mysql.connector
from mysql.connector import Error
import logging

class InteractionBdd:
    def __init__(self, information_connexion_bdd):
        self.database = information_connexion_bdd["database"]
        self.user = information_connexion_bdd["username"]
        self.password = information_connexion_bdd["mdp"]
        self.connexion = self.connexion_bdd()


    def connexion_bdd(self):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database=self.database,
                                                 user= self.user,
                                                 password=self.password)
            return connection

        except mysql.connector.Error as error:
            logging.critical("Failed to connect to in MySQL: {}".format(error))

    def deco_bdd(self):
        if self.connexion.is_connected():
            self.connexion.close()
            logging.info("MySQL connection is closed")

    def verification_entree_bdd(self, taille, date, nom, parent):
        logging.info("Verification presence en BDD")
        query = "Select sync from historique_download where size = %s and date_last_change = %s and nom = %s and parent_directory = %s"
        try : 
            cursor = self.connexion.cursor()
            cursor.execute(query, (taille, date, nom, parent))
            result = cursor.fetchall()
        except : 
            logging.critical("Erreur dans la recherche en BDD")
            logging.critical("requete en erreur : {}".format(query))
            logging.critical("attribut de la requete : {} - {} - {} - {} - ".format(taille, date, nom, parent))
        else: 
            cursor.close()
        if len(result) > 0:
            return True
        else:
            return False

    def insertion_bdd(self, taille, date, nom, parent):
        logging.info("Tentative insertion en BDD")
        request = "Insert into historique_download (size, date_last_change, nom, parent_directory, sync)  VALUES ( %s, %s, %s, %s, %s)"
        try: 
            cursor = self.connexion.cursor()
            result = cursor.execute(request,(taille, date, nom, parent, True))
            logging.info("Insertion en BDD OK")
        except : 
            logging.critical("Erreur dans l'insertion en BDD")
            logging.critical("requete en erreur : {}".format(request))
            logging.critical("attribut de la requete : {} - {} - {} - {} - ".format(taille, date, nom, parent))
        cursor.close()        
        self.connexion.commit()
        logging.info("Commit en BDD effectué")
