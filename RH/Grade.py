import MysqlDef

class Grade():
	def __init__(self,pid_grade,plibelle_grade):
		self.mid_grade = pid_grade
		self.mlibelle_grade = plibelle_grade

	# Accesseur Get pour l'id de la grade
	def GetIdGrade(self):
		return self.mid_grade

	# Accesseur Get pour le libelle de la grade
	def GetLibelleGrade(self):
		return self.mlibelle_grade

	# Accesseur Set pour le libelle de la grade 
	def SetLibelleGrade(self,plibelle_grade):
		self.mlibelle_grade = plibelle_grade

	# Methode pour ajouter ou modifier la grade dans la table grade
	def GradeIntoTable(self,connexion):

		# Si la grade ne possede pas d'id cela veut dire que la grade n'existe pas dans la table

		if self.mid_grade is None:

			# On teste si la grade existe deja dans la table

			requete = "SELECT id_grade FROM grade WHERE libelle_grade = \'"+self.mlibelle_grade+"\'"
			result = MysqlDef.executeRequete(connexion,requete)

			try:
				result[0][0] is None
			except IndexError:
				requete = "INSERT INTO grade (libelle_grade) VALUES (\'"+self.mlibelle_grade+"\')"
				
				if MysqlDef.executeRequete(connexion,requete) == False:
					print "Insertion de la grade: {0}, a echoue".format(self.mlibelle_grade)
					return False

				else:
					print "Insertion de la grade: {0}, a reussi".format(self.mlibelle_grade)
					# Recuperation de l'id de la grade
					requete = "SELECT id_grade FROM grade WHERE libelle_grade = \'"+self.mlibelle_grade+"\'"
					result = MysqlDef.executeRequete(connexion,requete)
					self.mid_grade = str(result[0][0])
					return True
	
			else:
				# Recuperation de l'id de la grade
				print "La grade {0} existe deja dans la table, ajout impossible".format(self.mlibelle_grade)
				requete = "SELECT id_grade FROM grade WHERE libelle_grade = \'"+self.mlibelle_grade+"\'"
				result = MysqlDef.executeRequete(connexion,requete)
				self.mid_grade = str(result[0][0])
				return False

		# Sinon la grade existe deja alors on le modifie (on le supprimant d'abort puis on l'ajoutant)
		else:
			requete = "DELETE FROM grade WHERE id_grade = \'"+self.mid_grade+"\'"
			if MysqlDef.executeRequete(connexion,requete) == False:
				print "Modififcation(etape suppression) de la grade: {0}, a echoue".format(self.mlibelle_grade)
				return False

			else:
				print "Modification(etape suppression) de la grade: {0}, a reussi".format(self.mlibelle_grade)

			requete = "INSERT INTO grade (id_grade,libelle_grade) VALUES ("+self.mid_grade+",\'"+self.mlibelle_grade+"\');"
			
			if MysqlDef.executeRequete(connexion,requete) == False:
				print "Modification(etape insertion) de la grade: {0}, a echoue".format(self.mlibelle_grade)
				return False

			else:
				print "Modification(etape insertion) de la grade: {0}, a reussi".format(self.mlibelle_grade)
				return True