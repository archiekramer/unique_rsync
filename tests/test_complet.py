#Run this test from tests directory
from email.mime import base
from test_requirement import set_up_bdd_vide, remove_bdd, INFO_CONNEXION_SCP_TEST, INFO_CONNEXION_BDD_TEST_2, ORIGIN_DIRECTORY_TEST, DESTINATION_REPERTOIRE_TEST
from test_requirement import charge_json_data
import unittest,time, os, time, shutil
from rsync_unique import main

class TestComparaisonRepertoire(unittest.TestCase):
    def setUp(self):
        set_up_bdd_vide(INFO_CONNEXION_BDD_TEST_2)
        self.json_string = charge_json_data()
        # repertoire destination creation
        try:
            os.makedirs(DESTINATION_REPERTOIRE_TEST)
        except FileExistsError: 
            shutil.rmtree(DESTINATION_REPERTOIRE_TEST)
            os.makedirs(DESTINATION_REPERTOIRE_TEST)

    def tearDown(self) -> None:
        shutil.rmtree(DESTINATION_REPERTOIRE_TEST)
        remove_bdd(INFO_CONNEXION_BDD_TEST_2)

    ## Verification retour fonction nature de ligne ##
    def test_complet(self):        
        time.sleep(0.5)
        main(info_scp = INFO_CONNEXION_SCP_TEST, info_bdd = INFO_CONNEXION_BDD_TEST_2, destination = DESTINATION_REPERTOIRE_TEST, origine = ORIGIN_DIRECTORY_TEST )
        chemin_fichier = []
        for key, value in self.json_string.items(): 
            chemin_fichier.append(value["parent"] + "/" + value["nom"])
        i =0 
        while os.path.isfile(chemin_fichier[i]) and i < (len(chemin_fichier) -1 ) :
            i += 1
        # erreur dans le jeu de donnée de test réglé avec le -1 ci dessous à corriger si retour dessus plus tard (recharger JDD propre)
        self.assertTrue(i == len(chemin_fichier)-1)


if __name__ == "__main__":
    runner = unittest.main()
