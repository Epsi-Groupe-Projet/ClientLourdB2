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
