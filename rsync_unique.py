# TODO Créer un docker et docker-compose pour heberger le tout.

from classes.GetScpConnexion import GetScpConnexion
from classes.ComparaisonRepertoireBdd import ComparationRepertoireBdd
from classes.DownloadFile import downloadFiles
from classes.dealWithSignal import *
from config import INFO_CONNEXION_BDD, INFO_CONNEXION_SCP, DESTINATION_REPERTOIRE, ORIGIN_DIRECTORY


if __name__ == '__main__':
    connexion_scp = GetScpConnexion(INFO_CONNEXION_SCP)
    list_result_directory  = connexion_scp.get_list_repertoire(ORIGIN_DIRECTORY)
    files_to_download = ComparationRepertoireBdd(list_result_directory, ORIGIN_DIRECTORY).main()
    downloadFiles(files_to_download, DESTINATION_REPERTOIRE,connexion_scp)
    connexion_scp.ssh.close()
#TODO Problement telechargement fichier
#"/home/archiekramer/Mediacentre/Divers/Angel\ Arekin\ -\ Retour\ aux\ sources\ -\ Le\ Porteur\ de\ Mort\ 6\ \ \[mp3-64\]/01\ -\ Cycle\ 49\ -\ Chapitre\ 1.mp3"
#'/home/archiekramer/Mediacentre/Divers/Angel Arekin - Retour aux sources - Le Porteur de Mort 6 [mp3-64]/19 - Chapitre 19.mp3'

