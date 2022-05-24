import sys, unittest, os, mysql.connector

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import INFO_CONNEXION_BDD_TEST

ORIGIN_DIRECTORY = "/home/archiekramer/Mediacentre/Divers/"
BASE_NON_REPRISE = ORIGIN_DIRECTORY

def set_up_bdd_test():
    connection = mysql.connector.connect (host='localhost',
                                        user= INFO_CONNEXION_BDD_TEST["username"],
                                        password=INFO_CONNEXION_BDD_TEST["mdp"])
    try: 
        cursor = connection.cursor()
        with open("tests/sql_dump_test/drop_base_test.sql", 'r') as dump_sql1:
            cursor.execute(dump_sql1.read())
    except mysql.connector.errors.DatabaseError : 
        logging.error("erreur ici")
    cursor.close()
    cursor = connection.cursor()
    with open("tests/sql_dump_test/test_base.sql", 'r') as dump_sql2:
        cursor.execute(dump_sql2.read())
    cursor.close()  

