from Initialisation import *
from Fenetre import *

connexion = start()

fenetre = Fenetre('Connexion',connexion,None)

# Connexion de l'utilisateur
fenetre.AfficherFenetre()
while fenetre.GetResultatButton().GetConnexion() == None:
	fenetre = Fenetre('ErreurConnexion',connexion,None)
	fenetre.AfficherFenetre()

ResultatPrecedent = fenetre.GetDicoResult()

fenetre = Fenetre(fenetre.GetNextFenetre(),connexion,ResultatPrecedent)
fenetre.AfficherFenetre()

ResultatPrecedent = fenetre.GetDicoResult()
fenetre = Fenetre(fenetre.GetNextFenetre(),connexion,ResultatPrecedent)
fenetre.AfficherFenetre()