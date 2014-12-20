from ConnexionMysql import *
import Parametre
import Service

def Connection(resultats,connexion):
	resultat = resultats['listResultEntry']
	connexion = ConnexionServeur(Parametre.host,resultat[0].get(),resultat[1].get())
	if connexion.GetConnexion != None:
		return connexion
	else:
		return False

def FonctionQuiFoutRien(resultats,connexion):
	return None


def AjouterUnDepartement(resultats,connexion):
	resultat = resultats['listResultEntry']
	unService = Service.Service(None,resultat[0].get(),None)
	unService.ServiceIntoTable(connexion)
	return True
	