# -*- coding: utf8 -*-

from Tkinter import *
from Function import *

host = 'localhost'
user = 'root'
passwd = 'root'
dbname = 'prodRH'
backGroundColor = 'white'
fgColor = 'maroon'

dicoTable = {}

# Parametre Table employe
id_employe = ['id_employe','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_employe = [id_employe]
prenom_employe = ['prenom_employe','VARCHAR(50)','NOT NULL']
column_employe.append(prenom_employe)
nom_employe = ['nom_employe','VARCHAR(50)','NOT NULL']
column_employe.append(nom_employe)
date_embauche_employe = ['date_embauche_employe','DATE','NOT NULL']
column_employe.append(date_embauche_employe)
salaire_employe = ['salaire_employe','FLOAT','NOT NULL']
column_employe.append(salaire_employe)
adresse_l1_employe = ['adresse_l1_employe','VARCHAR(50)','NOT NULL']
column_employe.append(adresse_l1_employe)
adresse_l2_employe = ['adresse_l2_employe','VARCHAR(50)','NULL']
column_employe.append(adresse_l2_employe)
cp_employe = ['cp_employe','INT','NOT NULL']
column_employe.append(cp_employe)
id_ville_employe = ['id_ville_employe','INT','NOT NULL']
column_employe.append(id_ville_employe)
telephone_employe = ['telephone_employe','VARCHAR(20)','NOT NULL']
column_employe.append(telephone_employe)
email_employe = ['email_employe','VARCHAR(50)','NOT NULL']
column_employe.append(email_employe)
commentaire_employe = ['commentaire_employe','VARCHAR(4000)','NULL']
column_employe.append(commentaire_employe)
poste_employe = ['poste_employe','VARCHAR(50)','NOT NULL']
column_employe.append(poste_employe)
id_grade_employe = ['id_grade_employe','INT','NOT NULL']
column_employe.append(id_grade_employe)
id_service_employe = ['id_service_employe','INT','NOT NULL']
column_employe.append(id_service_employe)

dicoTable['employe'] = column_employe

# Parametre table service

id_service = ['id_service','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_service = [id_service]
libelle_service = ['libelle_service','VARCHAR(50)','NOT NULL']
column_service.append(libelle_service)
id_service_service = ['id_service_service','INT','NULL']
column_service.append(id_service_service)

dicoTable['service'] = column_service

# Parametre table ville

id_ville = ['id_ville','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_ville = [id_ville]
libelle_ville = ['libelle_ville','VARCHAR(50)','NOT NULL']
column_ville.append(libelle_ville)

dicoTable['ville'] = column_ville

# Parametre table grade

id_grade = ['id_grade','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_grade = [id_grade]
libelle_grade = ['libelle_grade','VARCHAR(50)','NOT NULL']
column_grade.append(libelle_grade)

dicoTable['grade'] = column_grade

# Parametre table diplome

id_diplome = ['id_diplome','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_diplome = [id_diplome]
libelle_diplome = ['libelle_diplome','VARCHAR(50)','NOT NULL']
column_diplome.append(libelle_diplome)
level_diplome = ['level_diplome','INT','NOT NULL']
column_diplome.append(level_diplome)

dicoTable['diplome'] = column_diplome

# Parametre table diplome_obtenu

id_diplome_obtenu = ['id_diplome_obtenu','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_diplome_obtenu = [id_diplome_obtenu]
id_diplome_diplome_obtenu = ['id_diplome_diplome_obtenu','INT','NOT NULL']
column_diplome_obtenu.append(id_diplome_diplome_obtenu)
id_employe_diplome_obtenu = ['id_employe_diplome_obtenu','INT','NOT NULL']
column_diplome_obtenu.append(id_employe_diplome_obtenu)

dicoTable['diplome_obtenu'] = column_diplome_obtenu

# Parametre table TypeFenetre

libelle_type_fenetre = ['libelle_type_fenetre','VARCHAR(50)','NOT NULL']
column_type_fenetre = [libelle_type_fenetre]

dicoTable['type_fenetre'] = column_type_fenetre

dicoFenetre = {}

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

# Page accueil

FrameAccueil = ['Frame','Accueil',None,2,GROOVE,5,5,LEFT]
FenetreAccueil = [FrameAccueil]

FrameMessage = ['Frame','Message','Accueil',2,GROOVE,5,5,TOP]
FenetreAccueil.append(FrameMessage)
LabelMessage = ['Label','Message','Message','Bienvenue sur l\'accueil.',LEFT,5,5]
FenetreAccueil.append(LabelMessage)

FrameDepartement = ['Frame','Departement','Accueil',2,GROOVE,5,5,TOP]
FenetreAccueil.append(FrameDepartement)
ListeDynamiqueButtonDepartement = ['ListeDynamiqueButton','Departement','Departement','libelle_service','service','Null','Service']
FenetreAccueil.append(ListeDynamiqueButtonDepartement)
ButtonAjouterUnDepartement = ['Button','Departement','Departement','Ajouter un departement',FonctionQuiFoutRien,TOP,5,5,'AjouterUnDepartement']
FenetreAccueil.append(ButtonAjouterUnDepartement)

FrameEmploye = ['Frame','Employe','Accueil',2,GROOVE,5,5,TOP]
FenetreAccueil.append(FrameEmploye)
ButtonRecrutement = ['Button','Recrutement','Employe','Recrutement',FonctionQuiFoutRien,TOP,5,5,'AjouterUnEmploye']
FenetreAccueil.append(ButtonRecrutement)

dicoFenetre['Accueil'] = FenetreAccueil

# Page service

FrameService = ['Frame','Service',None,2,GROOVE,5,5,LEFT]
FenetreServiceSelec = [FrameService]

FrameDepartementSelec = ['Frame','DepartementSelec','Service',2,GROOVE,5,5,TOP]
FenetreServiceSelec.append(FrameDepartementSelec)
LabelDepartementSelec = ['Label','DepartementSelec','DepartementSelec','#Selected#',LEFT,5,5]
FenetreServiceSelec.append(LabelDepartementSelec)

FrameServiceSelec = ['Frame','ServiceSelec','Service',2,GROOVE,5,5,TOP]
FenetreServiceSelec.append(FrameServiceSelec)
ListeDynamiqueButtonServiceSelec = ['ListeDynamiqueButton','ServiceSelec','ServiceSelec','libelle_service','service','#SelectedButton#','Service']
FenetreServiceSelec.append(ListeDynamiqueButtonServiceSelec)

FrameServiceCreer = ['Frame','ServiceCreer','Service',2,GROOVE,5,5,TOP]
FenetreServiceSelec.append(FrameServiceCreer)
ButtonServiceCreer = ['Button','ServiceCreer','ServiceCreer','Ajouter un service',FonctionQuiFoutRien,TOP,5,5,'AjouterUnEmploye']
FenetreServiceSelec.append(ButtonServiceCreer)



dicoFenetre['Service'] = FenetreServiceSelec

# Page Ajouter un Departement

FrameDepartement = ['Frame','Departement',None,2,GROOVE,5,5,LEFT]
FenetreAjouterDepartement = [FrameDepartement]

FrameTitreDepartement = ['Frame','TitreDepartement','Departement',2,GROOVE,5,5,TOP]
FenetreAjouterDepartement.append(FrameTitreDepartement)
LabelTitreDepartement = ['Label','TitreDepartement','TitreDepartement','Ajouter un departement',TOP,5,5]
FenetreAjouterDepartement.append(LabelTitreDepartement)

FrameNomDepartement = ['Frame','NomDepartement','Departement',2,GROOVE,5,5,TOP]
FenetreAjouterDepartement.append(FrameNomDepartement)
LabelNomDepartement = ['Label','NomDepartement','NomDepartement','LibelleDepartement',LEFT,5,5]
FenetreAjouterDepartement.append(LabelNomDepartement)
EntrerNomDepartement= ['Entry','NomDepartement','NomDepartement',None,LEFT,5,5]
FenetreAjouterDepartement.append(EntrerNomDepartement)

FrameButtonDepartement = ['Frame','ButtonDepartement','Departement',2,GROOVE,5,5,TOP]
FenetreAjouterDepartement.append(FrameButtonDepartement)
ButtonAjouterDepartement = ['Button','AjouterDepartement','ButtonDepartement','Ajouter un departement',AjouterUnDepartement,TOP,5,5,'Accueil']
FenetreAjouterDepartement.append(ButtonAjouterDepartement)

dicoFenetre['AjouterUnDepartement'] = FenetreAjouterDepartement

# Page ajout employe

FrameEmploye = ['Frame','Employe',None,2,GROOVE,5,5,LEFT]
FenetreAjoutEmploye = [FrameEmploye]


FrameNom = ['Frame','Nom','Employe',2,GROOVE,5,5,TOP]
FenetreAjoutEmploye.append(FrameNom)
LabetNom = ['Label','Nom','Nom','Nom de l\'employe',LEFT,5,5]
FenetreAjoutEmploye.append(LabetNom)
AjoutNom = ['Entry','Nom','Nom',None,LEFT,5,5]
FenetreAjoutEmploye.append(AjoutNom)


FramePrenom = ['Frame','Prenom','Employe',2,GROOVE,5,5,TOP]
FenetreAjoutEmploye.append(FramePrenom)
LabelPrenom = ['Label','Prenom','Prenom','Prenom de l\'employe',LEFT,5,5]
FenetreAjoutEmploye.append(LabelPrenom)
EntryPrenom = ['Entry','Prenom','Prenom',None,LEFT,5,20]
FenetreAjoutEmploye.append(EntryPrenom)


FrameDateEmbauche = ['Frame','DateEmbauche','Employe',2,GROOVE,5,5,TOP]
FenetreAjoutEmploye.append(FrameDateEmbauche)
LabelDateEmbauche = ['Label','DateEmbauche','DateEmbauche','Date d\'embauche de l\'employe',LEFT,5,5]
FenetreAjoutEmploye.append(LabelDateEmbauche)

FrameDateEmbaucheJour = ['Frame','DateEmbaucheJour','DateEmbauche',2,GROOVE,5,5,TOP]
FenetreAjoutEmploye.append(FrameDateEmbaucheJour)
LabelDateEmbaucheJour = ['Label','DateEmbaucheJour','DateEmbaucheJour','Jour',LEFT,5,5]
FenetreAjoutEmploye.append(LabelDateEmbaucheJour)
EntryDateEmbaucheJour = ['Entry','DateEmbaucheJour','DateEmbaucheJour',None,LEFT,5,5]
FenetreAjoutEmploye.append(EntryDateEmbaucheJour)

FrameDateEmbaucheMois = ['Frame','DateEmbaucheMois','DateEmbauche',2,GROOVE,5,5,TOP]
FenetreAjoutEmploye.append(FrameDateEmbaucheMois)
LabelDateEmbaucheMois = ['Label','DateEmbaucheMois','DateEmbaucheMois','Mois',LEFT,5,5]
FenetreAjoutEmploye.append(LabelDateEmbaucheMois)
EntryDateEmbaucheMois = ['Entry','DateEmbaucheMois','DateEmbaucheMois',None,LEFT,5,5]
FenetreAjoutEmploye.append(EntryDateEmbaucheMois)

FrameDateEmbaucheAnnee = ['Frame','DateEmbaucheAnnee','DateEmbauche',2,GROOVE,5,5,TOP]
FenetreAjoutEmploye.append(FrameDateEmbaucheAnnee)
LabelDateEmbaucheAnnee = ['Label','DateEmbaucheAnnee','DateEmbaucheAnnee','Annee',LEFT,5,5]
FenetreAjoutEmploye.append(LabelDateEmbaucheAnnee)
EntryDateEmbaucheAnnee = ['Entry','DateEmbaucheAnee','DateEmbaucheAnnee',None,LEFT,5,5]
FenetreAjoutEmploye.append(EntryDateEmbaucheAnnee)


FrameSalaire = ['Frame','Salaire','Employe',2,GROOVE,5,5,TOP]
FenetreAjoutEmploye.append(FrameSalaire)
LabelSalaire = ['Label','Salaire','Salaire','Salaire de l\'employe',LEFT,5,5]
FenetreAjoutEmploye.append(LabelSalaire)
EntrySalaire = ['Entry','Salaire','Salaire',None,LEFT,5,20]
FenetreAjoutEmploye.append(EntrySalaire)

FrameL1Adresse = ['Frame','L1Adresse','Employe',2,GROOVE,5,5,TOP]
FenetreAjoutEmploye.append(FrameL1Adresse)
LabelL1Adresse = ['Label','L1Adresse','L1Adresse','L1 Adresse de l\'employe',LEFT,5,5]
FenetreAjoutEmploye.append(LabelL1Adresse)
EntryL1Adresse = ['Entry','L1Adresse','L1Adresse',None,LEFT,5,20]
FenetreAjoutEmploye.append(EntryL1Adresse)

FrameL2Adresse = ['Frame','L2Adresse','Employe',2,GROOVE,5,5,TOP]
FenetreAjoutEmploye.append(FrameL2Adresse)
LabelL2Adresse = ['Label','L2Adresse','L2Adresse','L2 Adresse de l\'employe',LEFT,5,5]
FenetreAjoutEmploye.append(LabelL2Adresse)
EntryL2Adresse = ['Entry','L2Adresse','L2Adresse',None,LEFT,5,20]
FenetreAjoutEmploye.append(EntryL2Adresse)

FrameVille = ['Frame','Ville','Employe',2,GROOVE,5,5,TOP]
FenetreAjoutEmploye.append(FrameVille)
LabelVille = ['Label','Ville','Ville','Ville',LEFT,5,5]
FenetreAjoutEmploye.append(LabelVille)
ListDeroulandeVille = ['ListeDeroulante','ListeVille','ListeVille','libelle_Ville',LEFT,'readonly']
FenetreAjoutEmploye.append(ListDeroulandeVille)

dicoFenetre['Ajout d\'un employe'] = FenetreAjoutEmploye

# Page d'ajout de Fenetre (Etape Nom Fenetre)

FrameGestionDeFenetre = ['Frame','GestionDeFenetre',None,2,GROOVE,5,5,LEFT]
FenetreGestionDeFenetre = [FrameGestionDeFenetre]

FrameChoix = ['Frame','FrameChoix','GestionDeFenetre',2,GROOVE,5,5,TOP]
FenetreGestionDeFenetre.append(FrameChoix)
ButtonCreationDeFenetre = ['Button','CreationDeFenetre','FrameChoix','Ajouter une fenetre',FonctionQuiFoutRien,TOP,5,5,'FenetreCreationDeFenetre']
FenetreGestionDeFenetre.append(ButtonCreationDeFenetre)
ButtonModificationDeFenetre = ['Button','ModificationDeFenetre','FrameChoix','Modification De Fenetre',FonctionQuiFoutRien,TOP,5,5,'Accueil']
FenetreGestionDeFenetre.append(ButtonModificationDeFenetre)
ButtonSuppressionDeFenetre = ['Button','SuppressionDeFenetre','FrameChoix','Suppression De Fenetre',FonctionQuiFoutRien,TOP,5,5,'Accueil']
FenetreGestionDeFenetre.append(ButtonSuppressionDeFenetre)


dicoFenetre['GestionDeFenetre'] = FenetreGestionDeFenetre

# Page Création fenetre
FrameCreationFenetre = ['Frame','CreationDeFenetre',None,2,GROOVE,5,5,LEFT]
FenetreCreationDeFenetre = [FrameCreationFenetre]

FrameChoixNom = ['Frame','ChoixNom','CreationDeFenetre',2,GROOVE,5,5,TOP]
FenetreCreationDeFenetre.append(FrameChoixNom)
LabeChoixNom = ['Label','ChoixNom','ChoixNom','Nom fenetre',LEFT,5,5]
FenetreCreationDeFenetre.append(LabeChoixNom)
EntryChoixNom = ['Entry','ChoixNom','ChoixNom',None,LEFT,5,20]
FenetreCreationDeFenetre.append(EntryChoixNom)

FrameDescription = ['Frame','Description','CreationDeFenetre',2,GROOVE,5,5,TOP]
FenetreCreationDeFenetre.append(FrameDescription)
LabelDescription = ['Label','Description','Description','Description fenetre',LEFT,5,5]
FenetreCreationDeFenetre.append(LabelDescription)
EntryDescription = ['Entry','Description','Description',None,LEFT,5,20]
FenetreCreationDeFenetre.append(EntryDescription)

ButtonEtape1CreationFenetre = ['Button','Etape1CreationFenetre','CreationDeFenetre','Commencer la création de la fenetre',Etape1CreationFenetre,TOP,5,5,'AjouterUnElement1']
FenetreCreationDeFenetre.append(ButtonEtape1CreationFenetre)

dicoFenetre['FenetreCreationDeFenetre'] = FenetreCreationDeFenetre

# Page d'ajout d'un element à une fenetre etape 1
FrameAjouterUnElement1 = ['Frame','AjouterUnElement1',None,2,GROOVE,5,5,LEFT]
FenetreAjouterUnElement1 = [FrameAjouterUnElement1]

FrameTypeElelement = ['Frame','TypeElelement','AjouterUnElement1',2,GROOVE,5,5,TOP]
FenetreAjouterUnElement1.append(FrameTypeElelement)
LabeTypeElelement = ['Label','TypeElelement','TypeElelement','Type element',LEFT,5,5]
FenetreAjouterUnElement1.append(LabeTypeElelement)
ListDeroulandeTypeElelement = ['ListeDeroulante','TypeElelement','libelle_TypeElelement','p_TypeElelement',LEFT,'readonly']
FenetreAjouterUnElement1.append(ListDeroulandeTypeElelement)

ButtonTypeElelement = ['Button','TypeElelement','AjouterUnElement1','Choix type element',Exit,TOP,5,5,'Exit']
FenetreAjouterUnElement1.append(ButtonTypeElelement)

dicoFenetre['AjouterUnElement1'] = FenetreAjouterUnElement1

# Formulaire pour un element de type frame
FrameFormualireFrame = ['Frame','FormualireFrame',None,2,GROOVE,5,5,LEFT]
FenetreFormualireFrame = [FrameFormualireFrame]

FrameInfoFrame = ['Frame','InfoFrame','FormualireFrame',2,GROOVE,5,5,LEFT]
FenetreFormualireFrame.append(FrameInfoFrame)

LabelNomFrame = ['Label','NomFrame','InfoFrame','Nom du frame',TOP,5,5]
FenetreFormualireFrame.append(LabelNomFrame)
EntryNomFrame = ['Entry','NomFrame','InfoFrame',None,TOP,5,20]
FenetreFormualireFrame.append(EntryNomFrame)

LabelNomFrameParent = ['Label','NomFrameParent','InfoFrame','Nom du frame parent',TOP,5,5]
FenetreFormualireFrame.append(LabelNomFrameParent)
EntryNomFrameParent = ['Entry','NomFrameParent','InfoFrame',None,TOP,5,20]
FenetreFormualireFrame.append(EntryNomFrameParent)

LabelPositionement = ['Label','Positionement','InfoFrame','Positionement du frame',TOP,5,5]
FenetreFormualireFrame.append(LabelPositionement)
EntryPositionement = ['Entry','Positionement','InfoFrame',None,TOP,5,20]
FenetreFormualireFrame.append(EntryPositionement)

ButtonValider = ['Button','Valider','InfoFrame','Valider',Exit,TOP,5,5,'Exit']
FenetreFormualireFrame.append(ButtonValider)

dicoFenetre['Frame'] = FenetreFormualireFrame


# Formulaire pour un element de type Label
FrameFormualireLabel = ['Label','FormualireLabel',None,2,GROOVE,5,5,LEFT]
FenetreFormualireLabel = [FrameFormualireLabel]

FrameInfoLabel = ['Frame','InfoLabel','FormualireLabel',2,GROOVE,5,5,LEFT]
FenetreFormualireLabel.append(FrameInfoLabel)

LabelNomLabel = ['Label','NomLabel','InfoLabel','Nom du Label',TOP,5,5]
FenetreFormualireLabel.append(LabelNomLabel)
EntryNomLabel = ['Entry','NomLabel','InfoLabel',None,TOP,5,20]
FenetreFormualireLabel.append(EntryNomLabel)

LabelNomFrameParent_Label = ['Label','NomFrameParent','InfoLabel','Nom du frame parent',TOP,5,5]
FenetreFormualireLabel.append(LabelNomFrameParent_Label)
EntryNomFrameParent_Label = ['Entry','NomFrameParent','InfoLabel',None,TOP,5,20]
FenetreFormualireLabel.append(EntryNomFrameParent_Label)

LabelTexteDuLabel = ['Label','LabelTexteDuLabel','InfoLabel','Texte du label',TOP,5,5]
FenetreFormualireLabel.append(LabelTexteDuLabel)
EntryTexteDuLabel = ['Entry','EntryTexteDuLabel','InfoLabel',None,TOP,5,20]
FenetreFormualireLabel.append(EntryTexteDuLabel)

LabelPositionement_Label = ['Label','Positionement','InfoLabel','Positionement du frame',TOP,5,5]
FenetreFormualireLabel.append(LabelPositionement_Label)
EntryPositionement_Label = ['Entry','Positionement','InfoLabel',None,TOP,5,20]
FenetreFormualireLabel.append(EntryPositionement_Label)

ButtonValider_Label = ['Button','Valider','InfoLabel','Valider',Exit,TOP,5,5,'Exit']
FenetreFormualireLabel.append(ButtonValider)

# Formulaire pour un element de type Entry
FrameFormualireEntry = ['Label','FormualireEntry',None,2,GROOVE,5,5,LEFT]
FenetreFormualireEntry = [FrameFormualireEntry]

FrameInfoEntry = ['Frame','InfoEntry','FormualireEntry',2,GROOVE,5,5,LEFT]
FenetreFormualireEntry.append(FrameInfoEntry)

LabelNomEntry = ['Label','NomEntry','InfoEntry','Nom du Entry',TOP,5,5]
FenetreFormualireEntry.append(LabelNomEntry)
EntryNomEntry = ['Entry','NomEntry','InfoLabel',None,TOP,5,20]
FenetreFormualireLabel.append(EntryPositionement_Label)