import MysqlDef

class Grade():
	def __init__(self,pid_grade,plibelle_grade):
		self.mid_grade = pid_grade
		self.mlibelle_grade = plibelle_grade

	# Accesseur Get pour l'id du grade
	def GetIdGrade(self):
		return self.mid_grade

	# Accesseur Get pour le libelle du grade
	def GetLibelleGrade(self):
		return self.mlibelle_grade

	# Accesseur Set pour le libelle du grade 
	def SetLibelleGrade(self,plibelle_grade):
		self.mlibelle_grade = plibelle_grade

	# Methode pour ajouter ou modifier le grade dans la table grade
	def GradeIntoTable(self,connexion):

		# Si le grade ne possede pas d'id cela veut dire que le grade n'existe pas dans la table

		if self.mid_grade is None:

			# On teste si le grade existe deja dans la table

			requete = "SELECT id_grade FROM grade WHERE libelle_grade = \'"+self.mlibelle_grade+"\'"
			result = MysqlDef.executeRequete(connexion,requete)

			try:
				result[0][0] is None
			except IndexError:
				requete = "INSERT INTO grade (libelle_grade) VALUES (\'"+self.mlibelle_grade+"\')"
				
				if MysqlDef.executeRequete(connexion,requete) == False:
					print "Insertion du grade: {0}, a echoue".format(self.mlibelle_grade)
					return False

				else:
					print "Insertion du grade: {0}, a reussi".format(self.mlibelle_grade)
					# Recuperation de l'id du grade
					requete = "SELECT id_grade FROM grade WHERE libelle_grade = \'"+self.mlibelle_grade+"\'"
					result = MysqlDef.executeRequete(connexion,requete)
					self.mid_grade = str(result[0][0])
					return True
	
			else:
				# Recuperation de l'id du grade
				print "La grade {0} existe deja dans la table, ajout impossible".format(self.mlibelle_grade)
				requete = "SELECT id_grade FROM grade WHERE libelle_grade = \'"+self.mlibelle_grade+"\'"
				result = MysqlDef.executeRequete(connexion,requete)
				self.mid_grade = str(result[0][0])
				return False

		# Sinon le grade existe deja alors on le modifie (on le supprimant d'abort puis on l'ajoutant)
		else:
			requete = "DELETE FROM grade WHERE id_grade = \'"+self.mid_grade+"\'"
			if MysqlDef.executeRequete(connexion,requete) == False:
				print "Modififcation(etape suppression) du grade: {0}, a echoue".format(self.mlibelle_grade)
				return False

			else:
				print "Modification(etape suppression) du grade: {0}, a reussi".format(self.mlibelle_grade)

			requete = "INSERT INTO grade (id_grade,libelle_grade) VALUES ("+self.mid_grade+",\'"+self.mlibelle_grade+"\');"
			
			if MysqlDef.executeRequete(connexion,requete) == False:
				print "Modification(etape insertion) du grade: {0}, a echoue".format(self.mlibelle_grade)
				return False

			else:
				print "Modification(etape insertion) du grade: {0}, a reussi".format(self.mlibelle_grade)
				return True

	# Methode pour recuperer un grade dans la table est fournir les donnees a l'objet grade

	def GetGradeFromTableSQL(self,connexion,plist_column_name,plist_parametre):

		if len(plist_column_name) != len(plist_parametre):
			print 'Le nombre de nom de colonne et de parametre fournit est different: Impossible de recupere le grade'
			return False

		else:
			# On cree la requete
			requete = "SELECT * FROM grade WHERE "
			i = 0
			while i < len(plist_column_name):
				requete = requete+plist_column_name[i]+" = \'"+plist_parametre[i]+"\' "
				if i != len(plist_column_name) -1:
					requete = requete + " AND "
				i += 1


		resultat = MysqlDef.executeRequete(connexion,requete)
		
		if resultat == False:
			print 'Requperation du grade impossible'
			return False

		else:
			table = resultat
			self.mid_grade = str(table[0][0])
			self.mlibelle_grade = table[0][1]

			print 'Recuperation du grade reussi'