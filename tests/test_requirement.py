import sys, os, mysql.connector, logging, json


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


INFO_CONNEXION_BDD_TEST_2 = {"username" : "archiekramer",
               "mdp" : "q41jum90",
               "database" : "history_sync_test_2"}


INFO_CONNEXION_BDD_TEST = {"username" : "archiekramer",
               "mdp" : "q41jum90",
               "database" : "history_sync_test"}

INFO_CONNEXION_SCP_TEST = {
    "host" : "127.0.0.1",
    "login": os.getlogin()
}

ORIGIN_DIRECTORY_TEST = os.path.abspath(os.path.join(os.path.dirname(__file__), 'test_file/'))
DESTINATION_REPERTOIRE_TEST = os.path.abspath(os.path.join(os.path.dirname(__file__), 'test_file_destination/'))

def charge_json_data(): 
    json_string = None
    with open('tests/sql_dump_test/json_data.json', 'r') as outfile:
        json_string = json.load(outfile)
    return json_string




def set_up_bdd_test_avec_fichier(info_bdd):
    connection = mysql.connector.connect (host='localhost',
                                        user= info_bdd["username"],
                                        password=info_bdd["mdp"])
    try: 
        cursor = connection.cursor()
        with open("tests/sql_dump_test/drop_base_test.sql", 'r') as dump_sql1:
            cursor.execute(dump_sql1.read().format(database = info_bdd["database"]))
    except mysql.connector.errors.DatabaseError : 
        logging.info("base de donnée non présente, erreur gérée")
    cursor.close()
    cursor = connection.cursor()
    with open("tests/sql_dump_test/dump_bdd.sql", 'r') as dump_sql2:
        cursor.execute(dump_sql2.read().format(database = info_bdd["database"]))
    logging.info("Init base de données ok")
    cursor.close()  
    connection.close()

def set_up_bdd_vide(info_bdd):
    connection = mysql.connector.connect (host='localhost',
                                        user= info_bdd["username"],
                                        password=info_bdd["mdp"])
    try: 
        cursor = connection.cursor()
        with open("tests/sql_dump_test/drop_base_test.sql", 'r') as dump_sql1:
            cursor.execute(dump_sql1.read().format(database = info_bdd["database"]))
    except mysql.connector.errors.DatabaseError : 
        logging.info("base de donnée non présente, erreur gérée")
    else: 
        cursor.close()
    cursor = connection.cursor()
    with open("tests/sql_dump_test/test_base.sql", 'r') as dump_sql2:
        cursor.execute(dump_sql2.read().format(database = info_bdd["database"]))
    logging.info("Init base de données ok")
    cursor.close()  
    connection.close()

def remove_bdd(info_bdd):
    connection = mysql.connector.connect (host='localhost',
                                        user= info_bdd["username"],
                                        password=info_bdd["mdp"])
    try: 
        cursor = connection.cursor()
        with open("tests/sql_dump_test/drop_base_test.sql", 'r') as dump_sql1:
            cursor.execute(dump_sql1.read().format(database = info_bdd["database"]))
    except mysql.connector.errors.DatabaseError : 
        logging.info("base de donnée non présente, erreur gérée")
    cursor.close()
    connection.close()

if __name__ == "__main__":
    remove_bdd(INFO_CONNEXION_BDD_TEST)
    set_up_bdd_vide(INFO_CONNEXION_BDD_TEST)
    print(charge_json_data())
