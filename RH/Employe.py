import MysqlDef

class Employe():
	def __init__(self,pid_employe,pprenom_employe,pnom_employe,pdate_embauche_employe,psalaire_employe,padresse_l1_employe,padresse_l2_employe,pcp_employe,pville_employe,ptelephone_employe,pemail_employe,pcommentaire_employe,pposte_employe,	pid_grade_employe, pid_service_employe):
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
		self.mid_grade_employe = pid_grade_employe
		self.mid_service_employe = pid_service_employe


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

	# Methode pour recuper l'identifiant du grade  de l'employe
	def GetIdGradeEmploye(self):
		return self.mid_grade_employe

	# Procedure pour modifier l'identifiant du grade de l'employe
	def SetIdGradeEmploye(self, pid_grade_employe):
		self.mid_grade_employe = pid_grade_employe

	# Methode pour recuper l'identifiant du service  de l'employe
	def GetIdServiceEmploye(self):
		return self.mid_service_employe

	# Procedure pour modifier l'identifiant du service de l'employe
	def SetIdServiceEmploye(self, pid_service_employe):
		self.mid_service_employe = pid_service_employe

	# Methode pour ajouter ou modifier l'employer dans la table employe
	def EmployerIntoTable(self,connexion):

		# Si l'employe ne possede pas d'id cela veut dire que l'employe n'existe pas dans la table

		if self.mid_employe is None:

			# On teste si l'employe existe deja dans la table

			requete = "SELECT id_employe FROM employe WHERE nom_employe = \'"+self.mnom_employe+"\' AND prenom_employe = \'"+self.mprenom_employe+"\'"
			result = MysqlDef.executeRequete(connexion,requete)

			try:
				result.fetchall()[0][0] is None
			except IndexError:
				requete = "INSERT INTO employe (prenom_employe, nom_employe, date_embauche_employe,salaire_employe,adresse_l1_employe,adresse_l2_employe,cp_employe,id_ville_employe,telephone_employe,	email_employe,commentaire_employe,poste_employe,id_grade_employe,id_service_employe) VALUES (\'"+self.mprenom_employe+"\', \'"+self.mnom_employe+"\',\'"+self.mdate_embauche_employe+"\',"+self.msalaire_employe+",\'"+self.madresse_l1_employe+"\',\'"+self.madresse_l2_employe+"\',"+self.mcp_employe+","+self.mville_employe.GetIdVille()+","+self.mtelephone_employe+",\'"+self.memail_employe+"\',\'"+self.mcommentaire_employe+"\',\'"+self.mposte_employe+"\',"+self.mid_grade_employe+","+self.mid_service_employe+");"
				
				if MysqlDef.executeRequete(connexion,requete) == False:
					print "Insertion de l'employe: {0} {1}, a echoue".format(self.mprenom_employe, self.mnom_employe)
					return False

				else:
					print "Insertion de l'employe: {0} {1}, a reussi".format(self.mprenom_employe, self.mnom_employe)
	
			else:
				print "L'employe {0} {1} existe deja dans la table ajout impossible".format(self.mprenom_employe,self.mnom_employe)
				return False


				# Recuperation de l'id de l'employe
				requete = "SELECT id_employe FROM employe WHERE nom_employe = \'"+self.mnom_employe+"\' AND prenom_employe = \'"+self.mprenom_employe+"\'"
				result = MysqlDef.executeRequete(connexion,requete)
				self.mid_employe = result.fetchall()[0][0]
				return True

		# Sinon l'employe existe deja alors on le modifie (on le supprimant d'abort puis on l'ajoutant)
		else:
			requete = "DELETE FROM employe WHERE id_employe = \'"+self.mid_employe+"\'"
			if MysqlDef.executeRequete(connexion,requete) == False:
				print "Modififcation(etape suppression) de l'employe: {0} {1}, a echoue".format(self.mprenom_employe, self.mnom_employe)
				return False

			else:
				print "Modification(etape suppression) de l'employe: {0} {1}, a reussi".format(self.mprenom_employe, self.mnom_employe)

			requete = "INSERT INTO employe (id_employe, prenom_employe, nom_employe, date_embauche_employe,salaire_employe,adresse_l1_employe,adresse_l2_employe,cp_employe,id_ville_employe,telephone_employe,	email_employe,commentaire_employe,poste_employe,id_grade_employe,id_service_employe) VALUES ("+self.mid_employe+",\'"+self.mprenom_employe+"\', \'"+self.mnom_employe+"\',\'"+self.mdate_embauche_employe+"\',"+self.msalaire_employe+",\'"+self.madresse_l1_employe+"\',\'"+self.madresse_l2_employe+"\',"+self.mcp_employe+","+self.mville_employe.GetIdVille()+","+self.mtelephone_employe+",\'"+self.memail_employe+"\',\'"+self.mcommentaire_employe+"\',\'"+self.mposte_employe+"\',"+self.mid_grade_employe+","+self.mid_service_employe+");"
			
			if MysqlDef.executeRequete(connexion,requete) == False:
				print "Modification(etape insertion) de l'employe: {0} {1}, a echoue".format(self.mprenom_employe, self.mnom_employe)
				return False

			else:
				print "Modification(etape insertion) de l'employe: {0} {1}, a reussi".format(self.mprenom_employe, self.mnom_employe)
				return True
