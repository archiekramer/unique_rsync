#Run this test from tests directory
from distutils.log import debug
from re import A
from test_requirement import *
from config import INFO_CONNEXION_BDD_TEST
import mysql.connector

from classes.ComparaisonRepertoireBdd import ComparationRepertoireBdd

class TestComparaisonRepertoire(unittest.TestCase):

    def setUp(self) -> None:
        # Creation BDD de test. 
        self.connection = mysql.connector.connect(host='localhost',
                                                database=self.database,
                                                user= self.user,
                                                password=self.password)
        cursor = self.connexion.cursor()
        result = cursor.execute(request,(taille, date, nom, parent, True))
        cursor.close()
        self.connexion.commit()
historique_download
        self.base_obj= ComparationRepertoireBdd([], {}, "/home/archiekramer/Mediacentre/Divers/")
        self.base_fichier = ""
        self.ligne_FILE = "-rw-rw-r--  1 archiekramer archiekramer 157K mai   12 12:35 263baba20371d78775616bd3bc4a99ca.pdf"
        self.ligne_PATH = "/home/archiekramer/Mediacentre/Divers/retropie-roms/roms-/atari2600:"

    def tearDown(self) -> None:
        if self.connexion.is_connected():
            self.connexion.close()


    ## Verification retour fonction nature de ligne ##
    def test_nature_ligne_directory(self):
        ligne ="drwxrwxr-x  9 archiekramer archiekramer 4,0K mai   11 20:19 02 - Professionnel"
        nature_ligne = self.base_obj.analyse_ligne_nature(ligne)
        self.assertEqual(nature_ligne, "DIRECTORY")

    def test_nature_ligne_vide(self):
        ligne = ""
        nature_ligne = self.base_obj.analyse_ligne_nature(ligne)
        self.assertEqual(nature_ligne, "EMPTY")

    def test_nature_ligne_fichier(self):
        ligne = self.ligne_FILE
        nature_ligne = self.base_obj.analyse_ligne_nature(ligne)
        self.assertEqual(nature_ligne, "FILE")

    def test_nature_ligne_size(self):
        ligne = "total 68K"
        nature_ligne = self.base_obj.analyse_ligne_nature(ligne)
        self.assertEqual(nature_ligne, "SIZE")

    def test_nature_ligne_path(self):
        ligne = self.ligne_PATH
        nature_ligne = self.base_obj.analyse_ligne_nature(ligne)
        self.assertEqual(nature_ligne, "PATH")

    def exploit_line_fichier(self):
        self.base_obj.exploit_line(self.ligne_FILE)

        pass

    def exploit_ligne_path(self):
        pass

    def extraction_ligne_fichier_correct(self):
        pass
    



