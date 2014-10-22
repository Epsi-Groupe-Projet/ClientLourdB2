import MysqlDef

class Diplome_Obtenu():
	def __init__(self,pid_diplome_obtenu,pdiplome_diplome_obtenu,pemploye_diplome_obtenu):
		self.mid_diplome_obtenu = pid_diplome_obtenu
		self.mdiplome_diplome_obtenu = pdiplome_diplome_obtenu
		self.memploye_diplome_obtenu = pemploye_diplome_obtenu

	# Accesseur Get pour l'id du diplome obtenu
	def GetIdDiplomeObtenu(self):
		return self.mid_diplome_obtenu

	# Accesseur Get pour le diplome obtenu
	def GetDiplomeDiplomeObtenu(self):
		return self.mdiplome_diplome_obtenu

	# Accesseur Set pour le diplome obtenu
	def SetDiplomeDiplomeObtenu(self,pdiplome_diplome_obtenu):
		self.mdiplome_diplome_obtenu = pdiplome_diplome_obtenu

	# Accesseur Get pour l'employe du diplome obtenu
	def GetEmployeDiplomeObtenu(self):
		return self.memploye_diplome_obtenu

	# Accesseur Set pour lemploye du diplome obtenu
	def SetEmployeDiplomeObtenu(self,pemploye_diplome_obtenu):
		self.memploye_diplome_obtenu = pemploye_diplome_obtenu

	# Methode pour ajouter ou modifier le diplome dans la table diplome
	def DiplomeObtenuIntoTable(self,connexion):

		# Si le diplome obtenue ne possede pas d'id cela veut dire que l'employe ne possede pas le diplome

		if self.mid_diplome_obtenu is None:

			# On teste si le diplome obtenue existe deja dans la table

			requete = "SELECT id_diplome_obtenu FROM diplome_obtenu WHERE id_diplome_diplome_obtenu = "+self.mdiplome_diplome_obtenu.GetIdDiplome()+" AND id_employe_diplome_obtenu = "+self.memploye_diplome_obtenu.GetIdEmploye()
			result = MysqlDef.executeRequete(connexion,requete)

			try:
				result[0][0] is None
			except IndexError:

				requete = "INSERT INTO diplome_obtenu (id_diplome_diplome_obtenu,id_employe_diplome_obtenu) VALUES ("+self.mdiplome_diplome_obtenu.GetIdDiplome()+", "+self.memploye_diplome_obtenu.GetIdEmploye()+")"
				
				if MysqlDef.executeRequete(connexion,requete) == False:
					print "Insertion du diplome obtenu: {0}, pour l'employe: {1} {2} a echoue".format(self.mdiplome_diplome_obtenu.GetLibelleDiplome(),self.memploye_diplome_obtenu.GetPrenomEmploye(),self.memploye_diplome_obtenu.GetNomEmploye())
					return False

				else:
					print "Insertion du diplome obtenu: {0}, pour l'employe: {1} {2}, a reussi".format(self.mdiplome_diplome_obtenu.GetLibelleDiplome(),self.memploye_diplome_obtenu.GetPrenomEmploye(),self.memploye_diplome_obtenu.GetNomEmploye())

					# Recuperation de l'id du diplome obtenu

					requete = "SELECT id_diplome_obtenu FROM diplome_obtenu WHERE id_diplome_diplome_obtenu = "+self.mdiplome_diplome_obtenu.GetIdDiplome()+" AND id_employe_diplome_obtenu = "+self.memploye_diplome_obtenu.GetIdEmploye()

					result = MysqlDef.executeRequete(connexion,requete)
					self.mdiplome_diplome_obtenu = str(result[0][0])
					return True
	
			else:
				# Recuperation de l'id du diplome obtenu

				print "Le diplome {0} existe deja dans la table, ajout impossible".format(self.mdiplome_diplome_obtenu.GetLibelleDiplome())
				result = MysqlDef.executeRequete(connexion,requete)
				self.mid_diplome = str(result[0][0])
				return False

		# Sinon le diplome obtenu existe deja alors on le modifie (on le supprimant d'abort puis on l'ajoutant)
		else:
			requete = "DELETE FROM diplome_obtenu WHERE id_diplome_diplome_obtenu =  "+self.mdiplome_diplome_obtenu.GetIdDiplome()+" AND id_employe_diplome_obtenu = "+self.memploye_diplome_obtenu.GetIdDiplome()
			if MysqlDef.executeRequete(connexion,requete) == False:
				print "Modififcation(etape suppression) du diplome obtenu: {0}, pour l'employe: {1} {2} a echoue".format(self.mdiplome_diplome_obtenu.GetLibelleDiplome(),self.memploye_diplome_obtenu.GetPrenomEmploye(),self.memploye_diplome_obtenu.GetNomEmploye())
				return False

			else:
				print "Modification(etape suppression) du diplome obtenu: {0}, pour l'employe: {1} {2} a reussi".format(self.mdiplome_diplome_obtenu.GetLibelleDiplome(),self.memploye_diplome_obtenu.GetPrenomEmploye(),self.memploye_diplome_obtenu.GetNomEmploye())

			requete = "INSERT INTO diplome_obtenu (id_diplome_obtenu,id_diplome_diplome_obtenu,id_employe_diplome_obtenu) VALUES ("+self.mid_diplome_obtenu+","+self.mdiplome_diplome_obtenu.GetIdDiplome()+", "+self.memploye_diplome_obtenu.GetIdEmploye()+")"

			if MysqlDef.executeRequete(connexion,requete) == False:
				print "Modification(etape insertion) du diplome obtenu: {0}, pour l'employe: {1} {2} a echoue".format(self.mdiplome_diplome_obtenu.GetLibelleDiplome(),self.memploye_diplome_obtenu.GetPrenomEmploye(),self.memploye_diplome_obtenu.GetNomEmploye())
				return False

			else:
				print "Modification(etape insertion) du diplome obtenu: {0}, pour l'employe: {1} {2} a reussi".format(self.mdiplome_diplome_obtenu.GetLibelleDiplome(),self.memploye_diplome_obtenu.GetPrenomEmploye(),self.memploye_diplome_obtenu.GetNomEmploye())
				return True