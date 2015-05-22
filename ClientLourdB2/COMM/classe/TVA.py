#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Yan
#
# Created:     21/10/2014
# Copyright:   (c) Yan 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class TVA:
    """ classe permettant l'ajout d'une commande  pour l'achat d'une voiture"""
    def __init__(self, p_id, p_taux, p_date ):
        """constructeur"""

        self.id_tva = p_id
        self.taux_tva = p_taux
        self.date_tva = p_date

    def getTaux(self):
        """ methode qui renvoie le taux de tva """
        print("Taux de TVA")
        return self.taux_tva

    def getDate(self):
        """ methode qui renvoie le date de TVA """
        print("Date TVA")
        return self.date_tva

    def setTaux(self, new_taux):
        """ methode qui permet de modifier le taux de tva """
        self.taux_tva = new_taux
        print("Le nouveau taux de TVA " + self.taux_tva)

    def setDate(self, new_date):
        """ methode qui permet de modifier la date de tva """
        self.date_tva = new_date
        print("La date de TVA " + self.date_tva)

    def __del__(self):
        """ methode qui supprime la TVA """
        del self
