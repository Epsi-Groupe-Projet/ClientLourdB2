#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Yan
#
# Created:     17/10/2014
# Copyright:   (c) Yan 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Facture_client:
    """ Classe qui permet de rediger une facture pour  le client """

    def __init__(self, p_id, p_date_facture, p_commande_client):
        """ constructeur """

        self.id_facture_client = p_id
        self.date_facture_client = p_date_facture
        self.id_commande_client_facture_client = p_commande_client


    def getDateFacture(self):
        """ methode qui renvoie la date de la facture du client """

        print("Date de la facture ")
        return self.date_facture_client

    def getDatePaiement(self):
        """ methode qui renvoie la date de paiement par le client """

        print("Date de paiement ")
        return self.date_paiement

    def getCommandeClient(self):
        """ methode permettant de renvoyer une commande """
        print("commande ")
        return self.id_commande_client_facture_client

    def getTotalHT(self):
        """ methode qui renvoie le montant hors taxe de la voiture """
        print("Total HT de la voiture")
        return self.total_HT

    def setTotalHT(self, new_total_HT):
        """ methode  qui permet de modifier le montant total hors taxe de la voiture """
        self.total_HT = new_total_HT
        print("Montant hors taxe : "+ self.total_HT)

    def setDateFacture(self, new_date_facture):
        """ methode qui permet de modifier la date de la facture du client """
        self.date_facture_client = new_date_facture
        print("La nouvelle date de facture "+ self.date_facture_client)

    def setDatePaiement(self, new_date_paiement):
        """ methode qui permet de modifier la date de paiement de la facture """

        self.date_paiement = new_date_paiement
        print("La nouvelle date de paiement"+ self.date_paiement)

    def setCommandeClient(self, new_commande):
        """ methode qui permet de modifier une commande """
        self.id_commande_client_facture_client = new_commande
        print("Commande :" + self.commande_client.getDate())

    def __del__(self):
        """ methode qui supprime la facture """
        del self



