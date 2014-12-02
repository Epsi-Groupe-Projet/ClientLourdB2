from Initialisation import *
from Fenetre import *

connexion = start()

fenetre = Fenetre('Connexion',connexion)

# Connexion de l'utilisateur
fenetre.AfficherFenetre()
while fenetre.GetResultatButton().GetConnexion() == None:
	fenetre = Fenetre('ErreurConnexion',connexion)
	fenetre.AfficherFenetre()
	connexion = fenetre.GetResultatButton()

fenetre = Fenetre(fenetre.GetNextFenetre(),connexion)
fenetre.AfficherFenetre()