import MysqlDef
import Ville
import Grade
import Service

class Employe():
	def __init__(self,pid_employe,pprenom_employe,pnom_employe,pdate_embauche_employe,psalaire_employe,padresse_l1_employe,padresse_l2_employe,pcp_employe,pville_employe,ptelephone_employe,pemail_employe,pcommentaire_employe,pposte_employe,	pgrade_employe, pservice_employe):
		self.mid_employe = pid_employe
		self.mprenom_employe = pprenom_employe
		self.mnom_employe = pnom_employe
		self.mdate_embauche_employe = pdate_embauche_employe
		self.msalaire_employe = psalaire_employe
		self.madresse_l1_employe = padresse_l1_employe
		self.madresse_l2_employe = padresse_l2_employe
		self.mcp_employe = pcp_employe
		self.mville_employe = pville_employe
		self.mtelephone_employe = ptelephone_employe
		self.memail_employe = pemail_employe
		self.mcommentaire_employe = pcommentaire_employe
		self.mposte_employe = pposte_employe
		self.mgrade_employe = pgrade_employe
		self.mservice_employe = pservice_employe


	# Methode pour recuper l'id de l'employe
	def GetIdEmploye(self):
		return self.mid_employe

	# Procedure pour modifier l'id de l'employe mise en commentaire
	#def SetIdEmploye(self, pid_employe):
	#	self.mid_employe = pid_employe

	# Methode pour recuper le nom de l'employe
	def GetNomEmploye(self):
		return self.mnom_employe

	# Procedure pour modifier le nom de l'employe
	def SetNomEmploye(self,pnom_employe):
		self.mnom_employe = pnom_employe

	# Methode pour recuper le prenom de l'employe
	def GetPrenomEmploye(self):
		return self.mprenom_employe

	# Procedure pour modifier le prenom de l'employe
	def SetPrenomEmploye(self, pprenom_employe):
		self.mprenom_employe = pprenom_employe

	# Methode pour recuper la Date Embauche de l'employe
	def GetDateEmbaucheEmploye(self):
		return self.mdate_embauche_employe

	# Procedure pour modifier la Date Embauche de l'employe
	def SetDateEmbaucheEmploye(self, pdate_embauche_employe):
		self.mdate_embauche_employe = pdate_embauche_employe

	# Methode pour recuper le salaire de l'employe
	def GetSalaireEmploye(self):
		return self.msalaire_employe

	# Procedure pour modifier le salaire de l'employe
	def SetSalaireEmploye(self, psalaire_employe):
		self.msalaire_employe = psalaire_employe

	# Methode pour recuper l'adresse L1 de l'employe
	def GetAdresseL1Employe(self):
		return self.madresse_l1_employe

	# Procedure pour modifier l'adresse L 1 de l'employe
	def SetAdresseL1Employe(self, padresse_l1_employe):
		self.madresse_l1_employe = padresse_l1_employe

	# Methode pour recuper l'adresse L2 de l'employe
	def GetAdresseL2Employe(self):
		return self.madresse_l2_employe

	# Procedure pour modifier l'adresse L 2 de l'employe
	def SetAdresseL2Employe(self, padresse_l2_employe):
		self.madresse_l2_employe = padresse_l2_employe

	# Methode pour recuper l'adresse Le code postal de l'employe
	def GetCPEmploye(self):
		return self.mcp_employe

	# Procedure pour modifier l'adresse Le code postal de l'employe
	def SetCPEmploye(self, pcp_employe):
		self.mcp_employe = pcp_employe

	# Methode pour recuper l'identifiant de la ville de l'employe
	def GetVilleEmploye(self):
		return self.mville_employe
	# Procedure pour modifier l'identifiant de la ville de l'employe
	def SetVilleEmploye(self, pville_employe):
		self.mville_employe = pville_employe

	# Methode pour recuper le telephone  de l'employe
	def GetTelephoneEmploye(self):
		return self.mtelephone_employe

	# Procedure pour modifier le telephone de l'employe
	def SetTelephoneEmploye(self, ptelephone_employe):
		self.mtelephone_employe = ptelephone_employe

	# Methode pour recuper l'email  de l'employe
	def GetEmailEmploye(self):
		return self.memail_employe

	# Procedure pour modifier l'email de l'employe
	def SetEmailEmploye(self, pemail_employe):
		self.memail_employe = pemail_employe

	# Methode pour recuper le commentaire  de l'employe
	def GetCommentaireEmploye(self):
		return self.mcommentaire_employe

	# Procedure pour modifier le commentaire de l'employe
	def SetCommentaireEmploye(self, pcommentaire_employe):
		self.mcommentaire_employe = pcommentaire_employe

	# Methode pour recuper le poste  de l'employe
	def GetPosteEmploye(self):
		return self.mposte_employe

	# Procedure pour modifier le poste de l'employe
	def SetPosteEmploye(self, pposte_employe):
		self.mposte_employe = pposte_employe

	# Methode pour recuper le grade  de l'employe
	def GetGradeEmploye(self):
		return self.mgrade_employe

	# Procedure pour modifier le grade de l'employe
	def SetGradeEmploye(self, pgrade_employe):
		self.mgrade_employe = pgrade_employe

	# Methode pour recuper le service  de l'employe
	def GetServiceEmploye(self):
		return self.mservice_employe

	# Procedure pour modifier le service de l'employe
	def SetServiceEmploye(self, pservice_employe):
		self.mservice_employe = pservice_employe

	# Methode pour ajouter ou modifier l'employer dans la table employe
	def EmployerIntoTable(self,connexion):

		# Si l'employe ne possede pas d'id cela veut dire que l'employe n'existe pas dans la table

		if self.mid_employe is None:

			# On teste si l'employe existe deja dans la table

			requete = "SELECT id_employe FROM employe WHERE nom_employe = \'"+self.mnom_employe+"\' AND prenom_employe = \'"+self.mprenom_employe+"\'"
			result = MysqlDef.executeRequete(connexion,requete)

			try:
				result[0][0] is None
			except IndexError:
				requete = "INSERT INTO employe (prenom_employe, nom_employe, date_embauche_employe,salaire_employe,adresse_l1_employe,adresse_l2_employe,cp_employe,id_ville_employe,telephone_employe,	email_employe,commentaire_employe,poste_employe,id_grade_employe,id_service_employe) VALUES (\'"+self.mprenom_employe+"\', \'"+self.mnom_employe+"\',\'"+self.mdate_embauche_employe+"\',"+self.msalaire_employe+",\'"+self.madresse_l1_employe+"\',\'"+self.madresse_l2_employe+"\',"+self.mcp_employe+","+self.mville_employe.GetIdVille()+","+self.mtelephone_employe+",\'"+self.memail_employe+"\',\'"+self.mcommentaire_employe+"\',\'"+self.mposte_employe+"\',"+self.mgrade_employe.GetIdGrade()+","+self.mservice_employe.GetIdService()+");"
				
				if MysqlDef.executeRequete(connexion,requete) == False:
					print "Insertion de l'employe: {0} {1}, a echoue".format(self.mprenom_employe, self.mnom_employe)
					return False

				else:
					print "Insertion de l'employe: {0} {1}, a reussi".format(self.mprenom_employe, self.mnom_employe)
					# Recuperation de l'id de l'employe
					requete = "SELECT id_employe FROM employe WHERE nom_employe = \'"+self.mnom_employe+"\' AND prenom_employe = \'"+self.mprenom_employe+"\'"
					result = MysqlDef.executeRequete(connexion,requete)
					self.mid_employe = str(result[0][0])
					return True
	
			else:
				print "L'employe {0} {1} existe deja dans la table ajout impossible".format(self.mprenom_employe,self.mnom_employe)
				# Recuperation de l'id de l'employe
				requete = "SELECT id_employe FROM employe WHERE nom_employe = \'"+self.mnom_employe+"\' AND prenom_employe = \'"+self.mprenom_employe+"\'"
				result = MysqlDef.executeRequete(connexion,requete)
				self.mid_employe = str(result[0][0])
				return False

		# Sinon l'employe existe deja alors on le modifie (on le supprimant d'abort puis on l'ajoutant)
		else:
			requete = "DELETE FROM employe WHERE id_employe = \'"+self.mid_employe+"\'"
			if MysqlDef.executeRequete(connexion,requete) == False:
				print "Modififcation(etape suppression) de l'employe: {0} {1}, a echoue".format(self.mprenom_employe, self.mnom_employe)
				return False

			else:
				print "Modification(etape suppression) de l'employe: {0} {1}, a reussi".format(self.mprenom_employe, self.mnom_employe)

			requete = "INSERT INTO employe (id_employe, prenom_employe, nom_employe, date_embauche_employe,salaire_employe,adresse_l1_employe,adresse_l2_employe,cp_employe,id_ville_employe,telephone_employe,	email_employe,commentaire_employe,poste_employe,id_grade_employe,id_service_employe) VALUES ("+self.mid_employe+",\'"+self.mprenom_employe+"\', \'"+self.mnom_employe+"\',\'"+self.mdate_embauche_employe+"\',"+self.msalaire_employe+",\'"+self.madresse_l1_employe+"\',\'"+self.madresse_l2_employe+"\',"+self.mcp_employe+","+self.mville_employe.GetIdVille()+","+self.mtelephone_employe+",\'"+self.memail_employe+"\',\'"+self.mcommentaire_employe+"\',\'"+self.mposte_employe+"\',"+self.mgrade_employe.GetIdGrade()+","+self.mservice_employe.GetIdService()+");"
			
			if MysqlDef.executeRequete(connexion,requete) == False:
				print "Modification(etape insertion) de l'employe: {0} {1}, a echoue".format(self.mprenom_employe, self.mnom_employe)
				return False

			else:
				print "Modification(etape insertion) de l'employe: {0} {1}, a reussi".format(self.mprenom_employe, self.mnom_employe)
				return True


	# Methode pour recuperer un employe dans la table est fournir les donnees a l'objet employe

	def GetEmployeFromTableSQL(self,connexion,plist_column_name,plist_parametre):

		if len(plist_column_name) != len(plist_parametre):
			print 'Le nombre de nom de colonne et de parametre fournit est different: Impossible de recupere l\'employe'
			return False

		else:
			# On cree la requete
			requete = "SELECT * FROM employe WHERE "
			i = 0
			while i < len(plist_column_name):
				requete = requete+plist_column_name[i]+" = \'"+plist_parametre[i]+"\' "
				if i != len(plist_column_name) -1:
					requete = requete + " AND "
				i += 1


		resultat = MysqlDef.executeRequete(connexion,requete)
		
		if resultat == False:
			print 'Requperation de l\'employe impossible'
			return False

		else:
			table = resultat
			self.mid_employe = str(table[0][0])
			self.pprenom_employe = table[0][1]
			self.pnom_employe = table[0][2]
			self.pdate_embauche_employe = str(table[0][3])
			self.psalaire_employe = str(table[0][4])
			self.madresse_l1_employe = table[0][5]
			self.madresse_l2_employe = table[0][6]
			self.mcp_employe = str(table[0][7])
			self.mtelephone_employe = str(table[0][9])
			self.memail_employe = table[0][10]
			self.mcommentaire_employe = table[0][11]
			self.mposte_employe = table[0][12]

			# Recuperation de la ville
			requeteVille = "SELECT id_ville, libelle_ville 	  FROM ville WHERE id_ville = "+str(table[0][8])
			resultatVille = MysqlDef.executeRequete(connexion,requeteVille)
			ville = Ville.Ville(resultatVille[0][0],resultatVille[0][1])

			# Recuperation du grade
			requeteGrade = "SELECT id_grade, libelle_grade FROM grade WHERE id_grade = "+str(table[0][13])
			resultatGrade = MysqlDef.executeRequete(connexion,requeteGrade)
			grade = Grade.Grade(resultatGrade[0][0],resultatGrade[0][1])

			# Recuperation du service
			requeteService = "SELECT id_service, libelle_service, id_service_service FROM service WHERE id_service = "+str(table[0][14])
			resultatService = MysqlDef.executeRequete(connexion,requeteService)
			service = Service.Service(resultatService[0][0],resultatService[0][1], resultatService[0][2])

