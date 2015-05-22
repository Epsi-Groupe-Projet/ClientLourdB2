 # -*- coding: utf8 -*-

import sys
sys.path.append("../core/")
sys.path.append("../fonction/")
sys.path.append("../classe/")

import unittest
import Ville
import Parametre
import MysqlDef
import ConnexionMysql

# Test de la classe Ville
class TestClasseVille(unittest.TestCase):

	#Initialisation des tests
	def setUp(self):
		self.villeATester = Ville.Ville(None,'Paris')
    	

    # Test de la recuperation de l'id de la ville
	def test_GetIdVille(self):
		self.assertEqual(self.villeATester.GetIdVille(),None)

	# Test de la recuperation du libelle de la ville
	def test_GetLibelleVille(self):
		self.assertEqual(self.villeATester.GetLibelleVille(),'Paris')

	# Test de la modification du libelle de la ville
	def test_SetLibelleVille(self):
		self.villeATester.SetLibelleVille('Marseille')
		self.assertEqual(self.villeATester.GetLibelleVille(),'Marseille')

"""	# Test qui verifie le fonction de la methode VilleIntoTable et d'une nouvelle insertion
	def test_VilleIntoTableNouveau(self):
		connexion = ConnexionMysql.ConnexionServeur(Parametre.host,Parametre.user,Parametre.passwd)
		requete = '''CREATE DATABASE testDb'''
		MysqlDef.executeRequete(connexion,requete)
		connexion.ConnexionBd("testDb")
		for nameTable in Parametre.dicoTable.keys():
			MysqlDef.existanceTable(connexion,nameTable,Parametre.dicoTable[nameTable])

		self.villeATester.VilleIntoTable(connexion)
		requete = '''SELECT libelle_ville FROM `ville` '''
		result = MysqlDef.executeRequete(connexion,requete)
		# s'attend a ce que les deux elements soient gaux. Sinon
	    # le test echoue.
		self.assertEqual(result[0][0],self.villeATester.GetLibelleVille())

		# Suppresion de la db test
		requete = '''DROP DATABASE testDb'''
		MysqlDef.executeRequete(connexion,requete)

	# Test qui verifie la modification d'une entrer en base
	def test_VilleIntoTableExistant(self):
		connexion = ConnexionMysql.ConnexionServeur(Parametre.host,Parametre.user,Parametre.passwd)
		requete = '''CREATE DATABASE testDb'''
		MysqlDef.executeRequete(connexion,requete)
		connexion.ConnexionBd("testDb")
		for nameTable in Parametre.dicoTable.keys():
			MysqlDef.existanceTable(connexion,nameTable,Parametre.dicoTable[nameTable])

		self.villeATester.VilleIntoTable(connexion)
		self.villeATester.SetLibelleVille('Marseille')
		self.villeATester.VilleIntoTable(connexion)
		requete = '''SELECT libelle_ville FROM `ville` '''
		result = MysqlDef.executeRequete(connexion,requete)
		# s'attend a ce que les deux elements soient gaux. Sinon
	    # le test echoue.
		self.assertEqual(result[0][0],self.villeATester.GetLibelleVille())

		# Suppresion de la db test
		requete = '''DROP DATABASE testDb'''
		MysqlDef.executeRequete(connexion,requete)"""


# Ceci lance le test si on execute le script
# directement.
if __name__ == '__main__':
    unittest.main()


