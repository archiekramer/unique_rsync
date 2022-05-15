import sys, unittest, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from classes.ComparaisonRepertoireBdd import ComparationRepertoireBdd


class TestComparaisonRepertoire(unittest.TestCase):

    def setUp(self) -> None:
        self.base_obj= ComparationRepertoireBdd([], {}, "/home/archiekramer/Mediacentre/Divers/")


    ## Verification retour fonction nature de ligne ##
    def test_nature_ligne_repertoire(self):
        ligne ="drwxrwxr-x  9 archiekramer archiekramer 4,0K mai   11 20:19 02 - Professionnel"
        nature_ligne = self.base_obj.analyse_ligne_nature(ligne)
        self.assertEqual(nature_ligne, "DIRECTORY")

    def test_nature_ligne_vide(self):
        ligne = ""
        nature_ligne = self.base_obj.analyse_ligne_nature(ligne)
        self.assertEqual(nature_ligne, "EMPTY")

    def test_nature_ligne_fichier(self):
        ligne = "-rw-rw-r--  1 archiekramer archiekramer 157K mai   12 12:35 263baba20371d78775616bd3bc4a99ca.pdf"
        nature_ligne = self.base_obj.analyse_ligne_nature(ligne)
        self.assertEqual(nature_ligne, "FILE")

    def test_nature_ligne_size(self):
        ligne = "total 68K"
        nature_ligne = self.base_obj.analyse_ligne_nature(ligne)
        self.assertEqual(nature_ligne, "SIZE")

    def test_nature_ligne_size(self):
        ligne = "/home/archiekramer/Mediacentre/Divers/retropie-roms/roms-/atari2600:"
        nature_ligne = self.base_obj.analyse_ligne_nature(ligne)
        self.assertEqual(nature_ligne, "PATH")

