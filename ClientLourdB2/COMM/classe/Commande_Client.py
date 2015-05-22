#-------------------------------------------------------------------------------
# Name:        module6
# Purpose:
#
# Author:      Yan
#
# Created:     17/10/2014
# Copyright:   (c) Yan 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Commande_Client:
    """ classe permettant l'ajout d'une commande  pour la vente d'une voiture"""
    def __init__(self, p_id, p_date, p_devis_client, p_client, p_facture):
        """constructeur"""

        self.id_commande_client = p_id
        self.date_commande_client = p_date
        self.devis_client = p_devis_client
        self.id_client_commande_client = p_client
        self.id_facture_client_commande_client = p_facture

    def getDateCommande(self):
        """ methode qui renvoie la date de la commande """
        print("La date de la commande ")
        return self.date

    def getDevisClient(self):
        """ methode qui renvoie le devis de la commande concernee """
        print("Devis ")
        return self.devis_client

    def getClient(self):
        """ methode qui renvoie le client de la commande """
        print("Client")
        return self.id_client_commande_client

    def getFacture(self):
        """ methode qui renvoie la facture de la commande """
        print("Facture de la commande")
        return self.id_facture_client_commande_client


    def setDevisClient(self, new_devis):
        """ methode qui permet de modifier un devis """
        self.devis_client = new_devis
        print("Devis :" + self.devis_client.getDateDevis())

    def setClient(self, new_client):
        """ methode qui permet de modifier un client """
        self.id_client_commande_client = new_client
        print("Client :" + self.client.getNom()+ " "+self.client.getPrenom())

    def setFacture(self, new_facture):
        """ methode qui permet de modifier une facture """
        self.id_facture_client_commande_client = new_facture
        print("Voiture :" + self.facture.getDateFacture())

    def setDateCommande(self, new_date):
        """ methode qui modifie la date de la commande """
        self.date = new_date
        print("La date de la commande est " + self.date)


    def __del__(self):
        """ methode qui supprime la commande """
        del self

