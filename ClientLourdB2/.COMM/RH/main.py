 # -*- coding: utf8 -*-

import sys
sys.path.append("core/")
sys.path.append("fonction/")
sys.path.append("classe/")
from Initialisation import *
from Fenetre import *

connexion = start()

fenetre = Fenetre('Connexion',connexion,None)

# Connexion de l'utilisateur
fenetre.AfficherFenetre()
while fenetre.GetResultatButton().GetConnexion() == None:
	fenetre = Fenetre('ErreurConnexion',connexion,None)
	fenetre.AfficherFenetre()

# Boucle
boucle = 1

while boucle:
	ResultatPrecedent = fenetre.GetDicoResult()

	fenetre = Fenetre(fenetre.GetNextFenetre(),connexion,ResultatPrecedent)
	fenetre.AfficherFenetre()