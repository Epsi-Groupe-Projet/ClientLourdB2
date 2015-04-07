# -*- coding: utf8 -*-

from Fenetre import *
from Initialisation import *
import os
from string import replace

def AjoutDescritpionEtPremierFrame(titre_fenetre,description_fenetre):

	# Ajout du commentaire
	stringFenetre = description_fenetre 
	stringFenetre = stringFenetre + "\n\n" + "Frame"+titre_fenetre+" = ['Frame','"+titre_fenetre+"',None,2,GROOVE,5,5,LEFT]\n"
	stringFenetre = stringFenetre + "Fenetre"+titre_fenetre+" = [Frame"+titre_fenetre+"]\n\n"

	return stringFenetre


def AjoutFenetre(stringFenetre):
	fichier = open("Test.py",'r')
	contenu_fichier = fichier.read().decode('utf8')
	fichier.close()

	contenu_fichier_modifie = contenu_fichier + "\n\n" + stringFenetre

	fichier = open("Test.py","w")
	fichier.write(contenu_fichier_modifie.encode('utf8'))
	fichier.close()


connexion = start()

fenetre = Fenetre('GestionDeFenetre',connexion,None)
fenetre.AfficherFenetre()

# Boucle
boucle = 1

while boucle:

	if fenetre.GetTitre() == "FenetreCreationDeFenetre":
		resultat = fenetre.GetDicoResult()
		resultat_forme = resultat["listResultEntry"]
		titre_fenetre = resultat_forme[0].get()
		# Suppression des espaces
		titre_fenetre = titre_fenetre.replace(" ","")
		description_fenetre = resultat_forme[1].get()

		InsertionDescription(titre_fenetre,description_fenetre)

		while 1:
			fenetre = Fenetre(fenetre.GetNextFenetre(),connexion,ResultatPrecedent)
			fenetre.AfficherFenetre()

			resultat = fenetre.GetDicoResult()
			resultat_forme = resultat["listResultEntry"]
			type_element = resultat_forme[0].get()
			
			fenetre = Fenetre(type_element,connexion,ResultatPrecedent)
			fenetre.AfficherFenetre()

			if type_element == "Frame":
				resultat = fenetre.GetDicoResult()
				resultat_forme = resultat["listResultEntry"]
				nom_frame = resultat_forme[0].get()
				nom_frame_parent = resultat_forme[1].get()
				positionement_frame = resultat_forme[3].get()

			if type_element == "Label":
				resultat = fenetre.GetDicoResult()
				resultat_forme = resultat["listResultEntry"]
				nom_label = resultat_forme[0].get()
				nom_frame_parent = resultat_forme[1].get()
				positionement_frame = resultat_forme[3].get()

			if type_element == "entry":
				resultat = fenetre.GetDicoResult()
				resultat_forme = resultat["listResultEntry"]




	ResultatPrecedent = fenetre.GetDicoResult()

	fenetre = Fenetre(fenetre.GetNextFenetre(),connexion,ResultatPrecedent)
	fenetre.AfficherFenetre()