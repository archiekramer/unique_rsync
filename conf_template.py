
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


#A modifier en production 
DEBUG = True
import logging
from logging.handlers import TimedRotatingFileHandler


filename_log = 'unique_rsync.log'

logger = logging.getLogger()
if DEBUG is True:
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.ERROR)
format = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s')
#Rotation des fichiers de log 1 fois par semaine on en garde 4 max
rotation_logging_handler = TimedRotatingFileHandler(filename_log, when='W0', backupCount=5)
rotation_logging_handler.setFormatter(format)
logger.addHandler(rotation_logging_handler)
