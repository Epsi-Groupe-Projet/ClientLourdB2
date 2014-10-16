import MySQLdb
import unittest
import MysqlDef
import Parametre
import ConnexionMysql

# Test de l'execution de la requete
class TestExecuteSQLFonctionne(unittest.TestCase):
	def test_execute_Requete(self):

		self.motTest = 'Test'
		connexion = ConnexionMysql.ConnexionServeur(Parametre.host,Parametre.user,Parametre.passwd)
		requete = '''CREATE DATABASE testDb'''
		MysqlDef.executeRequete(connexion.GetConnexion(),requete)
		connexion.ConnexionBd("testDb")

		# Creation de la table test
		requete = '''CREATE TABLE table_test (id INT  NOT NULL, name VARCHAR(50)  NOT NULL)'''
		MysqlDef.executeRequete(connexion.GetConnexion(),requete)

		# Insertio d'une donnee test
		requete = '''INSERT INTO table_test (id,name) VALUES(0,'Test')'''
		MysqlDef.executeRequete(connexion.GetConnexion(),requete)

		# Recuperation de la donne test
		requete = '''SELECT `name` FROM `table_test` '''
		result = MysqlDef.executeRequete(connexion.GetConnexion(),requete)
		# s'attend a ce que les deux elements soient gaux. Sinon
	    # le test echoue.
		self.assertEqual(result.fetchall()[0][0],self.motTest)
		requete = '''DROP TABLE table_test'''
		MysqlDef.executeRequete(connexion.GetConnexion(),requete)
		requete = '''DROP DATABASE testDb'''
		MysqlDef.executeRequete(connexion.GetConnexion(),requete)

# Ceci lance le test si on execute le script
# directement.
if __name__ == '__main__':
    unittest.main()
