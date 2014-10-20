import MysqlDef

class Ville():
	def __init__(self,pid_ville,plibelle_ville):
		self.mid_ville = pid_ville
		self.mlibelle_ville = plibelle_ville

	# Accesseur Get pour l'id de la ville
	def GetIdVille(self):
		return self.mid_ville

	# Accesseur Get pour le libelle de la ville
	def GetLibelleVille(self):
		return self.mlibelle_ville

	# Accesseur Set pour le libelle de la ville 
	def SetLibelleVille(self,plibelle_ville):
		self.mlibelle_ville = plibelle_ville

	# Methode pour ajouter ou modifier la ville dans la table ville
	def VilleIntoTable(self,connexion):

		# Si la ville ne possede pas d'id cela veut dire que la ville n'existe pas dans la table

		if self.mid_ville is None:

			# On teste si la ville existe deja dans la table

			requete = "SELECT id_ville FROM ville WHERE libelle_ville = \'"+self.mlibelle_ville+"\'"
			result = MysqlDef.executeRequete(connexion,requete)

			try:
				result.fetchall()[0][0] is None
			except IndexError:
				requete = "INSERT INTO ville (libelle_ville) VALUES (\'"+self.mlibelle_ville+"\')"
				
				if MysqlDef.executeRequete(connexion,requete) == False:
					print "Insertion de la ville: {0}, a echoue".format(self.mlibelle_ville)
					return False

				else:
					print "Insertion de la ville: {0}, a reussi".format(self.mlibelle_ville)
	
			else:
				print "La ville {0} existe deja dans la table, ajout impossible".format(self.mlibelle_ville)
				return False


				# Recuperation de l'id de la ville
				requete = "SELECT id_ville FROM ville WHERE libelle_ville = \'"+self.mlibelle_ville+"\'"
				result = MysqlDef.executeRequete(connexion,requete)
				self.mid_ville = result.fetchall()[0][0]
				return True

		# Sinon la ville existe deja alors on le modifie (on le supprimant d'abort puis on l'ajoutant)
		else:
			requete = "DELETE FROM ville WHERE id_ville = \'"+self.mid_ville+"\'"
			if MysqlDef.executeRequete(connexion,requete) == False:
				print "Modififcation(etape suppression) de la ville: {0}, a echoue".format(self.mlibelle_ville)
				return False

			else:
				print "Modification(etape suppression) de la ville: {0}, a reussi".format(self.mlibelle_ville)

			requete = "INSERT INTO ville (id_ville,libelle_ville) VALUES ("+self.mid_ville+",\'"+self.mlibelle_ville+"\');"
			
			if MysqlDef.executeRequete(connexion,requete) == False:
				print "Modification(etape insertion) de la ville: {0}, a echoue".format(self.mlibelle_ville)
				return False

			else:
				print "Modification(etape insertion) de la ville: {0}, a reussi".format(self.mlibelle_ville)
				return True
