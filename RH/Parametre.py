from Tkinter import *

host = 'localhost'
user = 'root'
passwd = '00112233..y'
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


dicoFenetre = {}

# Page ajout employe

FrameEmploye = ['Frame','Employe',None,2,GROOVE,5,5,LEFT]
FenetreAjoutEmploye = [FrameEmploye]


FrameNom = ['Frame','Nom','Employe',2,GROOVE,5,5,TOP]
FenetreAjoutEmploye.append(FrameNom)
LabetNom = ['Label','Nom','Nom','Nom de l\'employe',LEFT,5,5]
FenetreAjoutEmploye.append(LabetNom)
AjoutNom = ['Entry','Nom','Nom',LEFT,5,5]
FenetreAjoutEmploye.append(AjoutNom)


FramePrenom = ['Frame','Prenom','Employe',2,GROOVE,5,5,TOP]
FenetreAjoutEmploye.append(FramePrenom)
LabelPrenom = ['Label','Prenom','Prenom','Prenom de l\'employe',LEFT,5,5]
FenetreAjoutEmploye.append(LabelPrenom)
EntryPrenom = ['Entry','Prenom','Prenom',LEFT,5,20]
FenetreAjoutEmploye.append(EntryPrenom)


FrameDateEmbauche = ['Frame','DateEmbauche','Employe',2,GROOVE,5,5,TOP]
FenetreAjoutEmploye.append(FrameDateEmbauche)
LabelDateEmbauche = ['Label','DateEmbauche','DateEmbauche','Date d\'embauche de l\'employe',LEFT,5,5]
FenetreAjoutEmploye.append(LabelDateEmbauche)

FrameDateEmbaucheJour = ['Frame','DateEmbaucheJour','DateEmbauche',2,GROOVE,5,5,TOP]
FenetreAjoutEmploye.append(FrameDateEmbaucheJour)
LabelDateEmbaucheJour = ['Label','DateEmbaucheJour','DateEmbaucheJour','Jour',LEFT,5,5]
FenetreAjoutEmploye.append(LabelDateEmbaucheJour)
EntryDateEmbaucheJour = ['Entry','DateEmbaucheJour','DateEmbaucheJour',LEFT,5,5]
FenetreAjoutEmploye.append(EntryDateEmbaucheJour)

FrameDateEmbaucheMois = ['Frame','DateEmbaucheMois','DateEmbauche',2,GROOVE,5,5,TOP]
FenetreAjoutEmploye.append(FrameDateEmbaucheMois)
LabelDateEmbaucheMois = ['Label','DateEmbaucheMois','DateEmbaucheMois','Mois',LEFT,5,5]
FenetreAjoutEmploye.append(LabelDateEmbaucheMois)
EntryDateEmbaucheMois = ['Entry','DateEmbaucheMois','DateEmbaucheMois',LEFT,5,5]
FenetreAjoutEmploye.append(EntryDateEmbaucheMois)

FrameDateEmbaucheAnnee = ['Frame','DateEmbaucheAnnee','DateEmbauche',2,GROOVE,5,5,TOP]
FenetreAjoutEmploye.append(FrameDateEmbaucheAnnee)
LabelDateEmbaucheAnnee = ['Label','DateEmbaucheAnnee','DateEmbaucheAnnee','Annee',LEFT,5,5]
FenetreAjoutEmploye.append(LabelDateEmbaucheAnnee)
EntryDateEmbaucheAnnee = ['Entry','DateEmbaucheAnee','DateEmbaucheAnnee',LEFT,5,5]
FenetreAjoutEmploye.append(EntryDateEmbaucheAnnee)


FrameSalaire = ['Frame','Salaire','Employe',2,GROOVE,5,5,TOP]
FenetreAjoutEmploye.append(FrameSalaire)
LabelSalaire = ['Label','Salaire','Salaire','Salaire de l\'employe',LEFT,5,5]
FenetreAjoutEmploye.append(LabelSalaire)
EntrySalaire = ['Entry','Salaire','Salaire',LEFT,5,20]
FenetreAjoutEmploye.append(EntrySalaire)

FrameL1Adresse = ['Frame','L1Adresse','Employe',2,GROOVE,5,5,TOP]
FenetreAjoutEmploye.append(FrameL1Adresse)
LabelL1Adresse = ['Label','L1Adresse','L1Adresse','L1 Adresse de l\'employe',LEFT,5,5]
FenetreAjoutEmploye.append(LabelL1Adresse)
EntryL1Adresse = ['Entry','L1Adresse','L1Adresse',LEFT,5,20]
FenetreAjoutEmploye.append(EntryL1Adresse)

FrameL2Adresse = ['Frame','L2Adresse','Employe',2,GROOVE,5,5,TOP]
FenetreAjoutEmploye.append(FrameL2Adresse)
LabelL2Adresse = ['Label','L2Adresse','L2Adresse','L2 Adresse de l\'employe',LEFT,5,5]
FenetreAjoutEmploye.append(LabelL2Adresse)
EntryL2Adresse = ['Entry','L2Adresse','L2Adresse',LEFT,5,20]
FenetreAjoutEmploye.append(EntryL2Adresse)

FrameVille = ['Frame','Ville','Employe',2,GROOVE,5,5,TOP]
FenetreAjoutEmploye.append(FrameVille)
LabelVille = ['Label','Ville','Ville','Ville',LEFT,5,5]
FenetreAjoutEmploye.append(LabelVille)
ListDeroulandeVille = ['ListeDeroulante','ListeVille','Ville',LEFT,'readonly']
FenetreAjoutEmploye.append(ListDeroulandeVille)

dicoFenetre['Ajout d\'un employe'] = FenetreAjoutEmploye