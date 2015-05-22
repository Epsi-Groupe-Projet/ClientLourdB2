 # -*- coding: utf8 -*-

class Voiture :
    """ Classe permettant d'ajouter une voiture """
    def __init__(self, p_numero_serie, p_kilometrage, p_prix_achat_HT, p_prix_vente_HT, p_modele, p_tva):
        """ Constructeur """

        self.numero_serie = p_numero_serie
        self.kilometrage_voiture = p_kilometrage
        self.prix_achat_hors_taxe_voiture = p_prix_achat_HT
        self.prix_vente_hors_taxe_voiture = p_prix_vente_HT
        self.modele_voiture = p_modele
        self.tva_voiture = p_tva

    def GetNumeroSerie(self):
        """ methode qui renvoie le numero de serie de la voiture """
        return self.numero_serie

    def GetKilometrage(self):
        return self.kilometrage_voiture

    def GetPrixVente(self):
        """ methode qui renvoie le prix de vente de la voiture """
        return self.prix_vente_hors_taxe_voiture

    def GetPrixAchat(self):
        """ methode qui renvoie le prix d'achat de la voiture """
        return self.prix_achat_hors_taxe_voiture

    def GetTVA(self):
        """ methode qui renvoie la tva appliquee sur la voiture """

        return self.tva_voiture

    def SetKilometrage(self, new_kilometrage):
        """ methode  qui permet de mettre aÃƒâ€šÃ‚Â  jour le Kilometrage de la voiture """
        self.kilometrage_voiture = new_kilometrage

    def SetPrixVente(self, new_prix_vente_HT):
        """ methode  qui permet de modifier le prix de vente de la voiture """
        self.prix_vente_hors_taxe_voiture = new_prix_vente_HT

    def SetPrixAchat(self, new_prix_achat_HT):
        """ methode  qui permet de modifier le prix d'achat de la voiture """
        self.prix_achat_hors_taxe_voiture = new_prix_achat_HT

    def GetModele(self):
        """ methode qui renvoie le modele de la voiture """

        return self.modele_voiture

    def SetModele(self, new_modele):
        """ methode  qui permet de modifier le modele de la voiture """
        self.modele_voiture = new_modele

    def SetTVA(self, new_tva):
        """ methode qui permet de modifier la tva d'une voiture """
        self.tva_voiture = new_tva

    def __del__(self):
        """ methode qui supprime la voiture """
        del self

    # Methode pour ajouter ou modifier la voiturer dans la table voiture
    def VoitureIntoTable(self,connexion): 
        """A MODIFIER"""

        # Si l'voiture ne possede pas de code cela veut dire que l'voiture n'existe pas dans la table

        if self.p_numero_serie is None:
            """A PARTIR DE LA"""

            # On teste si l'voiture existe deja dans la table

            requete = "SELECT id_voiture FROM voiture WHERE nom_voiture = \'"+self.mnom_voiture+"\' AND prenom_voiture = \'"+self.mprenom_voiture+"\'"
            result = MysqlDef.executeRequete(connexion,requete)

            try:
                result[0][0] is None
            except IndexError:
                requete = "INSERT INTO voiture (prenom_voiture, nom_voiture, date_embauche_voiture,salaire_voiture,adresse_l1_voiture,adresse_l2_voiture,cp_voiture,id_ville_voiture,telephone_voiture, email_voiture,commentaire_voiture,poste_voiture,id_grade_voiture,id_service_voiture) VALUES (\'"+self.mprenom_voiture+"\', \'"+self.mnom_voiture+"\',\'"+self.mdate_embauche_voiture+"\',"+self.msalaire_voiture+",\'"+self.madresse_l1_voiture+"\',\'"+self.madresse_l2_voiture+"\',"+self.mcp_voiture+","+self.mville_voiture.GetIdVille()+",\'"+self.mtelephone_voiture+"\',\'"+self.memail_voiture+"\',\'"+self.mcommentaire_voiture+"\',\'"+self.mposte_voiture+"\',"+self.mgrade_voiture.GetIdGrade()+","+self.mservice_voiture.GetIdService()+");"
                
                if MysqlDef.executeRequete(connexion,requete) == False:
                    print "Insertion de l'voiture: {0} {1}, a echoue".format(self.mprenom_voiture, self.mnom_voiture)
                    return False

                else:
                    print "Insertion de l'voiture: {0} {1}, a reussi".format(self.mprenom_voiture, self.mnom_voiture)
                    # Recuperation de l'id de l'voiture
                    requete = "SELECT id_voiture FROM voiture WHERE nom_voiture = \'"+self.mnom_voiture+"\' AND prenom_voiture = \'"+self.mprenom_voiture+"\'"
                    result = MysqlDef.executeRequete(connexion,requete)
                    self.mid_voiture = str(result[0][0])
                    return True
    
            else:
                print "L'voiture {0} {1} existe deja dans la table ajout impossible".format(self.mprenom_voiture,self.mnom_voiture)
                # Recuperation de l'id de l'voiture
                requete = "SELECT id_voiture FROM voiture WHERE nom_voiture = \'"+self.mnom_voiture+"\' AND prenom_voiture = \'"+self.mprenom_voiture+"\'"
                result = MysqlDef.executeRequete(connexion,requete)
                self.mid_voiture = str(result[0][0])
                return False

        # Sinon l'voiture existe deja alors on le modifie (on le supprimant d'abort puis on l'ajoutant)
        else:
            requete = "DELETE FROM voiture WHERE id_voiture = \'"+self.mid_voiture+"\'"
            if MysqlDef.executeRequete(connexion,requete) == False:
                print "Modififcation(etape suppression) de l'voiture: {0} {1}, a echoue".format(self.mprenom_voiture, self.mnom_voiture)
                return False

            else:
                print "Modification(etape suppression) de l'voiture: {0} {1}, a reussi".format(self.mprenom_voiture, self.mnom_voiture)

            requete = "INSERT INTO voiture (id_voiture, prenom_voiture, nom_voiture, date_embauche_voiture,salaire_voiture,adresse_l1_voiture,adresse_l2_voiture,cp_voiture,id_ville_voiture,telephone_voiture, email_voiture,commentaire_voiture,poste_voiture,id_grade_voiture,id_service_voiture) VALUES ("+self.mid_voiture+",\'"+self.mprenom_voiture+"\', \'"+self.mnom_voiture+"\',\'"+self.mdate_embauche_voiture+"\',"+self.msalaire_voiture+",\'"+self.madresse_l1_voiture+"\',\'"+self.madresse_l2_voiture+"\',"+self.mcp_voiture+","+self.mville_voiture.GetIdVille()+",\'"+self.mtelephone_voiture+"\',\'"+self.memail_voiture+"\',\'"+self.mcommentaire_voiture+"\',\'"+self.mposte_voiture+"\',"+self.mgrade_voiture.GetIdGrade()+","+self.mservice_voiture.GetIdService()+");"
            
            if MysqlDef.executeRequete(connexion,requete) == False:
                print "Modification(etape insertion) de l'voiture: {0} {1}, a echoue".format(self.mprenom_voiture, self.mnom_voiture)
                return False

            else:
                print "Modification(etape insertion) de l'voiture: {0} {1}, a reussi".format(self.mprenom_voiture, self.mnom_voiture)
                return True


    # Methode pour recuperer un voiture dans la table est fournir les donnees a l'objet voiture

    def GetVoitureFromTableSQL(self,connexion,plist_column_name,plist_parametre):

        if len(plist_column_name) != len(plist_parametre):
            print 'Le nombre de nom de colonne et de parametre fournit est different: Impossible de recupere l\'voiture'
            return False

        else:
            # On cree la requete
            requete = "SELECT * FROM voiture WHERE "
            i = 0
            while i < len(plist_column_name):
                requete = requete+plist_column_name[i]+" = \'"+plist_parametre[i]+"\' "
                if i != len(plist_column_name) -1:
                    requete = requete + " AND "
                i += 1


        resultat = MysqlDef.executeRequete(connexion,requete)
        
        if resultat == False:
            print 'Requperation de l\'voiture impossible'
            return False

        else:
            table = resultat
            self.mid_voiture = str(table[0][0])
            self.mprenom_voiture = table[0][1]
            self.mnom_voiture = table[0][2]
            self.mdate_embauche_voiture = str(table[0][3])
            self.msalaire_voiture = str(table[0][4])
            self.madresse_l1_voiture = table[0][5]
            self.madresse_l2_voiture = table[0][6]
            self.mcp_voiture = str(table[0][7])
            self.mtelephone_voiture = str(table[0][9])
            self.memail_voiture = table[0][10]
            self.mcommentaire_voiture = table[0][11]
            self.mposte_voiture = table[0][12]

            # Recuperation de la ville
            requeteVille = "SELECT id_ville, libelle_ville    FROM ville WHERE id_ville = "+str(table[0][8])
            resultatVille = MysqlDef.executeRequete(connexion,requeteVille)
            self.mville_voiture = Ville.Ville(resultatVille[0][0],resultatVille[0][1])

            # Recuperation du grade
            requeteGrade = "SELECT id_grade, libelle_grade FROM grade WHERE id_grade = "+str(table[0][13])
            resultatGrade = MysqlDef.executeRequete(connexion,requeteGrade)
            self.mgrade_voiture = Grade.Grade(resultatGrade[0][0],resultatGrade[0][1])

            # Recuperation du service
            requeteService = "SELECT id_service, libelle_service, id_service_service FROM service WHERE id_service = "+str(table[0][14])
            resultatService = MysqlDef.executeRequete(connexion,requeteService)
            self.mservice_voiture = Service.Service(resultatService[0][0],resultatService[0][1], resultatService[0][2])

            print 'Recuperation de l\'voiture reussi'


