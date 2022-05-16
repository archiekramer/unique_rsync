import mysql.connector
from mysql.connector import Error

class InteractionBdd:
    def __init__(self, username_bdd, mdp_bdd, database):
        self.database = database
        self.user = username_bdd
        self.password = mdp_bdd
        self.connexion = self.connexion_bdd()


    def connexion_bdd(self):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database=self.database,
                                                 user= self.user,
                                                 password=self.password)
            return connection

        except mysql.connector.Error as error:
            print("Failed to connect to in MySQL: {}".format(error))

    def deco_bdd(self):
        if self.connexion.is_connected():
            self.connexion.close()
            print("MySQL connection is closed")

    def verification_entree_bdd(self, taille, date, nom, parent):
        query = "Select sync from historique_download where size = %s and date_last_change = %s and nom = %s and parent_directory = %s"
        #query = "Select * from historique_download"
        cursor = self.connexion.cursor()
        cursor.execute(query, (taille, date, nom, parent))
        result = cursor.fetchall()
        cursor.close()
        if len(result) > 0:
            return True
        else:
            return False

    def insertion_bdd(self, taille, date, nom, parent):
        request = "Insert into historique_download (size, date_last_change, nom, parent_directory, sync)  VALUES ( %s, %s, %s, %s, %s)"
        cursor = self.connexion.cursor()
        result = cursor.execute(request,(taille, date, nom, parent, True))
        cursor.close()
        self.connexion.commit()

