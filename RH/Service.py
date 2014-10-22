import MysqlDef

class Service():
	def __init__(self,pid_service,plibelle_service,pservice_service):
		self.mid_service = pid_service
		self.mlibelle_service = plibelle_service
		self.mservice_service = pservice_service

	# Accesseur Get pour l'id du service
	def GetIdService(self):
		return self.mid_service

	# Accesseur Get pour le libelle du service
	def GetLibelleService(self):
		return self.mlibelle_service

	# Accesseur Set pour le libelle du service 
	def SetLibelleService(self,plibelle_service):
		self.mlibelle_service = plibelle_service

	# Accesseur Get pour l'id du service parent
	def GetIdServiceService(self):
		return self.mlibelle_service

	# Accesseur Set pour l'id du service parent
	def SetIdServiceService(self,pservice_service):
		self.mid_service_service = pservice_service

	# Methode pour ajouter ou modifier le service dans la table service
	def ServiceIntoTable(self,connexion):

		# Si le service ne possede pas d'id cela veut dire que le service n'existe pas dans la table

		if self.mid_service is None:

			# On teste si le service existe deja dans la table

			requete = "SELECT id_service FROM service WHERE libelle_service = \'"+self.mlibelle_service+"\'"
			result = MysqlDef.executeRequete(connexion,requete)

			try:
				result[0][0] is None
			except IndexError:
				if self.mservice_service is not None:
					requete = "INSERT INTO service (libelle_service,id_service_service) VALUES (\'"+self.mlibelle_service+"\', "+self.mservice_service.GetIdService()+")"

				else:
					requete = "INSERT INTO service (libelle_service) VALUES (\'"+self.mlibelle_service+"\')"
				if MysqlDef.executeRequete(connexion,requete) == False:
					print "Insertion du service: {0}, a echoue".format(self.mlibelle_service)
					return False

				else:
					print "Insertion du service: {0}, a reussi".format(self.mlibelle_service)
					# Recuperation de l'id du service
					if self.mservice_service is not None:
						requete = "SELECT id_service FROM service WHERE libelle_service = \'"+self.mlibelle_service+"\' AND id_service_service = "+self.mservice_service.GetIdService()

					else:
						requete = "SELECT id_service FROM service WHERE libelle_service = \'"+self.mlibelle_service+"\'"

					result = MysqlDef.executeRequete(connexion,requete)
					self.mid_service = str(result[0][0])
					return True
	
			else:
				# Recuperation de l'id du service
				print "La service {0} existe deja dans la table, ajout impossible".format(self.mlibelle_service)
				result = MysqlDef.executeRequete(connexion,requete)
				self.mid_service = str(result[0][0])
				return False

		# Sinon le service existe deja alors on le modifie (on le supprimant d'abort puis on l'ajoutant)
		else:
			requete = "DELETE FROM service WHERE id_service = \'"+self.mid_service+"\' AND id_service_service = "+self.mservice_service.GetIdService()
			if MysqlDef.executeRequete(connexion,requete) == False:
				print "Modififcation(etape suppression) du service: {0}, a echoue".format(self.mlibelle_service)
				return False

			else:
				print "Modification(etape suppression) du service: {0}, a reussi".format(self.mlibelle_service)

			if self.mservice_service is not None:
				requete = "INSERT INTO service (id_service,libelle_service,id_service_service) VALUES ("+self.mid_service+",\'"+self.mlibelle_service+"\', "+self.mservice_service.GetIdService()+")"
			
			else:
				requete = "INSERT INTO service (id_service,libelle_service) VALUES ("+self.mid_service+",\'"+self.mlibelle_service+"\')"

			if MysqlDef.executeRequete(connexion,requete) == False:
				print "Modification(etape insertion) du service: {0}, a echoue".format(self.mlibelle_service)
				return False

			else:
				print "Modification(etape insertion) du service: {0}, a reussi".format(self.mlibelle_service)
				return True

	# Methode pour recuperer une service dans la table est fournir les donnees a l'objet service

	def GetServiceFromTableSQL(self,connexion,plist_column_name,plist_parametre):

		if len(plist_column_name) != len(plist_parametre):
			print 'Le nombre de nom de colonne et de parametre fournit est different: Impossible de recupere la service'
			return False

		else:
			# On cree la requete
			requete = "SELECT * FROM service WHERE "
			i = 0
			while i < len(plist_column_name):
				requete = requete+plist_column_name[i]+" = \'"+plist_parametre[i]+"\' "
				if i != len(plist_column_name) -1:
					requete = requete + " AND "
				i += 1


		resultat = MysqlDef.executeRequete(connexion,requete)
		
		if resultat == False:
			print 'Requperation de la service impossible'
			return False

		else:
			table = resultat
			self.mid_service = str(table[0][0])
			self.mlibelle_service = table[0][1]

			# Recuperation du service mere
			requeteServiceService = "SELECT id_service, libelle_service, id_service_service  FROM service WHERE id_service = "+str(table[0][2])
			resultatService = MysqlDef.executeRequete(connexion,requeteServiceService)
			self.mservice_service = Service(resultatService[0][0],resultatService[0][1],resultatService[0][2])

			print 'Recuperation du service reussi'

