import MySQLdb
import unittest
import MysqlDef
import Parametre
import ConnexionMysql


class TestExecuteSQLFonctionne(unittest.TestCase):

	# Test de l'execution de la requete
	def test_execute_Requete(self):

		self.motTest = 'Test'
		connexion = ConnexionMysql.ConnexionServeur(Parametre.host,Parametre.user,Parametre.passwd)
		requete = '''CREATE DATABASE testDb'''
		MysqlDef.executeRequete(connexion,requete)
		connexion.ConnexionBd("testDb")

		# Creation de la table test
		requete = '''CREATE TABLE table_test (id INT  NOT NULL, name VARCHAR(50)  NOT NULL)'''
		MysqlDef.executeRequete(connexion,requete)

		# Insertio d'une donnee test
		requete = '''INSERT INTO table_test (id,name) VALUES(0,'Test')'''
		MysqlDef.executeRequete(connexion,requete)

		# Recuperation de la donne test
		requete = '''SELECT `name` FROM `table_test` '''
		result = MysqlDef.executeRequete(connexion,requete)
		# s'attend a ce que les deux elements soient gaux. Sinon
	    # le test echoue.
		self.assertEqual(result[0][0],self.motTest)

		# Suppresion de la database test
		requete = '''DROP DATABASE testDb'''
		MysqlDef.executeRequete(connexion,requete)

# Ceci lance le test si on execute le script
# directement.
if __name__ == '__main__':
    unittest.main()
