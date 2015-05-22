# -*- coding: utf8 -*-

from Fenetre import *
from Initialisation import *
import os
from string import replace

def CreationDescriptionEtFrame1(titre_fenetre,description_fenetre):

	# Ajout du commentaire
	stringFenetre = "# "+description_fenetre 
	stringFenetre = stringFenetre + "\n\n" + "Frame"+titre_fenetre+" = ['Frame','"+titre_fenetre+"',None,2,GROOVE,5,5,LEFT]\n"
	stringFenetre = stringFenetre + "Fenetre"+titre_fenetre+" = [Frame"+titre_fenetre+"]\n"

	return stringFenetre

def CreationFrame(nom_frame,nom_frame_parent,positionement_frame,titre_fenetre):
	stringFenetre = "Frame"+nom_frame+" = ['Frame','"+nom_frame+"',"+nom_frame_parent+",2,GROOVE,5,5,"+positionement_frame+"]\n"
	stringFenetre = stringFenetre + "Fenetre"+titre_fenetre+".append(Frame"+nom_frame+")\n"

	return stringFenetre

def CreationLabel(nom_label,nom_frame_parent,text_label,positionement_Label,titre_fenetre):
	stringFenetre = "Label"+nom_label+" = ['Label','"+nom_label+"','"+nom_frame_parent+"','"+text_label+"',"+positionement_Label+",5,5]\n"
	stringFenetre = stringFenetre + "Fenetre"+titre_fenetre+".append(Label"+nom_label+")\n"

	return stringFenetre

def CreationEntry(nom_entry,nom_frame_parent,carac_remplacement,positionement_entry,hateur,largeur,titre_fenetre):
	stringFenetre = "Entry"+nom_entry+" = ['Entry','"+nom_entry+"','"+nom_frame_parent+"',"+carac_remplacement+","+positionement_entry+","+hateur+","+largeur+"]\n"
	stringFenetre = stringFenetre + "Fenetre"+titre_fenetre+".append(Entry"+nom_entry+")\n"

	return stringFenetre

def CreationImage(nom_image, nom_frame_parent, chemin_image, titre_fenetre):
	stringFenetre = "Image"+nom_image+" = ['Image','"+nom_image+"','"+nom_frame_parent+"','"+chemin_image+"']\n"
	stringFenetre = stringFenetre + "Fenetre"+titre_fenetre+".append(Image"+nom_image+")\n"

	return stringFenetre

def CreationButton(nom_button, nom_frame_parent, text_button, nom_fonction,positionement_button, next_fenetre, titre_fenetre):
	stringFenetre = "Button"+nom_button+" = ['Button','"+nom_button+"','"+nom_frame_parent+"','"+text_button+"',"+nom_fonction+","+positionement_button+",5,5,'"+next_fenetre+"']\n"
	stringFenetre = stringFenetre + "Fenetre"+titre_fenetre+".append(Button"+nom_button+")\n"

	return stringFenetre

