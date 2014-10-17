import MySQLdb
import Parametre
import MysqlDef
import ConnexionMysql

def start():

	# Connexion a la bd
	connexion = ConnexionMysql.ConnexionServeur(Parametre.host,Parametre.user,Parametre.passwd)
	# Test existance de la bd
	MysqlDef.existanceBd(connexion,Parametre.dbname)
	# Test existance des tables
	for nameTable in Parametre.dico.keys():
		MysqlDef.existanceTable(connexion,nameTable,Parametre.dico[nameTable])

	return connexion

		

	    

	



    



    



	