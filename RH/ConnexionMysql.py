import MySQLdb

class ConnexionServeur():
	connexion = None
	muser = None
	mhost = None
	mpasswd = None
	mdbname = None

	# Constructeur

	def __init__(self,phost,puser,ppasswd):

		self.muser = puser
		self.mhost = phost
		self.mpasswd = ppasswd

		#Connexion au serveur MYSQL
		try: 

			print "connexion..." 

			# connexion 

			self.connexion = MySQLdb.connect(self.mhost, self.muser, self.mpasswd) 

			# suivi 

			print "Connexion a MySQL reussie sous l'identite host={0},user={1},passwd={2}".format(self.mhost,self.muser,self.mpasswd) 

		except MySQLdb.OperationalError,message: 

			print "Erreur : {0}".format(message)

	def ConnexionBd(self,pdbname):

		self.mdbname = pdbname

		#Connexion au serveur MYSQL + base de donnee

		self.connexion.close()

		try: 

			print "connexion..." 

			# connexion 

			self.connexion = MySQLdb.connect(self.mhost, self.muser, self.mpasswd, self.mdbname) 

			# suivi 

			print "Connexion a MySQL reussie sous l'identite host={0},user={1},passwd={2}, dbname={3}".format(self.mhost,self.muser,self.mpasswd,self.mdbname) 

		except MySQLdb.OperationalError,message: 

			print "Erreur : {0}".format(message)

	def GetConnexion(self):
		if self.connexion is not None:
			return self.connexion

	def Close(self):
		self.connexion.close()

	def GetDbName(self):
		return self.mdbname