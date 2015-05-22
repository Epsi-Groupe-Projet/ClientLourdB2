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
		self.mdbname = None
		self.mconnexion = None

		#Connexion au serveur MYSQL
		try: 

			print "connexion..." 

			# connexion 

			self.mconnexion = MySQLdb.connect(self.mhost, self.muser, self.mpasswd) 

			# suivi 

			print "Connexion a MySQL reussie sous l'identite host={0},user={1},passwd={2}".format(self.mhost,self.muser,self.mpasswd) 

		except MySQLdb.OperationalError,message:
			self.FailConnexion()
			print "Erreur : {0}".format(message)


			

	def ConnexionBd(self,pdbname):

		self.mdbname = pdbname

		#Connexion au serveur MYSQL + base de donnee

		self.mconnexion.close()

		try: 

			print "connexion..." 

			# connexion 

			self.mconnexion = MySQLdb.connect(self.mhost, self.muser, self.mpasswd, self.mdbname) 

			# suivi 

			print "Connexion a MySQL reussie sous l'identite host={0},user={1},passwd={2}, dbname={3}".format(self.mhost,self.muser,self.mpasswd,self.mdbname) 

		except MySQLdb.OperationalError,message: 

			print "Erreur : {0}".format(message)

	def GetConnexion(self):
		return self.mconnexion

	def Close(self):
		self.mconnexion.close()

	def GetDbName(self):
		return self.mdbname

	def FailConnexion(self):
		self.mconnexion = None
		