# -*- coding: utf8 -*-

from Tkinter import *
from Function import *

host = 'localhost'
user = 'root'
passwd = 'root'
dbname = 'prodCOM'
backGroundColor = 'white'
fgColor = 'maroon'


dicoTable = {}

dicoFenetre = {}

# Parametre table marque
code_marque = ['code_marque','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_marque = [code_marque]

libelle_marque = ['libelle_marque','VARCHAR(50)','NOT NULL']
column_marque.append(libelle_marque)

dicoTable['marque'] = column_marque

# Parametre Table client
id_client = ['id_client','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_client = [id_client]

prenom_client = ['prenom_client','VARCHAR(50)','NOT NULL']
column_client.append(prenom_client)

nom_client = ['nom_client','VARCHAR(50)','NOT NULL']
column_client.append(nom_client)

adresse_l1_client = ['adresse_l1_client','VARCHAR(50)','NOT NULL']
column_client.append(adresse_l1_client)

adresse_l2_client = ['adresse_l2_client','VARCHAR(50)','NULL']
column_client.append(adresse_l2_client)

cp_client = ['cp_client','INT','NOT NULL']
column_client.append(cp_client)

ville_client = ['ville_client','VARCHAR(50)','NOT NULL']
column_client.append(ville_client)

telephone_client = ['telephone_client','INT','NOT NULL']
column_client.append(telephone_client)

email_client = ['email_client','VARCHAR(50)','NOT NULL']
column_client.append(email_client)

dicoTable['client'] = column_client


# Parametre table modele
code_modele = ['code_modele','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_modele = [code_modele]

libelle_modele = ['libelle_modele','VARCHAR(50)','NOT NULL']
column_modele.append(libelle_modele)

puissance_moteur_modele = ['puissance_moteur_modele','INT','NOT NULL']
column_modele.append(puissance_moteur_modele)

vitesse_modele = ['vitesse_modele','INT','NOT NULL']
column_modele.append(vitesse_modele)

code_marque_modele = ['code_marque_modele','INT','NOT NULL']
column_modele.append(code_marque_modele)

code_carburant_modele = ['code_carburant_modele','INT','NOT NULL']
column_modele.append(code_carburant_modele)

dicoTable['modele'] = column_modele

# Parametre table carburant
code_carburant = ['code_carburant','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_carburant = [code_carburant]

libelle_carburant = ['libelle_carburant','VARCHAR(50)','NOT NULL']
column_carburant.append(libelle_carburant)

dicoTable['carburant'] = column_carburant


# Parametre table option
id_option = ['id_option','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_option = [id_option]

libelle_option = ['libelle_option','VARCHAR(50)','NOT NULL']
column_option.append(libelle_option)

prix_hors_taxe_option = ['prix_hors_taxe_option','DOUBLE','NOT NULL']
column_option.append(prix_hors_taxe_option)

id_tva_option = ['id_tva_option','DOUBLE','NOT NULL']
column_option.append(id_tva_option)

dicoTable['option_voiture'] = column_option

# Parametre table voiture
numero_voiture = ['numero_voiture','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_voiture = [numero_voiture]

kilometrage_voiture = ['kilometrage_voiture','DOUBLE','NOT NULL']
column_voiture.append(kilometrage_voiture)

prix_achat_hors_taxe_voiture =['prix_achat_hors_taxe_voiture','INT','NOT NULL']
column_voiture.append(prix_achat_hors_taxe_voiture)

prix_vente_hors_taxe_voiture =['prix_vente_hors_taxe_voiture','DOUBLE','NOT NULL']
column_voiture.append(prix_vente_hors_taxe_voiture)

id_modele_voiture = ['id_modele_voiture','INT','NOT NULL']
column_voiture.append(id_modele_voiture )

id_tva_voiture = ['id_tva_voiture','INT','NOT NULL']
column_voiture.append(id_tva_voiture )

dicoTable['voiture'] = column_voiture


# Parametre table TVA
id_tva = ['id_tva','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_tva = [id_tva]

taux_tva = ['taux_tva','DOUBLE','NOT NULL']
column_tva.append(taux_tva)

date_tva = ['date_tva','DATE','NOT NULL']
column_tva.append(date_tva)

dicoTable['tva'] = column_tva

# Parametre table facture client
id_facture_client = ['id_facture_client','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_facture_client = [id_facture_client]

date_facture_client = ['date_facture_client','DATE','NOT NULL']
column_facture_client.append(date_facture_client)

date_paiement = ['date_paiement','DATE','NOT NULL']
column_facture_client.append(date_paiement)

total_ht = ['taux_tva','DOUBLE','NOT NULL']
column_facture_client.append(total_ht)

id_commande_client_facture_client = ['id_commande_client_facture_client','INT','NOT NULL']
column_facture_client.append(id_commande_client_facture_client)

dicoTable['facture_client'] = column_facture_client

# Parametre table commande client
id_commande_client = ['id_commande_client','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_commande_client = [id_commande_client]

date_commande_client = ['date_commande_client','DATE','NOT NULL']
column_commande_client.append(date_commande_client)

id_devis_client_commande = ['id_devis_client','INT','NOT NULL']
column_commande_client.append(id_devis_client_commande)

dicoTable['commande_client'] = column_commande_client

# Parametre table peinture_exterieur

id_peinture_exterieur = ['id_peinture_exterieur','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_peinture_exterieur = [id_peinture_exterieur]

libelle_peinture_exterieur = ['libelle_peinture_exterieur','VARCHAR(50)','NOT NULL']
column_peinture_exterieur.append(libelle_peinture_exterieur)

prix_peinture_exterieur_ht = ['prix_peinture_exterieur_ht','DOUBLE','NOT NULL']
column_peinture_exterieur.append(prix_peinture_exterieur_ht)

id_tva_peinture_exterieur = ['id_tva_peinture_exterieur','INT','NOT NULL']
column_peinture_exterieur.append(id_tva_peinture_exterieur)

dicoTable['peinture_exterieur'] = column_peinture_exterieur

#Parametre table devis_client

id_devis_client = ['id_devis_client','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_devis_client = [id_devis_client]

date_devis_client = ['date_devis_client','DATE','NOT NULL']
column_devis_client.append(date_devis_client)

id_peinture_devis_client = ['id_peinture_devis_client','INT','NOT NULL']
column_devis_client.append(id_peinture_devis_client)

id_voiture_devis_client = ['id_voiture_devis_client','INT','NOT NULL']
column_devis_client.append(id_voiture_devis_client)

id_client_devis_client = ['id_client_devis_client','INT','NOT NULL']
column_devis_client.append(id_client_devis_client)

dicoTable['devis_client'] = column_devis_client

# Parametre table devis_option

id_devis_option = ['id_devis_option','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_devis_option = [id_devis_option]

id_devis_devis_option = ['id_devis_devis_option','INT','NOT NULL']
column_devis_option.append(id_devis_devis_option)

id_option_devis_option = ['id_option_devis_option','INT','NOT NULL']
column_devis_option.append(id_option_devis_option)

dicoTable['devis_option'] = column_devis_client



# Page de connexion

FrameConnexion = ['Frame','Connexion',None,2,GROOVE,5,5,LEFT]
FenetreConnexion = [FrameConnexion]


FrameEntete = ['Frame','EnTete','Connexion',2,GROOVE,5,5,TOP]
FenetreConnexion.append(FrameEntete)
LabelEntete = ['Label','Entete','EnTete','Veuillez entrer vos identifiants pour vous connectez.',LEFT,5,5]
FenetreConnexion.append(LabelEntete)


FrameIdentifiant = ['Frame','Identifiant','Connexion',2,GROOVE,5,5,TOP]
FenetreConnexion.append(FrameIdentifiant)
LabelIdentifiant = ['Label','Identifiant','Identifiant','Identifiant',LEFT,5,5]
FenetreConnexion.append(LabelIdentifiant)
EntrerIdentifiant = ['Entry','Identifiant','Identifiant',None,LEFT,5,5]
FenetreConnexion.append(EntrerIdentifiant)

FrameMDP = ['Frame','MDP','Connexion',2,GROOVE,5,5,TOP]
FenetreConnexion.append(FrameMDP)
LabelMDP = ['Label','MDP','MDP','Mot de passe',LEFT,5,5]
FenetreConnexion.append(LabelMDP)
EntrerMDP = ['Entry','MDP','MDP','*',LEFT,5,5]
FenetreConnexion.append(EntrerMDP)

FrameSeConnecter = ['Frame','SeConnecter','Connexion',2,GROOVE,5,5,TOP]
FenetreConnexion.append(FrameSeConnecter)
ButtonSeConnecter = ['Button','SeConnecter','SeConnecter','Se Connecter',Connection,LEFT,5,5,'Accueil']
FenetreConnexion.append(ButtonSeConnecter)

FrameImageTest = ['Frame','ImageTest','Connexion',2,GROOVE,5,5,TOP]
FenetreConnexion.append(FrameImageTest)
ImageTest = ['Image','ImageTest','ImageTest','img/Moscovitch_logo.png']
FenetreConnexion.append(ImageTest)

dicoFenetre['Connexion'] = FenetreConnexion

# Page d' Erreur Connexion

FrameConnexion = ['Frame','Connexion',None,2,GROOVE,5,5,LEFT]
FenetreConnexion = [FrameConnexion]


FrameEntete = ['Frame','EnTete','Connexion',2,GROOVE,5,5,TOP]
FenetreConnexion.append(FrameEntete)
LabelEntete = ['Label','Entete','EnTete','Veuillez entrer vos identifiants pour vous connectez.',LEFT,5,5]
FenetreConnexion.append(LabelEntete)


FrameIdentifiant = ['Frame','Identifiant','Connexion',2,GROOVE,5,5,TOP]
FenetreConnexion.append(FrameIdentifiant)
LabelIdentifiant = ['Label','Identifiant','Identifiant','Identifiant',LEFT,5,5]
FenetreConnexion.append(LabelIdentifiant)
EntrerIdentifiant = ['Entry','Identifiant','Identifiant',None,LEFT,5,5]
FenetreConnexion.append(EntrerIdentifiant)

FrameMDP = ['Frame','MDP','Connexion',2,GROOVE,5,5,TOP]
FenetreConnexion.append(FrameMDP)
LabelMDP = ['Label','MDP','MDP','Mot de passe',LEFT,5,5]
FenetreConnexion.append(LabelMDP)
EntrerMDP = ['Entry','MDP','MDP','*',LEFT,5,5]
FenetreConnexion.append(EntrerMDP)

FrameMessage = ['Frame','Message','Connexion',2,GROOVE,5,5,TOP]
FenetreConnexion.append(FrameMessage)
LabelMessage = ['Label','Message','Message','Identifiant ou mot de passe errone.',LEFT,5,5]
FenetreConnexion.append(LabelMessage)

FrameSeConnecter = ['Frame','SeConnecter','Connexion',2,GROOVE,5,5,TOP]
FenetreConnexion.append(FrameSeConnecter)
ButtonSeConnecter = ['Button','SeConnecter','SeConnecter','Se Connecter',Connection,LEFT,5,5,'Accueil']
FenetreConnexion.append(ButtonSeConnecter)

FrameImageTest = ['Frame','ImageTest','Connexion',2,GROOVE,5,5,TOP]
FenetreConnexion.append(FrameImageTest)
ImageTest = ['Image','ImageTest','ImageTest','img/Moscovitch_logo.png']
FenetreConnexion.append(ImageTest)


dicoFenetre['ErreurConnexion'] = FenetreConnexion



# Page choix marque voiture

FrameChoixMarqueVoiture = ['Frame','ChoixMarqueVoiture',None,2,GROOVE,5,5,LEFT]
FenetreChoixMarqueVoiture = [FrameChoixMarqueVoiture]

FrameEnTeteChoixMarqueVoiture = ['Frame','EnTeteChoixMarqueVoiture','ChoixMarqueVoiture',2,GROOVE,5,5,TOP]
FenetreChoixMarqueVoiture.append(FrameEnTeteChoixMarqueVoiture)
LabelEnTeteChoixMarqueVoiture = ['Label','EnTeteChoixMarqueVoiture','EnTeteChoixMarqueVoiture','Choix de la marque de la voiture:',LEFT,5,5]
FenetreChoixMarqueVoiture.append(LabelEnTeteChoixMarqueVoiture)

FrameLeChoixMarqueVoiture = ['Frame','LeChoixMarqueVoiture','ChoixMarqueVoiture',2,GROOVE,5,5,TOP]
FenetreChoixMarqueVoiture.append(FrameLeChoixMarqueVoiture)
LabelLeChoixMarqueVoiture = ['Label','LeChoixMarqueVoiture','LeChoixMarqueVoiture','Veuillez choisir une marque',LEFT,5,5]
FenetreChoixMarqueVoiture.append(LabelLeChoixMarqueVoiture)
ListeLeChoixMarqueVoiture = ['ListeDeroulante','LeChoixMarqueVoiture','LeChoixMarqueVoiture','libelle_marque','marque',LEFT,'readonly']
FenetreChoixMarqueVoiture.append(ListeLeChoixMarqueVoiture)

FrameValiderChoixMarqueVoiture = ['Frame','ValiderChoixMarqueVoiture','ChoixMarqueVoiture',2,GROOVE,5,5,TOP]
FenetreChoixMarqueVoiture.append(FrameValiderChoixMarqueVoiture)
ButtonValiderChoixMarqueVoiture = ['Button','ValiderChoixMarqueVoiture','ValiderChoixMarqueVoiture','Valider',Connection,LEFT,5,5,'Accueil']
FenetreChoixMarqueVoiture.append(ButtonValiderChoixMarqueVoiture)

FrameImageChoixMarqueVoiture = ['Frame','ImageChoixMarqueVoiture','ChoixMarqueVoiture',2,GROOVE,5,5,TOP]
FenetreChoixMarqueVoiture.append(FrameImageChoixMarqueVoiture)
ImageChoixMarqueVoiture = ['Image','ImageChoixMarqueVoiture','ImageChoixMarqueVoiture','img/Moscovitch_logo.png']
FenetreChoixMarqueVoiture.append(ImageChoixMarqueVoiture)

dicoFenetre['ChoixMarqueVoiture'] = FenetreChoixMarqueVoiture

# Page ajout voiture

FrameVoiture = ['Frame','Voiture',None,2,GROOVE,5,5,LEFT]
FenetreAjoutVoiture = [FrameVoiture]


FrameNumero = ['Frame','numero','Voiture',2,GROOVE,5,5,TOP]
FenetreAjoutVoiture.append(FrameNumero)
LabetNumero = ['Label','numero','numero','numero de la voiture:',LEFT,5,5]
FenetreAjoutVoiture.append(LabetNumero)
AjoutNumero = ['Entry','numero','numero',None,LEFT,5,5]
FenetreAjoutVoiture.append(AjoutNumero)


FrameKilometrage = ['Frame','kilometrage','Voiture',2,GROOVE,5,5,TOP]
FenetreAjoutVoiture.append(FrameKilometrage)
LabelKilometrage = ['Label','kilometrage','kilometrage','Kilometrage de la voiture:',LEFT,5,5]
FenetreAjoutVoiture.append(LabelKilometrage)
EntryKilometrage = ['Entry','kilometrage','kilometrage',None,LEFT,5,20]
FenetreAjoutVoiture.append(EntryKilometrage)


FramePrixAchat = ['Frame','PrixAchat','Voiture',2,GROOVE,5,5,TOP]
FenetreAjoutVoiture.append(FramePrixAchat)
LabelPrixAchat = ['Label','PrixAchat','PrixAchat','Prix d\'achat de la voiture:',LEFT,5,5]
FenetreAjoutVoiture.append(LabelPrixAchat)
EntryPrixAchat = ['Entry','PrixAchat','PrixAchat',None,LEFT,5,5]
FenetreAjoutVoiture.append(EntryPrixAchat)

FramePrixVente = ['Frame','PrixVente','Voiture',2,GROOVE,5,5,TOP]
FenetreAjoutVoiture.append(FramePrixVente)
LabelPrixVente = ['Label','PrixVente','PrixVente','Prix de vente de la voiture:',LEFT,5,5]
FenetreAjoutVoiture.append(LabelPrixVente)
EntryPrixVente = ['Entry','PrixVente','PrixVente',None,LEFT,5,5]
FenetreAjoutVoiture.append(EntryPrixVente)

FrameValiderAjoutUneVoiture = ['Frame','ValiderAjoutUneVoiture','Voiture',2,GROOVE,5,5,TOP]
FenetreAjoutVoiture.append(FrameValiderAjoutUneVoiture)
ButtonValiderAjoutUneVoiture = ['Button','ValiderAjoutUneVoiture','ValiderAjoutUneVoiture','Valider',Connection,LEFT,5,5,'Accueil']
FenetreAjoutVoiture.append(ButtonValiderAjoutUneVoiture)

FrameImageAjoutUneVoiture = ['Frame','ImageAjoutUneVoiture','Voiture',2,GROOVE,5,5,TOP]
FenetreAjoutVoiture.append(FrameImageAjoutUneVoiture)
ImageAjoutUneVoiture = ['Image','ImageAjoutUneVoiture','ImageAjoutUneVoiture','img/Moscovitch_logo.png']
FenetreAjoutVoiture.append(ImageAjoutUneVoiture)

dicoFenetre['Ajout d\'une voiture'] = FenetreAjoutVoiture