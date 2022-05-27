# TODO Créer un docker et docker-compose pour heberger le tout.

import logging
from classes.GetScpConnexion import GetScpConnexion
from classes.ComparaisonRepertoireBdd import ComparationRepertoireBdd
from classes.DownloadFile import downloadFiles
from classes.dealWithSignal import *
from config import INFO_CONNEXION_BDD, INFO_CONNEXION_SCP, DESTINATION_REPERTOIRE, ORIGIN_DIRECTORY
#BDD de test
from tests.test_requirement import test_file_destination, test_file_origine, INFO_CONNEXION_SCP_TEST, INFO_CONNEXION_BDD_TEST

info_scp = INFO_CONNEXION_SCP
info_bdd = INFO_CONNEXION_BDD
destination = DESTINATION_REPERTOIRE
origine = ORIGIN_DIRECTORY


if __name__ == '__main__':
    connexion_scp = GetScpConnexion(info_scp)
    list_result_directory  = connexion_scp.get_list_repertoire(origine)
    files_to_download = ComparationRepertoireBdd(list_result_directory, repertoire_origine=origine).main(info_bdd)
    downloadFiles(files_to_download, destination, connexion_scp).download_files(base_directory_origine = origine)
    connexion_scp.ssh.close()
    logging.info("Fin du script de synchronisation")