def InitialisationFonction(nom_fonction):
	fichier = open("Function.py",'r')
	contenu_fichier = fichier.read()
	fichier.close()

	stringFonction = "# Fonction "+nom_fonction+" à créer.\n"
	stringFonction = stringFonction + "def "+nom_fonction+"(resultats,connexion):\n"
	stringFonction = stringFonction + '	""" A remplir """\n'
	stringFonction = stringFonction + "	return True\n"

	contenu_fichier_modifie = contenu_fichier + "\n\n" + stringFonction

	fichier = open("Function.py","w")
	fichier.write(contenu_fichier_modifie)
	fichier.close()

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

		stringFenetre = CreationDescriptionEtFrame1(titre_fenetre,description_fenetre)
		AjoutFenetre(stringFenetre)

		while 1:
			fenetre = Fenetre(fenetre.GetNextFenetre(),connexion,ResultatPrecedent)
			fenetre.AfficherFenetre()

			resultat = fenetre.GetDicoResult()
			resultat_forme = resultat["listResultEntry"]
			type_element = resultat_forme[0].get()
			print type_element
			
			fenetre = Fenetre(type_element,connexion,ResultatPrecedent)
			fenetre.AfficherFenetre()

			if type_element == "Frame":
				resultat = fenetre.GetDicoResult()
				resultat_forme = resultat["listResultEntry"]
				nom_frame = resultat_forme[0].get()
				nom_frame_parent = resultat_forme[1].get()
				positionement_frame = resultat_forme[2].get()

				if nom_frame_parent != None:
					nom_frame_parent = "'"+nom_frame_parent+"'"

				stringFenetre = CreationFrame(nom_frame,nom_frame_parent,positionement_frame,titre_fenetre)
				AjoutFenetre(stringFenetre)

			if type_element == "Label":
				resultat = fenetre.GetDicoResult()
				resultat_forme = resultat["listResultEntry"]
				nom_label = resultat_forme[0].get()
				nom_frame_parent = resultat_forme[1].get()
				text_label = resultat_forme[2].get()
				positionement_Label = resultat_forme[3].get()

				stringFenetre = CreationLabel(nom_label,nom_frame_parent,text_label,positionement_Label,titre_fenetre)
				AjoutFenetre(stringFenetre)

			if type_element == "Entry":
				resultat = fenetre.GetDicoResult()
				resultat_forme = resultat["listResultEntry"]
				nom_entry = resultat_forme[0].get()
				nom_frame_parent = resultat_forme[1].get()
				carac_remplacement = resultat_forme[2].get()
				positionement_entry = resultat_forme[3].get()
				hateur = resultat_forme[4].get()
				largeur = resultat_forme[5].get()

				if carac_remplacement != None:
					carac_remplacement = "'"+carac_remplacement+"'"

				stringFenetre = CreationEntry(nom_entry,nom_frame_parent,carac_remplacement,positionement_entry,hateur,largeur,titre_fenetre)
				AjoutFenetre(stringFenetre)

			if type_element == "Image":
				resultat = fenetre.GetDicoResult()
				resultat_forme = resultat["listResultEntry"]
				nom_image = resultat_forme[0].get()
				nom_frame_parent = resultat_forme[1].get()
				chemin_image = resultat_forme[2].get()

				stringFenetre = CreationImage(nom_image, nom_frame_parent, chemin_image, titre_fenetre)
				AjoutFenetre(stringFenetre)

			if type_element == "Button":
				resultat = fenetre.GetDicoResult()
				resultat_forme = resultat["listResultEntry"]
				nom_button = resultat_forme[0].get()
				nom_frame_parent = resultat_forme[1].get()
				text_button = resultat_forme[2].get()
				nom_fonction = resultat_forme[3].get()
				positionement_button = resultat_forme[4].get()
				next_fenetre = resultat_forme[5].get()

				stringFenetre = CreationButton(nom_button, nom_frame_parent, text_button, nom_fonction,positionement_button, next_fenetre, titre_fenetre)
				AjoutFenetre(stringFenetre)
				InitialisationFonction(nom_fonction)

			if type_element == "ListeDynamiqueButton":
				resultat = fenetre.GetDicoResult()
				resultat_forme = resultat["listResultEntry"]
				nom_ListeDynamiqueButton = resultat_forme[0].get()
				nom_frame_parent = resultat_forme[1].get()
				nom_colonne = resultat_forme[2].get()
				nom_table = resultat_forme[3].get()
				valeur = resultat_forme[4].get()
				next_fenetre = resultat_forme[5].get()
				
				stringFenetre = CreationListeDynamiqueButton(nom_ListeDynamiqueButton,nom_frame_parent,nom_colonne,nom_table,valeur,next_fenetre,titre_fenetre)
				AjoutFenetre(stringFenetre)

	ResultatPrecedent = fenetre.GetDicoResult()

	fenetre = Fenetre(fenetre.GetNextFenetre(),connexion,ResultatPrecedent)
	fenetre.AfficherFenetre()