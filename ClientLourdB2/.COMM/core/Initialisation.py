from MySQLdb import *
from Parametre import *
from MysqlDef import *
from ConnexionMysql import *

def start():

	# Connexion a la bd
	connexion = ConnexionServeur(host,user,passwd)
	# Test existance de la bd
	existanceBd(connexion,dbname)
	# Test existance des tables
	for nameTable in dicoTable.keys():
		existanceTable(connexion,nameTable,dicoTable[nameTable])

	return connexion

		

	    

	



    



    



	