import MysqlDef

class Diplome():
	def __init__(self,pid_diplome,plibelle_diplome,plevel_diplome):
		self.mid_diplome = pid_diplome
		self.mlibelle_diplome = plibelle_diplome
		self.mlevel_diplome = plevel_diplome

	# Accesseur Get pour l'id du diplome
	def GetIdDiplome(self):
		return self.mid_diplome

	# Accesseur Get pour le libelle du diplome
	def GetLibelleDiplome(self):
		return self.mlibelle_diplome

	# Accesseur Set pour le libelle du diplome 
	def SetLibelleDiplome(self,plibelle_diplome):
		self.mlibelle_diplome = plibelle_diplome

	# Accesseur Get pour le niveau du diplome
	def GetLevelDiplome(self):
		return self.mlibelle_diplome

	# Accesseur Set pour l'id du niveau du diplome
	def SetLevelDiplome(self,plevel_diplome):
		self.mlevel_diplome = plevel_diplome

	# Methode pour ajouter ou modifier le diplome dans la table diplome
	def DiplomeIntoTable(self,connexion):

		# Si la diplome ne possede pas d'id cela veut dire que le diplome n'existe pas dans la table

		if self.mid_diplome is None:

			# On teste si la diplome existe deja dans la table

			requete = "SELECT id_diplome FROM diplome WHERE libelle_diplome = \'"+self.mlibelle_diplome+"\'"
			result = MysqlDef.executeRequete(connexion,requete)

			try:
				result[0][0] is None
			except IndexError:
				if self.mlevel_diplome is not None:
					requete = "INSERT INTO diplome (libelle_diplome,level_diplome) VALUES (\'"+self.mlibelle_diplome+"\', "+self.mlevel_diplome+")"

				else:
					requete = "INSERT INTO diplome (libelle_diplome) VALUES (\'"+self.mlibelle_diplome+"\')"
				if MysqlDef.executeRequete(connexion,requete) == False:
					print "Insertion du diplome: {0}, a echoue".format(self.mlibelle_diplome)
					return False

				else:
					print "Insertion du diplome: {0}, a reussi".format(self.mlibelle_diplome)
					# Recuperation de l'id du diplome
					if self.mlevel_diplome is not None:
						requete = "SELECT id_diplome FROM diplome WHERE libelle_diplome = \'"+self.mlibelle_diplome+"\' AND level_diplome = "+self.mlevel_diplome

					else:
						requete = "SELECT id_diplome FROM diplome WHERE libelle_diplome = \'"+self.mlibelle_diplome+"\'"

					result = MysqlDef.executeRequete(connexion,requete)
					self.mid_diplome = str(result[0][0])
					return True
	
			else:
				# Recuperation de l'id du diplome
				print "Le diplome {0} existe deja dans la table, ajout impossible".format(self.mlibelle_diplome)
				result = MysqlDef.executeRequete(connexion,requete)
				self.mid_diplome = str(result[0][0])
				return False

		# Sinon le diplome existe deja alors on le modifie (on le supprimant d'abort puis on l'ajoutant)
		else:
			requete = "DELETE FROM diplome WHERE id_diplome = \'"+self.mid_diplome+"\' AND level_diplome = "+self.mlevel_diplome
			if MysqlDef.executeRequete(connexion,requete) == False:
				print "Modififcation(etape suppression) du diplome: {0}, a echoue".format(self.mlibelle_diplome)
				return False

			else:
				print "Modification(etape suppression) du diplome: {0}, a reussi".format(self.mlibelle_diplome)

			if self.mlevel_diplome is not None:
				requete = "INSERT INTO diplome (id_diplome,libelle_diplome,level_diplome) VALUES ("+self.mid_diplome+",\'"+self.mlibelle_diplome+"\', "+self.mlevel_diplome+")"
			
			else:
				requete = "INSERT INTO diplome (id_diplome,libelle_diplome) VALUES ("+self.mid_diplome+",\'"+self.mlibelle_diplome+"\')"

			if MysqlDef.executeRequete(connexion,requete) == False:
				print "Modification(etape insertion) du diplome: {0}, a echoue".format(self.mlibelle_diplome)
				return False

			else:
				print "Modification(etape insertion) du diplome: {0}, a reussi".format(self.mlibelle_diplome)
				return True