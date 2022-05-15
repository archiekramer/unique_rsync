# TODO Créer un docker et docker-compose pour heberger le tout.

from classes.GetScpConnexion import GetScpConnexion
from classes.ComparaisonRepertoireBdd import ComparationRepertoireBdd
from classes.DownloadFile import downloadFiles
from config import INFO_CONNEXION_BDD, INFO_CONNEXION_SCP, DESTINATION_REPERTOIRE

origin_directory = "/home/archiekramer/Mediacentre/Divers/"

if __name__ == '__main__':
    connexion_scp = GetScpConnexion(INFO_CONNEXION_SCP)
    list_result_directory  = connexion_scp.get_list_repertoire(repertoire_origin)
    resultat_analyse = ComparationRepertoireBdd(list_result_directory, INFO_CONNEXION_BDD, origin_directory).main()
    downloadFiles(resultat_analyse.file_to_sync, DESTINATION_REPERTOIRE,INFO_CONNEXION_SCP, INFO_CONNEXION_BDD)
    connexion_scp.ssh.close()
