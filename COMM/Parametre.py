host = 'localhost'
user = 'root'
passwd = '00112233..y'
dbname = 'prodCO'
dico = {}

# Parametre Table fournisseur
id_fournisseur = ['id_fournisseur','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_fournisseur = [id_fournisseur]

prenom_fournisseur = ['prenom_fournisseur','VARCHAR(50)','NOT NULL']
column_fournisseur.append(prenom_fournisseur)

nom_fournisseur = ['nom_fournisseur','VARCHAR(50)','NOT NULL']
column_fournisseur.append(nom_fournisseur)

adresse_l1_fournisseur = ['adresse_l1_fournisseur','VARCHAR(50)','NOT NULL']
column_fournisseur.append(adresse_l1_fournisseur)

adresse_l2_fournisseur = ['adresse_l2_fournisseur','VARCHAR(50)','NULL']
column_fournisseur.append(adresse_l2_fournisseur)

cp_fournisseur = ['cp_fournisseur','INT','NOT NULL']
column_fournisseur.append(cp_fournisseur)

id_ville_fournisseur = ['id_ville_fournisseur','INT','NOT NULL']
column_fournisseur.append(id_ville_fournisseur)

telephone_fournisseur = ['telephone_fournisseur','INT','NOT NULL']
column_fournisseur.append(telephone_fournisseur)

email_fournisseur = ['email_fournisseur','VARCHAR(50)','NOT NULL']
column_fournisseur.append(email_fournisseur)

nom_represantant_fournisseur = ['nom_represantant_fournisseur','VARCHAR(50)','NOT NULL']
column_fournisseur.append(nom_represantant_fournisseur)


dico['fournisseur'] = column_fournisseur

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

id_ville_client = ['id_ville_client','INT','NOT NULL']
column_fournisseur.append(id_ville_client)

telephone_client = ['telephone_client','INT','NOT NULL']
column_client.append(telephone_client)

email_client = ['email_client','VARCHAR(50)','NOT NULL']
column_client.append(email_client)

id_ville_client = ['id_ville_client','INT','NOT NULL']
column_client.append(id_ville_client)

dico['client'] = column_client

# Parametre table ville
id_ville = ['id_ville','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_ville = [id_ville]

libelle_ville = ['libelle_ville','VARCHAR(50)','NOT NULL']
column_ville.append(libelle_ville)

dico['ville'] = column_ville

# Parametre table modele
id_modele = ['id_modele','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_modele = [id_modele]

libelle_modele = ['libelle_modele','VARCHAR(50)','NOT NULL']
column_modele.append(libelle_modele)

id_marque_modele = ['id_marque_modele','INT','NOT NULL']
column_modele.append(id_marque_modele)

dico['modele'] = column_modele

# Parametre table marque
id_marque = ['id_marque','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_marque = [id_marque]

libelle_marque = ['libelle_marque','VARCHAR(50)','NOT NULL']
column_marque.append(libelle_marque)

dico['marque'] = column_marque

# Parametre table option
id_option = ['id_option','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_option = [id_option]

libelle_option = ['libelle_option','VARCHAR(50)','NOT NULL']
column_option.append(libelle_option)

prix_option = ['prix_option','REEl','NOT NULL']
column_option.append(prix_option)

dico['option'] = column_option

# Parametre table voiture
id_voiture = ['id_voiture','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_voiture = [id_voiture]

vitesse_voiture = ['vitesse_voiture','INT','NOT NULL']
column_voiture.append(vitesse_voiture)

carburant_voiture = ['carburant_voiture','VARCHAR(50)','NOT NULL']
column_voiture.append(carburant_voiture)

prix_achat_hors_taxe_voiture =['prix_achat_hors_taxe_voiture','INT','NOT NULL']
column_voiture.append(prix_achat_hors_taxe_voiture)

prix_vente_hors_taxe_voiture =['prix_vente_hors_taxe_voiture','REEl','NOT NULL']
column_voiture.append(prix_vente_hors_taxe_voiture)

id_modele_voiture = ['id_modele_voiture','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_voiture.append(id_modele_voiture )

id_option_voiture = ['id_option_voiture','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_voiture.append(id_option_voiture )

id_tva_voiture = ['id_tva_voiture','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_voiture.append(id_tva_voiture )

id_fournisseur_voiture = ['id_fournisseur_voiture','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_voiture.append(id_fournisseur_voiture)

dico['voiture'] = column_voiture


# Parametre table TVA
id_tva = ['id_tva','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_tva = (id_tva)

taux_tva = ['taux_tva','REEl','NOT NULL']
column_tva.append(taux_tva)

date_tva = ['date_tva','DATE','NOT NULL']
column_tva.append(date_tva)

dico['tva'] = column_tva

# Parametre table facture client
id_facture_client = ['id_facture_client','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_facture_client = (id_facture_client)

date_facture_client = ['date_facture_client','DATE','NOT NULL']
column_facture_client.append(date_facture_client)

id_commande_client_facture_client = ['id_commande_client_facture_client','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_facture_client.append(id_commande_client_facture_client)

dico['facture_client'] = column_facture_client

# Parametre table commande client
id_commande_client = ['id_commande_client','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_commande_client = (id_commande_client)

date_commande_client = ['date_commande_client','DATE','NOT NULL']
column_commande_client.append(date_commande_client)

id_voiture_commade_client = ['id_voiture_commade_client','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_commande_client.append(id_voiture_commade_client)

id_client_commande_client = ['id_client_commande_client','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_commande_client.append(id_client_commande_client)

dico['commande_client'] = column_commande_client

# Parametre table facture fournisseur
id_facture_fournisseur = ['id_facture_fournisseur','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_facture_fournisseur = (id_facture_fournisseur)

date_facture_fournisseur = ['date_facture_fournisseur','DATE','NOT NULL']
column_facture_fournisseur.append(date_facture_fournisseur)

id_commande_fournisseur_facture_fournisseur  = ['id_commande_fournisseur_facture_fournisseur ','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_facture_fournisseur.append(id_commande_fournisseur_facture_fournisseur)

dico['facture_fournisseur'] = column_facture_fournisseur

# Parametre table commande fournisseur
id_commande_fournisseur = ['id_commande_fournisseur','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_commande_fournisseur = (id_commande_fournisseur)

date_commande_fournisseur = ['date_commande_fournisseurt','DATE','NOT NULL']
column_commande_fournisseur.append(date_commande_fournisseur)

id_voiture_commande_fourniseur = ['id_voiture_commande_fourniseur','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_commande_fournisseur.append(id_voiture_commande_fourniseur)

id_fournisseur_commande_fourniseur = ['id_fournisseur_commande_fourniseur','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_commande_fournisseur.append(id_fournisseur_commande_fourniseur)

dico['commande_fournisseur'] = column_commande_fournisseur

# Parametre table livraison
id_livraison =['id_livraison','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT',]
column_livraison = (id_livraison)

date_prevu_livraison = ['date_prevu_livraison','DATE','NOT NULL']
column_livraison.append(date_prevu_livraison)

date_de_recuperation = ['date_de_recuperation','DATE','NOT NULL']
column_livraison.append(date_de_recuperation)

observation_livraison = ['observation_livraison','VARCHAR(500)','NULL']
column_livraison.append(observation_livraison)

id_commande_fournisseur_livraison = ['id_commande_fournisseur_livraison','INT','NOT NULL','PRIMARY KEY','AUTO_INCREMENT']
column_livraison.append(id_commande_fournisseur_livraison)

dico['livraison'] = column_livraison