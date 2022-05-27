#Run this test from tests directory
from email.mime import base
from test_requirement import *

from classes.ComparaisonRepertoireBdd import ComparationRepertoireBdd

class TestComparaisonRepertoire(unittest.TestCase):

    def setUp(self) -> None:
        self.listing_repertoire = [b'/home/archiekramer/Project/unique_rsync/tests/test_file:', b'total 160K', b'-rw-rw-r-- 1 archiekramer archiekramer    0 2022-05-25 05:51 2', b'drwxrwxr-x 6 archiekramer archiekramer 4,0K 2022-05-25 05:50 Archiekramer - Projet last [mp3-128]', b'-rw-rw-r-- 1 archiekramer archiekramer    0 2022-05-25 05:51 fichier', b'-rw-rw-r-- 1 archiekramer archiekramer    0 2022-05-25 05:51 fihcier', b'-rw-rw-r-- 1 archiekramer archiekramer 138K 2022-05-25 05:43 json_data_test.json', b'-rw-rw-r-- 1 archiekramer archiekramer  14K 2022-05-26 06:04 unique_rsync.log', b'', b'/home/archiekramer/Project/unique_rsync/tests/test_file/Archiekramer - Projet last [mp3-128]:', b'total 16K', b"drwxrwxr-x 2 archiekramer archiekramer 4,0K 2022-05-25 05:49 qidsjasqk ['3]", b"drwxrwxr-x 2 archiekramer archiekramer 4,0K 2022-05-25 05:49 qidsjasqk ['3] (3e copie)", b"drwxrwxr-x 2 archiekramer archiekramer 4,0K 2022-05-25 05:51 qidsjasqk ['3] (autre copie)", b"drwxrwxr-x 2 archiekramer archiekramer 4,0K 2022-05-25 05:49 qidsjasqk ['3] (copie)", b'-rw-rw-r-- 1 archiekramer archiekramer    0 2022-05-25 05:48 test', b'', b"/home/archiekramer/Project/unique_rsync/tests/test_file/Archiekramer - Projet last [mp3-128]/qidsjasqk ['3]:", b'total 0', b'-rw-rw-r-- 1 archiekramer archiekramer 0 2022-05-25 05:48 test', b'-rw-rw-r-- 1 archiekramer archiekramer 0 2022-05-25 05:48 test (copie)', b'', b"/home/archiekramer/Project/unique_rsync/tests/test_file/Archiekramer - Projet last [mp3-128]/qidsjasqk ['3] (3e copie):", b'total 0', b'-rw-rw-r-- 1 archiekramer archiekramer 0 2022-05-25 05:48 test2#{]@ [-- @', b'-rw-rw-r-- 1 archiekramer archiekramer 0 2022-05-25 05:48 test2#{]@ [-- @ (copie)', b'', b"/home/archiekramer/Project/unique_rsync/tests/test_file/Archiekramer - Projet last [mp3-128]/qidsjasqk ['3] (autre copie):", b'total 0', b'', b"/home/archiekramer/Project/unique_rsync/tests/test_file/Archiekramer - Projet last [mp3-128]/qidsjasqk ['3] (copie):", b'total 0', b'-rw-rw-r-- 1 archiekramer archiekramer 0 2022-05-25 05:48 test']
        self.base_obj= ComparationRepertoireBdd([])
        self.base_fichier = ""

    def tearDown(self) -> None:
        pass
        # if self.connexion.is_connected():
        #     self.connexion.close()

    ## Verification retour fonction nature de ligne ##
    def test_nature_ligne_directory(self):
        ligne ="drwxrwxr-x  9 archiekramer archiekramer 4,0K mai   11 20:19 02 - Professionnel"
        nature_ligne = self.base_obj.analyse_ligne_nature(ligne)
        self.assertEqual(nature_ligne, "DIRECTORY")

    def test_nature_ligne_vide(self):
        ligne = ""
        nature_ligne = self.base_obj.analyse_ligne_nature(ligne)
        self.assertEqual(nature_ligne, "EMPTY")

    def test_nature_ligne_file(self):
        ligne = "-rw-rw-r--  1 archiekramer archiekramer 157K mai   12 12:35 263baba20371d78775616bd3bc4a99ca.pdf"
        nature_ligne = self.base_obj.analyse_ligne_nature(ligne)
        self.assertEqual(nature_ligne, "FILE")

    def test_nature_ligne_size(self):
        ligne = "total 68K"
        nature_ligne = self.base_obj.analyse_ligne_nature(ligne)
        self.assertEqual(nature_ligne, "SIZE")

    def test_nature_ligne_path(self):
        ligne = "/home/archiekramer/Mediacentre/Divers/retropie-roms/roms-/atari2600:"
        nature_ligne = self.base_obj.analyse_ligne_nature(ligne, base_directory = "/home/archiekramer/Mediacentre/Divers/")
        self.assertEqual(nature_ligne, "PATH")

    #Extraction des données brut et récupération des bonnes infoss (taille, date, comme attendu)
    def exploit_lignes_fichier(self):
        self.assertEqual(("0","2022-05-25 05:51", "fichier"), self.base_obj.ligne_fichier_extract(self.listing_repertoire[4]))

    #Donner une ligne dans le fichier absente de la base de données mene au telechargement
    def exploit_line_fichier_absente_bdd(self):
        objet_comparaison= ComparationRepertoireBdd(self.listing_repertoire, repertoire_origine = test_file_origine)
        #initier connexion_bdd
        objet_comparaison.init_co(INFO_CONNEXION_BDD_TEST)
        objet_comparaison.exploit_line(self.listing_repertoire[4])
        nom_fichier = objet_comparaison.file_to_sync["fichier"]["nom"]
        parent = objet_comparaison.file_to_sync["fichier"]["parent"]
        self.assertEqual(tuple(nom_fichier, parent), ("fichier", test_file_origine))

    #Donner une ligne dans le fichier présente de la base de données déja préssente
    def exploit_line_fichier_presente_bdd(self):
        objet_comparaison2= ComparationRepertoireBdd(self.listing_repertoire, repertoire_origine = test_file_origine)
        #initier connexion_bdd
        objet_comparaison2.init_co(INFO_CONNEXION_BDD_TEST)
        objet_comparaison2.exploit_line(self.listing_repertoire[4])
        self.assertEqual(objet_comparaison.file_to_sync["fichier"]["nom"], "fichier")

    #Donner un repertoire dans le fichier mène à son ajout en tant que repertoire parent actuel
    def exploit_ligne_path(self):
        pass

