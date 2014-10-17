host = 'localhost'
user = 'root'
passwd = '00112233..y'
dbname = 'prodRH'

dico = {}

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
telephone_employe = ['telephone_employe','INT','NOT NULL']
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

dico['employe'] = column_employe

# Parametre table service

id_service = ['id_service','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_service = [id_service]
libelle_service = ['libelle_service','VARCHAR(50)','NOT NULL']
column_service.append(libelle_service)
id_service_service = ['id_service_service','INT','NOT NULL']
column_service.append(id_service_service)

dico['service'] = column_service

# Parametre table ville

id_ville = ['id_ville','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_ville = [id_ville]
libelle_ville = ['libelle_ville','VARCHAR(50)','NOT NULL']
column_ville.append(libelle_ville)

dico['ville'] = column_ville

# Parametre table grade

id_grade = ['id_grade','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_grade = [id_grade]
libelle_grade = ['libelle_grade','VARCHAR(50)','NOT NULL']
column_grade.append(libelle_grade)

dico['grade'] = column_grade

# Parametre table diplome

id_diplome = ['id_diplome','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_diplome = [id_diplome]
libelle_diplome = ['libelle_diplome','VARCHAR(50)','NOT NULL']
column_diplome.append(libelle_diplome)
level_diplome = ['level_diplome','INT','NOT NULL']
column_diplome.append(level_diplome)

dico['diplome'] = column_diplome

# Parametre table diplome_obtenu

id_diplome_obtenu = ['id_diplome_obtenu','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_diplome_obtenu = [id_diplome_obtenu]
id_diplome_diplome_obtenu = ['id_diplome_diplome_obtenu','INT','NOT NULL']
column_diplome_obtenu.append(id_diplome_diplome_obtenu)
id_employe_diplome_obtenu = ['id_employe_diplome_obtenu','INT','NOT NULL']
column_diplome_obtenu.append(id_employe_diplome_obtenu)

dico['diplome_obtenu'] = column_diplome_obtenu