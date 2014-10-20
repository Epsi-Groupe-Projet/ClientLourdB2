import unittest
import Employe
import Ville
import Parametre
import MysqlDef
import ConnexionMysql

# Test de la classe Employe
class TestClasseEmploye(unittest.TestCase):

	def setUp(self):
    	#Initialisation des tests
		self.villeEmploye = Ville.Ville('1','Marseille')
		self.employeATester = Employe.Employe(None,'Yassine','Faris','1992-12-21','2500.5','19 rue Solle','','33200',self.villeEmploye,'0663362470','yass-faris@hotmail.fr','FAIL','Chef de service Informatique','2','1')

	# Test de la recuperation de l'id de l'employe
	def test_GetIdEmploye(self):
		self.assertEqual(self.employeATester.GetIdEmploye(),None)

	# Test de la recuperation du nom de l'employe
	def test_GetNomEmploye(self):
		self.assertEqual(self.employeATester.GetNomEmploye(),'Faris')

	# Test de la modification du nom de l'employe
	def test_SetNomEmploye(self):
		self.employeATester.SetNomEmploye('Faris2')
		self.assertEqual(self.employeATester.GetNomEmploye(),'Faris2')

	# Test de la recuperation du prenom de l'employe
	def test_GetPrenomEmploye(self):
		self.assertEqual(self.employeATester.GetPrenomEmploye(),'Yassine')

	# Test de la modification du prenom de l'employe
	def test_SetPrenomEmploye(self):
		self.employeATester.SetPrenomEmploye('Yassine2')
		self.assertEqual(self.employeATester.GetPrenomEmploye(),'Yassine2')

	# Test de la recuperation de la date d'embauche de l'employe
	def test_GetDateEmbaucheEmploye(self):
		self.assertEqual(self.employeATester.GetDateEmbaucheEmploye(),'1992-12-21')

	# Test de la modification de la date d'embauche de l'employe
	def test_SetDateEmbaucheEmploye(self):
		self.employeATester.SetDateEmbaucheEmploye('1992-12-22')
		self.assertEqual(self.employeATester.GetDateEmbaucheEmploye(),'1992-12-22')

	# Test de la recuperation du salaire de l'employe
	def test_GetSalaireEmploye(self):
		self.assertEqual(self.employeATester.GetSalaireEmploye(),'2500.5')

	# Test de la modification du salaire de l'employe
	def test_SetSalaireEmploye(self):
		self.employeATester.SetSalaireEmploye('2500')
		self.assertEqual(self.employeATester.GetSalaireEmploye(),'2500')

	# Test de la recuperation de la l1 adresse de l'employe
	def test_GetAdresseL1Employe(self):
		self.assertEqual(self.employeATester.GetAdresseL1Employe(),'19 rue Solle')

	# Test de la modification de la l1 adresse de l'employe
	def test_SetAdresseL1Employe(self):
		self.employeATester.SetAdresseL1Employe('18 rue Solle')
		self.assertEqual(self.employeATester.GetAdresseL1Employe(),'18 rue Solle')

	# Test de la recuperation de la l2 adresse de l'employe
	def test_GetAdresseL2Employe(self):
		self.assertEqual(self.employeATester.GetAdresseL2Employe(),'')

	# Test de la modification de la l2 adresse de l'employe
	def test_SetAdresseL2Employe(self):
		self.employeATester.SetAdresseL2Employe('L2 adresse')
		self.assertEqual(self.employeATester.GetAdresseL2Employe(),'L2 adresse')

	# Test de la recuperation du cp de l'employe
	def test_GetCPEmploye(self):
		self.assertEqual(self.employeATester.GetCPEmploye(),'33200')

	# Test de la modification du cp de l'employe
	def test_SetCPEmploye(self):
		self.employeATester.SetCPEmploye('33000')
		self.assertEqual(self.employeATester.GetCPEmploye(),'33000')

	# Test de la recuperation de l'identifiant de la ville de l'employe
	def test_GetVilleEmploye(self):
		self.assertEqual(self.employeATester.GetVilleEmploye(),self.villeEmploye)

	# Test de la modification de l'identifiant de la ville  de l'employe
	def test_SetVilleEmploye(self):
		self.employeATester.SetVilleEmploye(self.villeEmploye)
		self.assertEqual(self.employeATester.GetVilleEmploye(),self.villeEmploye)

		# Test de la recuperation du telephone de l'employe
	def test_GetTelephoneEmploye(self):
		self.assertEqual(self.employeATester.GetTelephoneEmploye(),'0663362470')

	# Test de la modification du telephone  de l'employe
	def test_SetTelephoneEmploye(self):
		self.employeATester.SetTelephoneEmploye('0663362471')
		self.assertEqual(self.employeATester.GetTelephoneEmploye(),'0663362471')

	# Test de la recuperation de l'email de l'employe
	def test_GetEmailEmploye(self):
		self.assertEqual(self.employeATester.GetEmailEmploye(),'yass-faris@hotmail.fr')

	# Test de la modification de l'email de l'employe
	def test_SetEmailEmploye(self):
		self.employeATester.SetEmailEmploye('yass-faris@hotmail.com')
		self.assertEqual(self.employeATester.GetEmailEmploye(),'yass-faris@hotmail.com')

	# Test de la recuperation du commentaire de l'employe
	def test_GetCommentaireEmploye(self):
		self.assertEqual(self.employeATester.GetCommentaireEmploye(),'FAIL')

	# Test de la modification du commentaire de l'employe
	def test_SetCommentaireEmploye(self):
		self.employeATester.SetCommentaireEmploye('FAILS')
		self.assertEqual(self.employeATester.GetCommentaireEmploye(),'FAILS')

	# Test de la recuperation du poste de l'employe
	def test_GetPosteEmploye(self):
		self.assertEqual(self.employeATester.GetPosteEmploye(),'Chef de service Informatique')

	# Test de la modification du poste de l'employe
	def test_SetPosteEmploye(self):
		self.employeATester.SetPosteEmploye('Chef du departement Informatique')
		self.assertEqual(self.employeATester.GetPosteEmploye(),'Chef du departement Informatique')

	# Test de la recuperation de l'identifiant du grade de l'employe
	def test_GetIdGradeEmploye(self):
		self.assertEqual(self.employeATester.GetIdGradeEmploye(),'2')

	# Test de la modification de l'identifiant du grade de l'employe
	def test_SetPosteEmploye(self):
		self.employeATester.SetIdGradeEmploye('3')
		self.assertEqual(self.employeATester.GetIdGradeEmploye(),'3')

	# Test de la recuperation de l'identifiant du service de l'employe
	def test_GetIdServiceEmploye(self):
		self.assertEqual(self.employeATester.GetIdServiceEmploye(),'1')

	# Test de la modification de l'identifiant du service de l'employe
	def test_SetIdServiceEmploye(self):
		self.employeATester.SetIdServiceEmploye('6')
		self.assertEqual(self.employeATester.GetIdServiceEmploye(),'6')

	# Test qui verifie le fonction de la methode EmployerIntoTable et d'une nouvelle insertion
	def test_EmployerIntoTableNouveau(self):
		connexion = ConnexionMysql.ConnexionServeur(Parametre.host,Parametre.user,Parametre.passwd)
		requete = '''CREATE DATABASE testDb'''
		MysqlDef.executeRequete(connexion,requete)
		connexion.ConnexionBd("testDb")
		for nameTable in Parametre.dico.keys():
			MysqlDef.existanceTable(connexion,nameTable,Parametre.dico[nameTable])

		self.employeATester.EmployerIntoTable(connexion)
		requete = '''SELECT prenom_employe FROM `employe` '''
		result = MysqlDef.executeRequete(connexion,requete)
		# s'attend a ce que les deux elements soient gaux. Sinon
	    # le test echoue.
		self.assertEqual(result.fetchall()[0][0],self.employeATester.GetPrenomEmploye())

		# Suppresion de la db test
		requete = '''DROP DATABASE testDb'''
		MysqlDef.executeRequete(connexion,requete)

	# Test qui verifie la modification d'une entrer en base
	def test_EmployerIntoTableExistant(self):
		connexion = ConnexionMysql.ConnexionServeur(Parametre.host,Parametre.user,Parametre.passwd)
		requete = '''CREATE DATABASE testDb'''
		MysqlDef.executeRequete(connexion,requete)
		connexion.ConnexionBd("testDb")
		for nameTable in Parametre.dico.keys():
			MysqlDef.existanceTable(connexion,nameTable,Parametre.dico[nameTable])

		self.employeATester.EmployerIntoTable(connexion)
		self.employeATester.SetNomEmploye('Fares')
		self.employeATester.EmployerIntoTable(connexion)
		requete = '''SELECT nom_employe FROM `employe` '''
		result = MysqlDef.executeRequete(connexion,requete)
		# s'attend a ce que les deux elements soient gaux. Sinon
	    # le test echoue.
		self.assertEqual(result.fetchall()[0][0],self.employeATester.GetNomEmploye())

		# Suppresion de la db test
		requete = '''DROP DATABASE testDb'''
		MysqlDef.executeRequete(connexion,requete)




# Ceci lance le test si on execute le script
# directement.
if __name__ == '__main__':
    unittest.main()


