import MySQLdb
import Parametre
import MysqlDef
import ConnexionMysql

def start():

	# Connexion a la bd

	connexion = ConnexionMysql.ConnexionServeur(Parametre.host,Parametre.user,Parametre.passwd)

	# Test si la base de donne existe

	try: 
		requete = "SHOW DATABASES LIKE '"+Parametre.dbname+"' ;"
		result = MysqlDef.executeRequete(connexion.GetConnexion(),requete)

		# Creation de la base sinon

		if not result.fetchall() :

			#suivi

			print "La Base de donnee suivante est inexistante : "+Parametre.dbname
			requete = "CREATE DATABASE "+Parametre.dbname+";"
			MysqlDef.executeRequete(connexion.GetConnexion(),requete)

			#suivi

			print "La Base de donnee suivante a etait cree : "+Parametre.dbname
			connexion.ConnexionBd(Parametre.dbname)
		else:
			print "La Base de donnee suivante existe deja : "+Parametre.dbname
			connexion.ConnexionBd(Parametre.dbname)

	except MySQLdb.OperationalError,message: 

		print "Erreur : {0}".format(message)

	return connexion

		

	    

	



    



    



	