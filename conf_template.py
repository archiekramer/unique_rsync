
DESTINATION_REPERTOIRE = "DESTINATION"
ORIGIN_DIRECTORY = "ORIGIN"
BASE_NON_REPRISE = ORIGIN_DIRECTORY

INFO_CONNEXION_SCP = {
    "host" : "UHOST",
    "login" : "username"
}

INFO_CONNEXION_BDD = {"username" : "username",
               "mdp" : "SUPERSECRETPASSWORD",
               "database" : "history_sync"
                }

#A supprimer en production 
DEBUG = False

LOG_DIRECTORY = '~/'
filename_log = 'unique_rsync.log'
import logging

if DEBUG is True:
    logging.basicConfig(filename=LOG_DIRECTORY + filename_log, level=logging.DEBUG)
else:
    logging.basicConfig(filename=LOG_DIRECTORY + filename_log', level=logging.ERROR)

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s')
#Rotation des fichiers de log 1 fois par semaine on en garde 4 max
logging.handlers.TimedRotatingFileHandler(filename_log, when='W0',backupCount=4)