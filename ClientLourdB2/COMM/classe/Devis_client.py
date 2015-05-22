#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Yan
#
# Created:     07/11/2014
# Copyright:   (c) Yan 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Devis_Client:
    """ classe qui permet l'ajout d'un devis  pour la vente d'une voiture"""
    def __init__(self, p_id, p_date, p_voiture, p_client, p_peinture):
        """constructeur"""

        self.id_devis_client = p_id
        self.date_devis_client = p_date
        self.id_voiture_devis_client = p_voiture
        self.id_client_devis_client = p_client
        self.id_peinture_devis_client = p_peinture

    def getDateDevis(self):
        """ methode qui renvoie la date du devis """
        print("La date du devis ")
        return self.date_devis_client

    def getVoiture(self):
        """ methode qui renvoie la voiture concernee """
        print("voiture ")
        return self.id_voiture_devis_client

    def getClient(self):
        """ methode qui renvoie le client du devis """
        print("Client")
        return self.id_client_devis_client


    def getPeinture(self):
        """ methode qui renvoie la peinture de la voiture concernee """
        print("peinture de la voiture")
        return self.id_peinture_devis_client


    def setVoiture(self, new_voiture):
        """ methode qui permet de modifier une voiture """
        self.id_voiture_devis_client = new_voiture
        print("Voiture :" + self.voiture.getModele())

    def setClient(self, new_client):
        """ methode qui permet de modifier un client """
        self.id_client_devis_client = new_client
        print("Client :" + self.client.getNom()+ " "+self.client.getPrenom())



    def setDateDevis(self, new_date):
        """ methode qui modifie la date du devis """
        self.date_devis_client = new_date
        print("La date du devis est " + self.date_devis_client)

    def setPeinture(self, new_peinture):
        """ methode qui permet de modifier la peinture de la voiture concernee """
        self.id_peinture_devis_client = new_peinture
        print("peinture :" + self.peinture.getLibellePeinture())

    def __del__(self):
        """ methode qui supprime la commande """
        del self
