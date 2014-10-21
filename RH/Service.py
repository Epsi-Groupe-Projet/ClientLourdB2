import MysqlDef

class Service():
	def __init__(self,pid_service,plibelle_service,pid_service_service):
		self.mid_service = pid_service
		self.mlibelle_service = plibelle_service
		self.mid_service_service = pid_service_service

	# Accesseur Get pour l'id de la service
	def GetIdService(self):
		return self.mid_service

	# Accesseur Get pour le libelle de la service
	def GetLibelleService(self):
		return self.mlibelle_service

	# Accesseur Set pour le libelle de la service 
	def SetLibelleService(self,plibelle_service):
		self.mlibelle_service = plibelle_service

	# Accesseur Get pour l'id du service parent
	def GetIdServiceService(self):
		return self.mlibelle_service

	# Accesseur Set pour l'id du service parent
	def SetIdServiceService(self,pid_service_service):
		self.mid_service_service = pid_service_service

	# Methode pour ajouter ou modifier la service dans la table service
	def ServiceIntoTable(self,connexion):

		# Si la service ne possede pas d'id cela veut dire que la service n'existe pas dans la table

		if self.mid_service is None:

			# On teste si la service existe deja dans la table

			requete = "SELECT id_service FROM service WHERE libelle_service = \'"+self.mlibelle_service+"\'"
			result = MysqlDef.executeRequete(connexion,requete)

			try:
				result[0][0] is None
			except IndexError:
				if self.mid_service_service is not None:
					requete = "INSERT INTO service (libelle_service,id_service_service) VALUES (\'"+self.mlibelle_service+"\', "+self.mid_service_service+")"

				else:
					requete = "INSERT INTO service (libelle_service) VALUES (\'"+self.mlibelle_service+"\')"
				if MysqlDef.executeRequete(connexion,requete) == False:
					print "Insertion de la service: {0}, a echoue".format(self.mlibelle_service)
					return False

				else:
					print "Insertion de la service: {0}, a reussi".format(self.mlibelle_service)
					# Recuperation de l'id de la service
					if self.mid_service_service is not None:
						requete = "SELECT id_service FROM service WHERE libelle_service = \'"+self.mlibelle_service+"\' AND id_service_service = "+self.mid_service_service

					else:
						requete = "SELECT id_service FROM service WHERE libelle_service = \'"+self.mlibelle_service+"\'"

					result = MysqlDef.executeRequete(connexion,requete)
					self.mid_service = str(result[0][0])
					return True
	
			else:
				# Recuperation de l'id de la service
				print "La service {0} existe deja dans la table, ajout impossible".format(self.mlibelle_service)
				result = MysqlDef.executeRequete(connexion,requete)
				self.mid_service = str(result[0][0])
				return False

		# Sinon la service existe deja alors on le modifie (on le supprimant d'abort puis on l'ajoutant)
		else:
			requete = "DELETE FROM service WHERE id_service = \'"+self.mid_service+"\' AND id_service_service = "+self.mid_service_service
			if MysqlDef.executeRequete(connexion,requete) == False:
				print "Modififcation(etape suppression) de la service: {0}, a echoue".format(self.mlibelle_service)
				return False

			else:
				print "Modification(etape suppression) de la service: {0}, a reussi".format(self.mlibelle_service)

			if self.mid_service_service is not None:
				requete = "INSERT INTO service (id_service,libelle_service,id_service_service) VALUES ("+self.mid_service+",\'"+self.mlibelle_service+"\', "+self.mid_service_service+")"
			
			else:
				requete = "INSERT INTO service (id_service,libelle_service) VALUES ("+self.mid_service+",\'"+self.mlibelle_service+"\')"

			if MysqlDef.executeRequete(connexion,requete) == False:
				print "Modification(etape insertion) de la service: {0}, a echoue".format(self.mlibelle_service)
				return False

			else:
				print "Modification(etape insertion) de la service: {0}, a reussi".format(self.mlibelle_service)
				return True