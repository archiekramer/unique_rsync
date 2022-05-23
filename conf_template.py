
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
DEBUG = True

import logging
if DEBUG is True:
    logging.basicConfig(filename='unique_rsync.log', level=logging.DEBUG)
else:
    logging.basicConfig(filename='unique_rsync.log', level=logging.ERROR)
