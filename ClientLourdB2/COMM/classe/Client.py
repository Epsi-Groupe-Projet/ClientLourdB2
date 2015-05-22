#-------------------------------------------------------------------------------
# Name:        module7
# Purpose:
#
# Author:      Yan
#
# Created:     17/10/2014
# Copyright:   (c) Yan 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Client :
    """ classe qui permet l'ajout d'un nouveau client """
    def __init__(self, p_id_client, p_nom, p_prenom, p_adresse1, p_adresse2, p_tel, p_email, p_cp, p_ville):
        """ constructeur """

        self.id_client = p_id_client
        self.nom_client = p_nom
        self.prenom_client = p_prenom
        self.adresse_l1_client  = p_adresse1
        self.adresse_l2_client  = p_adresse2
        self.telephone_client = p_tel
        self.email_client = p_email
        self.cp_client = p_cp
        self.nom_ville_client = p_ville


    def getNom(self):
        """methode qui permet de renvoyer le nom du client"""
        print("Nom ")
        return self.nom_client

    def getPrenom(self):
        """methode qui permet de renvoyer le prenom du client"""
        print("Prenom ")
        return self.prenom_client


    def getAdresse1(self):
        """methode qui permet de renvoyer la premiere ligne d'adressse du client"""
        print("Adresse ")
        return self.adresse_l1_client

    def getAdresse2(self):
        """methode qui permet de renvoyer la seconde ligne d'adressse du client"""
        print("Adresse ")
        return self.adresse_l2_client

    def getTelephone(self):
        """methode qui permet de renvoyer le numero de telephone du client"""
        print("Numero ")
        return self.telephone_client

    def getEmail(self):
        """methode qui permet de renvoyer l'email du client"""
        print("Email ")
        return self.email_client

    def getCP(self):
        """methode qui permet de renvoyer le code postal du client"""
        print("Code postal ")
        return self.cp_client

    def getVille(self):
        """methode qui permet de renvoyer la ville du client"""
        print("Ville ")
        return self.nom_ville_client

    def setNom(self, new_nom):
        """ methode qui permet de modifier le nom du client """

        self.nom_client = new_nom
        print("Nom :"+ self.nom_client)

    def setPrenom(self, new_prenom):
        """ methode qui permet de modifier le prenom du client """

        self.prenom_client = new_prenom
        print("Prenom :"+ self.prenom_client)


    def setAdresse1(self, new_adresse1):
        """ methode qui permet de modifier la premiere d'adresse du client """

        self.adresse_l1_client = new_adresse1
        print("Adresse modifiee :"+ self.adresse_l1_client)

    def setAdresse2(self, new_adresse2):
        """ methode qui permet de modifier la seconde ligne d'adresse du client """

        self.adresse_l2_client = new_adresse2
        print("Adresse modifiee :"+ self.adresse_l2_client)

    def setTelephone(self, new_tel):
        """ methode qui permet de modifier le numero de telephone du client """

        self.telephone_client = new_tel
        print("Numero de telephone modifie :"+ self.telephone_client)


    def setEmail(self, new_email):
        """ methode qui permet de modifier l'email du client """

        self.email_client = new_email
        print("Email modifiee:"+ self.email_client)

    def setCP(self, new_cp):
        """ methode qui permet de modifier le code postal du client """

        self.cp_client = new_cp
        print("Code postal modifie :"+ self.cp_client)

    def setVille(self, new_ville):
        """ methode qui permet de modifier la ville du client """

        self.nom_ville_client = new_ville
        print("Ville :"+ self.nom_ville_client)


    def __del__(self):
        """ methode qui supprime le client """
        del self






