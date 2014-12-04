from ConnexionMysql import *
import Parametre

def Connection(resultats):
	resultat = resultats['listResultEntry']
	connexion = ConnexionServeur(Parametre.host,resultat[0].get(),resultat[1].get())
	if connexion.GetConnexion != None:
		return connexion
	else:
		return False

def FonctionQuiFoutRien(resultat):
	return None