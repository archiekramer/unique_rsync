import sys, unittest, os, mysql.connector
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import INFO_CONNEXION_BDD_TEST

connection = mysql.connector.connect (host='localhost',
                                       user= INFO_CONNEXION_BDD_TEST["username"],
                                       password=INFO_CONNEXION_BDD_TEST["mdp"])
cursor = connection.cursor()
with open("tests/sql_dump_test/test_base.sql", 'r') as dump_sql:
    cursor.execute(dump_sql.read())

cursor.close()

#TODO Ajout d'un drop database drop database {0}; apres les tests